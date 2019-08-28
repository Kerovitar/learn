from django.db import models

# Create your models here.
class PoolMaterial(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description = models.TextField("Description", blank=True)


class PoolType(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description = models.TextField("description", blank=True)


class Pool(models.Model):
    
    name = models.CharField("Name", max_length=120)
    img = models.ImageField("Image")
    volume = models.BigIntegerField("Volume")
    type =models.ForeignKey(PoolType, models.SET_NULL, null=True) 
    material = models.ForeignKey(PoolMaterial, models.SET_NULL, null=True)
    
    
class FountainMaterial(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description = models.TextField("Description", blank=True)
    
    
class FountainType(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description = models.TextField("Description", blank=True)     
    
    
class Fountain(models.Model):
    
    name = models.CharField("Name", max_length=120)
    img = models.ImageField("Image")
    video = models.FileField("Video")
    type = models.ForeignKey(FountainType, models.SET_NULL, null=True)
    material = models.ForeignKey(FountainMaterial, models.SET_NULL, null=True)
    
    
class BathMaterial(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description = models.TextField("Description", blank=True)    
    
        
class BathType(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description =models.TextField("Description", blank=True)    
    
    
class Bath(models.Model):
        
    name = models.CharField("Name", max_length=120)
    img = models.ImageField("Image")
    type = models.ForeignKey(BathType, models.SET_NULL, null=True)
    material = models.ForeignKey(BathMaterial, models.SET_NULL, null=True)
    
 
class SPAMaterial(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description = models.TextField("Description", blank=True)     
    

class SPAType(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description =models.TextField("Description", blank=True)    
    
    
class SPA(models.Model):
        
    name = models.CharField("Name", max_length=120)
    img = models.ImageField("Image")
    type = models.ForeignKey(SPAType, models.SET_NULL, null=True)
    material = models.ForeignKey(SPAMaterial, models.SET_NULL, null=True)
    

class HummumMaterial(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description =models.TextField("Description", blank=True) 
    

class HummumType(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description = models.TextField("Description", blank=True)    
    
    
class Hummum(models.Model):
        
    name = models.CharField("Name",  max_length=120)
    img = models.ImageField("Image")
    type = models.ForeignKey(HummumType, models.SET_NULL, null=True)
    material = models.ForeignKey(HummumMaterial, models.SET_NULL, null=True)
    

class AutowatMaterial(models.Model):
    
    name = models.CharField("Name", max_length=120)
    description =models.TextField("Description", blank=True)
    

class Autowat(models.Model):
        
    name = models.CharField("Name",  max_length=120)
    img = models.ImageField("Image")
    material = models.ForeignKey(AutowatMaterial, models.SET_NULL, null=True)       
           
           
class Contact(models.Model):
    
    adress = models.TextField("Adress")
    tel = models.CharField("Tel", max_length=30)
    email = models.CharField("Email", max_length=50)
    map = models.URLField("Map")    

    