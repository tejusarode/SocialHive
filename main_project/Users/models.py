from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage


import os

# Custom storage for uploaded avatars
avatar_storage = FileSystemStorage(location=os.path.join('media', 'avatars'))

class RegisterUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True, null=False, blank=False)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])

    # For default avatars
    avatar = models.CharField(max_length=255, choices=[
        ('css/avatar1.png', 'Avatar 1'),
        ('css/avatar2.png', 'Avatar 2'),
        ('css/avatar3.png', 'Avatar 3'),
        ('css/avatar4.png', 'Avatar 4'),
        ('custom avatar', 'Custom Upload'),  # Option for custom avatar upload
    ], default='')

    
    custom_avatar = models.ImageField(upload_to='avatars/', storage=avatar_storage, null=True, blank=True)

    bio = models.TextField(max_length=200, blank=True, null=True)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)


    #to check if user uploaded custom avatar then custom avatar else one from the default avatar
    def get_avatar(self):
        if self.avatar == 'custom avatar' and self.custom_avatar:
            return self.custom_avatar.url
        elif self.avatar:
            return f'/static/{self.avatar}'  
        return None
    
    # Ensure that followers_count and following_count are non-negative
    def save(self, *args, **kwargs): # custom save method for RegisterUser  which takes any number of arguements and keyword arguements 
        if self.following_count < 0:
            self.following_count = 0
        if self.followers_count < 0:
            self.followers_count = 0
        super().save(*args, **kwargs)#Calls the parents class save method 

    def __str__(self):# it is magic method that is how our data is going to be visible instead of object
        return self.username
    
class Follow(models.Model):
    user = models.ForeignKey(RegisterUser, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(RegisterUser, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'follower')
