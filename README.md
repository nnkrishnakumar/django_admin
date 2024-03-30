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



