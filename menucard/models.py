from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
import uuid
# Create your models here.


class Project(models.Model):
    TYPE_CHOICE = (
        ('SAVE THE DATE','SAVE THE DATE'),
        ('WEDDING','WEDDING'),
        ('ENGAGEMENT','ENGAGEMENT')
    )
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=30, choices=TYPE_CHOICE)
    uid = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    groom_name = models.CharField(max_length=250)
    groom_image =  VersatileImageField('groom_image',blank=True,null=True,upload_to="images/",ppoi_field='ppoi')
    ppoi = PPOIField('groom_image PPOI')
    about_groom = models.TextField()
    groom_instagram = models.URLField(null=True, blank=True)
    groom_facebook = models.URLField(null=True, blank=True)
    bride_name = models.CharField(max_length=250)
    bride_image =  VersatileImageField('bride_image',blank=True,null=True,upload_to="images/",ppoi_field='ppoi')
    ppoi = PPOIField('bride_image PPOI')
    about_bride = models.TextField()
    bride_instagram = models.URLField(null=True, blank=True)
    bride_facebook = models.URLField(null=True, blank=True)
    date = models.DateField()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

class Banner(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    banner_image = VersatileImageField('banner_image',blank=True,null=True,upload_to="images/banner/",ppoi_field='ppoi')
    ppoi = PPOIField('banner_image PPOI')

    def __str__(self):
        return self.project