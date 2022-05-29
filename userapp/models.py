from django.db import models
from datetime import datetime
# Create your models here.
class User_Register(models.Model):
    assign_id = models.AutoField(primary_key=True)

    user_name = models.CharField(verbose_name='User_Name', db_column="user_name", max_length=50, blank=False,
                                  null=False)
    user_phone = models.BigIntegerField(verbose_name='User_Phone', db_column="user_phone", blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True)
    user_pwd=models.CharField(verbose_name='User_Password',db_column="user_pwd",max_length=100,blank=False,null=False)
    user_image = models.FileField(verbose_name='User_Image', db_column="user_image", upload_to='User/Profile-image/', blank=False,)
    user_otp = models.BigIntegerField(verbose_name='User_otp', db_column="user_otp", blank=False,
                                  null=True)
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='User_Register'

class Rapido(models.Model):
    a_id = models.AutoField(primary_key=True)

    orgine= models.CharField(verbose_name='Orgine', db_column="orgine", max_length=50, blank=False,
                                  null=False)
    destination= models.CharField(verbose_name='Destination', db_column="destination", max_length=50, blank=False,
                                  null=False)
    distance = models.CharField(verbose_name='Distance', db_column="distance", max_length=50, blank=False, 
                                  null=False)
    subtotal = models.CharField(verbose_name='Subtotal', db_column="subtotal", max_length=50, blank=False,
                                  null=False)
    gst = models.CharField(verbose_name='Gst', db_column="gst", max_length=50, blank=False,
                                  null=False)
    total = models.CharField(verbose_name='Total', db_column="total", max_length=50, blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True, default='pending')

    cap_id = models.CharField(verbose_name='Cap_id', db_column="cap_id", max_length=50, blank=False,
                                  null=True)
    cap_name = models.CharField(verbose_name='Cap_name', db_column="cap_name", max_length=50, blank=False,
                                  null=True)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  null=True, default='pending')
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Rapido'

class Portor(models.Model):
    a_id = models.AutoField(primary_key=True)

    orgine= models.CharField(verbose_name='Orgine', db_column="orgine", max_length=50, blank=False,
                                  null=False)
    
    destination= models.CharField(verbose_name='Destination', db_column="destination", max_length=50, blank=False,
                                  null=False)
    distance = models.CharField(verbose_name='Distance', db_column="distance", max_length=50, blank=False, 
                                  null=False)
    subtotal = models.CharField(verbose_name='Subtotal', db_column="subtotal", max_length=50, blank=False,
                                  null=False)
    gst = models.CharField(verbose_name='Gst', db_column="gst", max_length=50, blank=False,
                                  null=False)
    total = models.CharField(verbose_name='Total', db_column="total", max_length=50, blank=False,
                                  null=False)
    vechile_type= models.CharField(verbose_name='Vechile_type', db_column="vechile_type", max_length=50, blank=False,
                                  null=True)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True, default='pending')
    
    cap_id = models.CharField(verbose_name='Cap_id', db_column="cap_id", max_length=50, blank=False,
                                  null=True)
    cap_name = models.CharField(verbose_name='Cap_name', db_column="cap_name", max_length=50, blank=False,
                                  null=True)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  null=True, default='pending')
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Portor'

class swiggy_genie(models.Model):
    a_id = models.AutoField(primary_key=True)

    orgine= models.CharField(verbose_name='Orgine', db_column="orgine", max_length=50, blank=False,
                                  null=False)
    destination= models.CharField(verbose_name='Destination', db_column="destination", max_length=50, blank=False,
                                  null=False)
    distance = models.CharField(verbose_name='Distance', db_column="distance", max_length=50, blank=False, 
                                  null=False)
    subtotal = models.CharField(verbose_name='Subtotal', db_column="subtotal", max_length=50, blank=False,
                                  null=False)
    gst = models.CharField(verbose_name='Gst', db_column="gst", max_length=50, blank=False,
                                  null=False)
    total = models.CharField(verbose_name='Total', db_column="total", max_length=50, blank=False,
                                  null=False)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True, default='pending')

    cap_id = models.CharField(verbose_name='Cap_id', db_column="cap_id", max_length=50, blank=False,
                                  null=True)


    cap_name = models.CharField(verbose_name='Cap_name', db_column="cap_name", max_length=50, blank=False,
                                  null=True)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  null=True, default='pending')
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='swiggy_genie'

class Lynk(models.Model):
    a_id = models.AutoField(primary_key=True)

    orgine= models.CharField(verbose_name='Orgine', db_column="orgine", max_length=50, blank=False,
                                  null=False)
    destination= models.CharField(verbose_name='Destination', db_column="destination", max_length=50, blank=False,
                                  null=False)
    distance = models.CharField(verbose_name='Distance', db_column="distance", max_length=50, blank=False, 
                                  null=False)
    subtotal = models.CharField(verbose_name='Subtotal', db_column="subtotal", max_length=50, blank=False,
                                  null=False)
    gst = models.CharField(verbose_name='Gst', db_column="gst", max_length=50, blank=False,
                                  null=False)
    total = models.CharField(verbose_name='Total', db_column="total", max_length=50, blank=False,
                                  null=False)
    vechile_type= models.CharField(verbose_name='Vechile_type', db_column="vechile_type", max_length=50, blank=False,
                                  null=True)
    user_email = models.EmailField(db_column='user_email', verbose_name='User_Email', max_length=100, null=True, blank=True, default='pending')

    cap_id = models.CharField(verbose_name='Cap_id', db_column="cap_id", max_length=50, blank=False,
                                  null=True)
    cap_name = models.CharField(verbose_name='Cap_name', db_column="cap_name", max_length=50, blank=False,
                                  null=True)
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  null=True, default='pending')
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Lynk'

class User_feedback (models.Model):
    fee_id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name', db_column='Name', max_length=50, blank=False, null=True)
    phone = models.BigIntegerField(verbose_name='Phone', db_column="phone", blank=False,null=True)
    
    orgniztion = models.CharField(verbose_name='Orgniztion', db_column='orgniztion', max_length=50, blank=False)
    order_id = models.CharField(verbose_name='Order_id', db_column='order_id', max_length=50, blank=False, null=True)
    description = models.CharField(verbose_name='Description', db_column='description', max_length=50, blank=False)
    rating = models.BigIntegerField(verbose_name='Rating', db_column="rating", blank=False,null=True)
    class Meta:
        db_table='User_feedback'