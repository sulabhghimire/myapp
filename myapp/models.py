from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import pytz
from PIL import Image

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    avatar = models.ImageField(upload_to='profile_pics')
    country = CountryField()
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
    
        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

        try:
            this = UserProfile.objects.get(id=self.id)
            if this.avatar != self.avatar:
                this.avatar.delete()
        except: pass

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    created_at = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=1000)
    