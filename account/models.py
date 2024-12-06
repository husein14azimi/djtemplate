# account.models

from django.db import models
from django.conf import settings
from . import validators

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class Person(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='images/profiles', default='images/profiles/defaultProfilePicture.png', validators=[validators.validate_file_size], blank=True)

    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}: {self.user.email}'