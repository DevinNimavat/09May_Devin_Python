from rest_framework import serializers

from myapp.models import bookdata


class bookserial(serializers.ModelSerializer):
    class Meta:
        model=bookdata
        fields='__all__'