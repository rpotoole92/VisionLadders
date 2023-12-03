from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def projects(request):
  #template = loader.get_template("landing/landing.html")
  #return HttpResponse(template.render({},request))
  return HttpResponse("Temporary landing page")
