# django_admin
learning


How to to default migrations?

> it already has some schema of the tables.

python manage.py makemigrations  :> it is used to create new model

> python manage.py migrate:  it create some schema which is available in default.


How to install db sqlite

command : sudo apt update
command : sudo apt install sqlitebrowser

Note: if i change the sqlite db with other database and run makemigration it will create all all default tables.


<!-- create super user  -->
cmd: python manage.py createsuperuser

id of admin pannel

username: admin
password: admin


Note: can get the user name and password of superuser inside the table called sqldb>Browse data option .

<!-- what is URL(Route) and Views -->

<!-- function and class based views -->

<!-- how to create Views and Urls and how to connect  -->


How to create dynamic routes url in django

dynamic routes are of three type:

1> int   :     path("home/<int:content_id>",views.home_content,name="content"),
2> str  :  path("home/<str:content_id>",views.home_content,name="content"),
3> slug     : example: hello-ws-iip :     path("home/<slug:course>",views.home_course,name="course")


<!-- how to configure html file using templates -->
from django.shortcuts import render
<!-- views.py -->
def home(request):
    return render(request,'home.html')
<!-- urls.py -->
    path('',views.home,name='home'),


<!-- How to pass data from views.py to templates -->
views.py
def home(request):
    data={
        "title":"Martians"
    }
    return render(request,'home.html',data)

home.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        .main{
        width:1000px;
        background-color: red;
        color: white;

    }
    </style>
    
</head>
<body>
    <div class="main"><h1>Welcome to AI Martians</h1> </div>
    
</body>
</html>



<!-- how to use for loop in django -->
html file

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        .main{
        width:1000px;
        background-color: red;
        color: white;

    }
    </style>
    
</head>
<body>
    <div class="main"><h1>Welcome to AI Martians {{subject}}</h1> </div>
    {% for i in subject %}
    <div class="main">{{forloop.counter}} {{i}}</div>
    {% endfor %}

</body>
</html>

<!-- Django Template using if...elif...else -->

<!-- managing static files (e.g. images,JavaScript,CSS) STATICFILES_DIRS -->

----------------------------------------------------------------------------
configure static folder which contain css and javascript files of a project using 

in settings.py file.

STATICFILES_DIRS=[
    BASE_DIR,"static"
]


---------------------------------------------------------------------------------
Header and footer include in django HTML Tamplate include

Header and footer html file mostly common for all the webpage of a website

NOTE: it is used to reduce repetations 

{% include "header.html" %}
{% include "footer.html" %}

-----------------------------------------------------------------------------
Extends - Django Templates Tags

create a single file of html base.html create  include content of the html between {% block content %} and end the block content {% endblock %}


{% include "header.html" %}

{% block content %}

{% endblock %}

{% include "footer.html" %}

--------------------------------------------------------------------------------
Django URL templates

There are two ways to connect two templates together 

1st way:


2nd way: 

in urls.py

urlpatterns=[
    path("admin/", admin.site.urls),
    path("home/", views.home,name="home"),
    path("about/", views.about,name="about"),
    path("contact-us/",views.contact,name="contact"),
    
]

now in header.html
where all the header details like , home, about, contact icon available

do some changes into 

<a href="{% url 'home' %}">Home</a>
<a href="{% url 'about' %}">About</a>
<a href="{% url 'contact' %}">Contact us</a>

---------------------------------------------------------------------------------------
How to highlight active links in Django

in header.html

<li class="{% if request.path == '/' %} active {% endif %}">
<li class="{% if request.path == '/' %} active {% endif %}">
<li class="{% if request.path == '/' %} active {% endif %}">
