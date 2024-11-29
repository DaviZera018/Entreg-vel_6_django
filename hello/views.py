from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1> Hello, World! Bem-vindo ao app Hello! </h1>")
