from django.db import models
from datetime import datetime
# Create your models here.

class Captain_Register(models.Model):
    assign_id = models.AutoField(primary_key=True)

    cap_name = models.CharField(verbose_name='Cap_Name', db_column="cap_name", max_length=50, blank=False,
                                  null=False)
    cap_phone = models.BigIntegerField(verbose_name='Cap_Phone', db_column="cap_phone", blank=False,
                                  null=False)
    cap_license = models.CharField(verbose_name='Cap_License', db_column="cap_license", max_length=50, blank=False,
                                  null=False)
    city = models.CharField(verbose_name='City', db_column="city", max_length=50, blank=False,
                                  null=False)
    vechicle = models.CharField(verbose_name='Vechicle', db_column="vechicle", max_length=50, blank=False,
                                  null=False)

    cap_email = models.EmailField(db_column='cap_email', verbose_name='Cap_Email', max_length=100, null=True, blank=True)
    
    cap_pwd=models.CharField(verbose_name='Cap_Password',db_column="cap_pwd",max_length=100,blank=False,null=False)
    
    
    
    cap_image = models.FileField(verbose_name='Cap_Image', db_column="cap_image", upload_to='Captain/Profile-image/', blank=False,)

    cap_vehicle_image = models.FileField(verbose_name='Cap_Vehicle_Image', db_column="cap_vehicle_image", upload_to='Captain/Vehicle-image/', blank=False,)

    cap_driving_lic = models.FileField(verbose_name='Cap_Driving_Lic', db_column="cap_driving_lic", upload_to='Captain/Driving-image/', blank=False,)

    
    status = models.CharField(verbose_name='Status', db_column="status", max_length=50, blank=False,
                                  default='Pending')
    datetime_created = models.DateTimeField(default=datetime.now)
    
    class Meta:
        db_table='Captain_Register'

