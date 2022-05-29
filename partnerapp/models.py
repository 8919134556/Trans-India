from django.db import models
from datetime import datetime

# Create your models here.

class Partner_Register(models.Model):
    assign_id = models.AutoField(primary_key=True)

    par_name = models.CharField(verbose_name='Par_Name', db_column="par_name", max_length=50, blank=False,
                                  null=False)
    par_phone = models.BigIntegerField(verbose_name='Par_Phone', db_column="par_phone", blank=False,
                                  null=False)
    partner = models.CharField(verbose_name='Partner', db_column="partner", max_length=50, blank=False,
                                  null=False)
    city = models.CharField(verbose_name='City', db_column="city", max_length=50, blank=False,
                                  null=False)
    par_license = models.CharField(verbose_name='Par_license', db_column="par_license", max_length=50, blank=False,
                                  null=False)

    par_email = models.EmailField(db_column='par_email', verbose_name='Par_Email', max_length=100, null=True, blank=True)
    
    par_pwd=models.CharField(verbose_name='Par_Password',db_column="par_pwd",max_length=100,blank=False,null=False)
    
    
    
    par_image = models.FileField(verbose_name='Par_Image', db_column="par_image", upload_to='Partner/Profile-image/', blank=False,)

   

    par_lic = models.FileField(verbose_name='Par_Lic', db_column="par_lic", upload_to='Partner/Lic-image/', blank=False,)

    
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  default='pending')
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Partner_Register'

class Two_wheeler(models.Model):
    assign_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name', db_column='Name', max_length=50, blank=False)
    price = models.CharField(verbose_name='Price', db_column='price', max_length=50,blank=False)

    class Meta:
        db_table='Two_wheeler'

class Four_wheeler(models.Model):
    assign_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name', db_column='Name', max_length=50, blank=False)
    price = models.CharField(verbose_name='Price', db_column='price', max_length=50,blank=False)
    image = models.FileField(verbose_name='Image', db_column="image", upload_to='demo/', blank=False, default="null")

    class Meta:
        db_table='Four_wheeler'

class Lynk_Four_wheeler(models.Model):
    assign_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name', db_column='Name', max_length=50, blank=False)
    price = models.CharField(verbose_name='Price', db_column='price', max_length=50,blank=False)
    image = models.FileField(verbose_name='Image', db_column="image", upload_to='demo/', blank=False, default="null")

    class Meta:
        db_table='Lynk_Four_wheeler'


    
