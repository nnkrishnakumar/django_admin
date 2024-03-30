from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world")

def home_content(request,content_id):
    return HttpResponse("this is content of home page")


# this will take the argument in the form of string 
def home_id(request,id):
    return HttpResponse(id)

# slug : slug contain "-" related values
def home_course(request,course):
    return HttpResponse(course)