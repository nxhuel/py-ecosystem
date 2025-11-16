# Django learning

1. Levantar venv
```
$ python3 -m venv venv

$ source venv/bin/activate 
// en win cambia: myworld\Scripts\activate.bat

```

2. Preparar el venv
```
$ python3 -m pip install Django

$ django-admin --version

$ pip install pymysql

$ pip list
```

3. Continuar con Django
```
// creacion de proyecto
$ django-admin startproject django_learning

// ejecucion
$ python3 manage.py runserver

// creacion de aplicacion
$ python3 manage.py startapp members

// configuracion de enrutamiento
// members/urls.py
urlpatterns = [
    path('members/', views.members, name='members')
]
// django_learning/urls.py
urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]

// creacion y configuracion de templates
// members/templates/myfirst.html
// codigo simple html

// integrarlo en setting.py para que la carpeta raiz reconozca la aplicacion creada

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members' // <- aca
]

// configurar views.py
def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

// realizacion la migracion
$ python3 manage.py migrate

// creacion de modelos (tablas de una db)
// p.e.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

$ python3 manage.py makemigrations members

$ python3 manage.py migrate

// visualizar las consultar sql 
$ python3 manage.py sqlmigrate members 0001

```

4. Administracion
```
// crear usuario
$ python3 manage.py createsuperuser

```

5. Conexion a mysql
```
$ pip install pymysql

// __init__.py
import pymysql
# pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.install_as_MySQLdb()

// settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

7. API REST
```
$ pip install djangorestframework
```