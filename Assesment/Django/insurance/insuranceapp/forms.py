from django import forms

from .models import insurance, healthdata, lifedata, vehicledata, homedata, traveldata, businessdata


class registerform(forms.ModelForm):
    class Meta:
        model=insurance
        fields='__all__'
        
class healthform(forms.ModelForm):
    class Meta:
        model=healthdata
        fields='__all__'

class lifeform(forms.ModelForm):
    class Meta:
        model=lifedata
        fields='__all__'

class vehicleform(forms.ModelForm):
    class Meta:
        model=vehicledata
        fields='__all__'

class homeform(forms.ModelForm):
    class Meta:
        model=homedata
        fields='__all__'

class travelform(forms.ModelForm):
    class Meta:
        model=traveldata
        fields=['fullnm','em','mobile','type','policy','destination','departure_date','return_date','id_proof','photo','itinerary','driving_license','ticket']

class businessform(forms.ModelForm):
    class Meta:
        model=businessdata
        fields='__all__'

class passform(forms.ModelForm):
    class Meta:
        model=insurance
        fields=['pas']