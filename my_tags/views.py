from django.shortcuts import render
import datetime
import markdown
from django.utils.safestring import mark_safe
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'index.html', {"x": "welcome to django"})

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def filter_demo(request):
    context = {
        "my_string": "Hello World",
        "my_date": datetime.date(2025, 6, 18),
        "long_string": "This is a long string to be displayed entirely",
        "string_length": "We are learning django programming",
        "optional_value": "",
        "capfirst_string": "my name is John",
        "join_string": ["Django", "is", "awesome"],
        "my_text": "Learning Django is fun",
        "wordcount_line": "Django is a powerful and flexible web framework.",
        "multiline_text": "This is the first line.\nThis is the second line.\nAnd here is the third."
    }
    return render(request, 'filters.html', context)

def login_form(request):
    context = {
        "username": "",
        "email": "",
        "password": ""
    }
    return render(request, 'login.html', context)

def signup_form(request):
    context = {
        "first_name": "",
        "last_name": "",
        "username": "",
        "email": "",
        "password": ""
    }
    return render(request, 'signup.html', context)

def blog_list(request):
    blogs = Blog.objects.prefetch_related('editors').all()
    for blog in blogs:
        blog.rendered_text = mark_safe(markdown.markdown(blog.text))
    return render(request, 'blog_list.html', {'blogs': blogs})