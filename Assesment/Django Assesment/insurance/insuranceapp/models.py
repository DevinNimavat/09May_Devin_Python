from django.db import models

# Create your models here.


class insurance(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fnm=models.CharField(max_length=20)
    lnm=models.CharField(max_length=20)
    em=models.EmailField()
    unm=models.CharField(max_length=20)
    pas=models.CharField(max_length=16)
    dob=models.DateField()
    mobile=models.BigIntegerField()
    
# Health
class healthdata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullnm=models.CharField(max_length=20)
    em=models.EmailField()
    mobile=models.BigIntegerField()
    type=models.CharField(max_length=20)
    policy_no=models.BigIntegerField()
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    id_proof=models.ImageField(upload_to=f'Images/Health/ID Proof')
    health_certi=models.ImageField(upload_to='Images/Health/Certificate/')
    photo=models.ImageField(upload_to='Images/Health/Photo/')
    hospital_bill=models.ImageField(upload_to='Images/Health/Hospital Bill/')

# Life
class lifedata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullnm=models.CharField(max_length=20)
    em=models.EmailField()
    mobile=models.BigIntegerField()
    type=models.CharField(max_length=20)
    policy=models.BigIntegerField()
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    id_proof=models.FileField(upload_to='Images/Life/ID Proof')
    income=models.FileField(upload_to='Images/Life/Income')
    photo=models.FileField(upload_to='Images/Life/Photos')
    beneficiary_details=models.FileField(upload_to='Images/Life/Beneficiary')

# Vehicle

class vehicledata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullnm=models.CharField(max_length=20)
    em=models.EmailField()
    mobile=models.BigIntegerField()
    type=models.CharField(max_length=20)
    policy=models.BigIntegerField()
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    id_proof=models.FileField(upload_to='Images/Vehicle/ID Proof')
    vehicle_reg=models.FileField(upload_to='Images/Vehicle/Registration/')
    photo=models.FileField(upload_to='Images/Vehicle/Photo/')
    insurance_details=models.FileField(upload_to='Images/Vehicle/Insurance/')

# Home
class homedata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullnm=models.CharField(max_length=20)
    em=models.EmailField()
    mobile=models.BigIntegerField()
    type=models.CharField(max_length=20)
    policy=models.BigIntegerField()
    property_value=models.BigIntegerField()
    property_address=models.CharField(max_length=100)
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    id_proof=models.FileField(upload_to='Images/Home/ID Proof')
    photo=models.FileField(upload_to='Images/Home/Photo/')
    bill=models.FileField(upload_to='Images/Home/Bill/')
    property_doc=models.FileField(upload_to='Images/Home/Property/')

# Travel

class traveldata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullnm=models.CharField(max_length=20)
    em=models.EmailField()
    mobile=models.BigIntegerField()
    type=models.CharField(max_length=20)
    policy=models.BigIntegerField()
    destination=models.BigIntegerField()
    departure_date=models.DateField()
    return_date=models.DateField()
    id_proof=models.FileField(upload_to='Images/Travel/ID Proof')
    photo=models.FileField(upload_to='Images/Travel/Photo/')
    itinerary=models.FileField(upload_to='Images/Travel/Itinerary/')
    visa=models.FileField(upload_to='Images/Travel/Visa/')
    ticket=models.FileField(upload_to='Images/Travel/Ticket/')
    driving_license=models.FileField(upload_to='Images/Travel/Driving License')

# business
class businessdata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    fullnm=models.CharField(max_length=20)
    business_em=models.EmailField()
    owner_no=models.BigIntegerField()
    business_nm=models.CharField(max_length=20)
    business_no=models.BigIntegerField()
    gts_no=models.BigIntegerField()
    business_type=models.CharField(max_length=20)
    type=models.CharField(max_length=50)
    policy=models.BigIntegerField()
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    id_proof=models.FileField(upload_to='Images/Business/ID Proof')
    tax_certi=models.FileField(upload_to='Images/Business/Tax Certi/')
    financial_statement=models.FileField(upload_to='Images/Business/Financial Statement/')
    business_photo=models.FileField(upload_to='Images/Business/Business Photo/')
    gts_photo=models.FileField(upload_to='Images/Business/GTS Photo/')
    photo=models.FileField(upload_to='Images/Business/Photo/')