from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home </h1>')

def about(request):
<<<<<<< HEAD
    return render(request, 'blog/about.html', {'title': 'About'})
=======
    return HttpResponse('<h1>Blog About </h1>')
>>>>>>> origin/main
