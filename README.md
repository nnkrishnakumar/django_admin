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