from django.db import models

# Create your models here.----------------------------------------------------------
class CatagoryHub(models.Model):
    catagory_name = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.catagory_name
    class Meta:
        verbose_name = 'CatagoryHub'
        verbose_name_plural = 'CatagoryHubs'

# -------------------------------------------------------------------------------------

class CatagoryInitial(models.Model):
    catagory = models.ForeignKey(CatagoryHub, on_delete=models.CASCADE)
    intial_name = models.CharField(max_length=60, blank=True, null=True)
    def __str__(self):
        return self.intial_name
    class Meta:
        verbose_name = 'CatagoryInitial'
        verbose_name_plural = 'CatagoryInitials'

# -------------------------------------------------------------------------------------

class CatagorySecondary(models.Model):
    
    catagoryInitail = models.ForeignKey(CatagoryInitial, on_delete=models.CASCADE)
    secondary_name = models.CharField(max_length=60, blank=True, null=True)

    
    def __str__(self):
        return self.secondary_name
    
    class Meta:
        verbose_name = ("CatagorySecondary")
        verbose_name_plural = ("CatagorySecondaries")

# -------------------------------------------------------------------------------------

class MobileProductDetail(models.Model):
    product_Name = models.CharField(max_length=50, blank=False, null=False)
    product_Image = models.ImageField(upload_to ='uploads/')
    product_Cost = models.BigIntegerField(blank=False, null=False)
    product_Discount = models.BigIntegerField(blank=True, null=True)
    product_Color = models.CharField(max_length=50, blank=False, null=False)
    delivery_Address = models.CharField(max_length=80, blank=False, null=False)
    product_Highlight = models.CharField(max_length=80, blank=False, null=False)
    
    class Meta:
        verbose_name = ("MobileProductDetail")
        verbose_name_plural = ("MobileProductDetails")

    def __str__(self):
        return self.product_Name

# -------------------------------------------------------------------------------------

class Highlight(models.Model):
    highLights = models.ForeignKey(MobileProductDetail, related_name='highlights', on_delete=models.CASCADE)
    highLights_Rom = models.CharField(max_length=50, blank=False, null=False)
    highLights_Ram = models.CharField(max_length=50, blank=False, null=False)
    highLights_Display = models.CharField(max_length=50)
    highLights_Cemara = models.CharField(max_length=50)
    highLights_Battery = models.CharField(max_length=50)
    highLights_Processor = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Highlight")
        verbose_name_plural = ("Highlights")

    def __str__(self):
        return self.highLights_Ram

# -------------------------------------------------------------------------------------

class DeliveryAddress(models.Model):
    delivery_address = models.ForeignKey(MobileProductDetail, related_name='deliveries', on_delete=models.CASCADE)
    delivery_House_No = models.CharField(max_length=60, blank=False, null=False)
    delivery_Street = models.CharField(max_length=60)
    delivery_City = models.CharField(max_length=60, blank=False, null=False)
    delivery_Pin_Code = models.CharField(max_length=60, blank=False, null=False)
    delivery_State = models.CharField(max_length=60)
    delivery_Country = models.CharField(max_length=60, blank=False, null=False)

    class Meta:
        verbose_name = ("Delivary")
        verbose_name_plural = ("Delivaries")

    def __str__(self):
        return self.delivery_State

# -------------------------------------------------------------------------------------



