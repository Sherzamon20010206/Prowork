

from django.db import models
import datetime
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

class Type(models.Model):
        type = models.CharField(max_length=300, null=True, blank=True)

        def __str__(self):
          return  self.type
class Kitob(models.Model):
    title=models.CharField(max_length=300,null=True,blank=True)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,null=True,blank=True)
    img=models.ImageField(upload_to="document",null=True,blank=True)
    tag=models.TextField(null=True,blank=True)
    data=models.TimeField(auto_now_add=True,null=True,blank=True)
    file=models.FileField(upload_to="DocFile",null=True,blank=True)
    slug = models.SlugField(null=True, blank=True, max_length=125)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
