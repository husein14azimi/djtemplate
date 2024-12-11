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
> this `readme` is to demonstrate the path to implement the profile picture feature in the project (and also deployment). the `jwt auth` and `jalali-datetime` features are built in the previous repositories. you can say this project is built on the basis of them.




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


<br></br>
<br></br>
<br></br>
<br></br>
<br></br>


## Deployment

the project is currently ran on <href>https://emcby1.pythonanywhere.com</href>.

first, after creating a free account on <href>https://pythonanywhere.com</href>, you have to start a console. after choosing `console: python 10` (the maximum version you can find there), in the `/home` directory, clone the repository:
```
git clone https://github.com/husein14azimi/djtemplate
```
and then head to the `home/.virtualenvs` and run:
```
python -m venv venv_djtemplate
```
(the name of the virtual environment is mandatory)

in the `.virtualenvs`, activate the venv:
```
source venv_djtemplate/bin/activate
```
now we have activated our empty venv. go to your cloned repository and use the requirements.txt you had created before:
```
pip install -r requirements.txt
```

### web app
head to the `Web` section and click on the start a new web app. you will choose your technology here. DON'T choose the django; because it only provides `django4`; but rest_framework requires `django5`. therefore, we will use the `venv` we just created. in that list, click on the `manual` or the same meaning thing; that lets you use your `venv` instead of using pre-built engines. after you choose that, the redirects you directly to the **web app manage** section. in there, you are going to make some changes. let's start from the top:

#### Code
in this section, change the `source code` to the cloned repository (project's directory):
```
/home/emcby1/djtemplate
```

your working directory should be set to
```
/home/<username>/
```

change the `wsgi` conf:
click on the link and in the file, configurations for each technology is written, but commented. find the `DJANGO` section and un-comment them. make some changes in the addressing and path:
```
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/emcby1/mysite/mysite/settings.py'
# and your manage.py is is at '/home/emcby1/mysite/manage.py'
path = '/home/emcby1/djtemplate'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
save the file.


#### virtualenv
add the path to your venv
```
/home/emcby1/.virtualenvs/venv_djtemplate
```
if you want to know whether you have provided the right link, you can click on the **start a console in this venv**


#### static files

in the dev phase (localhost), because of `DEBUG=True`, you will see the admin panel with writing no configuration. on the server, you have to make some changes on the project files (this means that you should go to the `files` section, click on each file, make the changes and save it) and after that, come back to the `web` section and do the last thing in this part.

* write the static settings in the `core.settings`:
    ```
    STATIC_URL = '/static/'
    STATIC_ROOT = '/home/emcby1/djtemplate/staticfiles'
    ```
    note that the `STATIC_ROOT` depends on your profile and project name.

* run the `python manage.py collectstatic`

* after the command, you are going to have to add the url and path to the static in the `Web` section: `static files` in the pythonanywhere dashboard.
    ```
    url: /static/
    path: /home/emcby1/djtemplate/staticfiles
    ```





### Lastly,
there are some configurations on the server which are not done in the local storage:

* adding the `pythonanywhere`'s given domain to the `core.settings.ALLOWED_HOSTS`:
    ```
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'emcby1.pythonanywhere.com',]
    ```

* click on the **reload app** in the `web` section.

* if you don't see the project when you hit the url, try running
    ```
    python manage.py runserver
    ```
    once.




