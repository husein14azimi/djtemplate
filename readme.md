<br></br>
<p align="center">
IN THE NAME OF GOD
</p>


<br></br>

# django template project 💻

this is a template project to prevent coding for common usual stuff:
* rest API
* email-based authentication
* jwt-token-based authentication
* converting the gregorian date-time values from DB to jalali ones
* implementing profile picture for users


> [!NOTE]
> this `readme` is to demonstrate the path to implement the profile picture feature in the project. the `jwt auth` and `jalali-datetime` features are built in the previous repositories. you can say this project is built on the basis of them.




## coding flow for the profile picture feature

first, create a directory in the base directory and name it `media`

then, write in the `core.settings`:
```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

in the `core.urls`, add the following:
```
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

then, to test if the settings and urls work properly, you can manually paste a photo to the `media` directory and hit the url:

`localhost:8000/media/<picture-name.png>`

so if you see the image, the configurations work properly so far.

### adding the `profile_picture` to `Person` model (profile model)

in other situations like pictures for a social account or pictures of a product or course, there can be more than one image associated to the parent model; but in here, we know that each user can have only one p. picture; therefore, we will define a new model named profile picture