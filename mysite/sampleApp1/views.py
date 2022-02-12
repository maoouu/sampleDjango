from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(response):
    # This is how you load an html file from template
    # render(HTMLResponse, <directory-to-file>)
    return render(response, "sampleApp1/index.html")