# Generated by Django 5.1.3 on 2024-12-04 19:02

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_picture',
            field=models.ImageField(default='account/images/profiles/defaultProfilePicture.png', upload_to='account/images/profiles', validators=[account.validators.validate_file_size]),
        ),
    ]