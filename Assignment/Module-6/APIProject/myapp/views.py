from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from myapp.models import bookdata
from myapp.serializer import bookserial


# Create your views here.

@api_view(['GET'])
def getall(request):
    try:
        data=bookdata.objects.all()
    except bookdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=bookserial(data,many=True)
    return Response(data=serial.data)

@api_view(['GET'])
def getone(request,id):
    try:
        data=bookdata.objects.get(id=id)
    except bookdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=bookserial(data)
    return Response(data=serial.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def addbook(request):
    if request.method=='POST':
        serial=bookserial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def updatebook(request,id):
    try:
        data1=bookdata.objects.get(id=id)
    except bookdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serial=bookserial(data1)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=bookserial(data=request.data,instance=data1)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE','GET'])
def deletebook(request,id):
    try:
        data=bookdata.objects.get(id=id)
    except bookdata.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=bookserial(data)
        return Response(data=serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        bookdata.delete(data)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
