from django.shortcuts import render
from django.http import HttpResponse

import yaml
import os

def index(request):
    currentfilepath = os.path.dirname(os.path.abspath(__file__))
    projpath = nthParent(currentfilepath,1)
    config = yaml.safe_load(open(projpath+"/resources/config.yml"))

    return HttpResponse("Hello, world. You're at the polls index."+config["xvar"])

def nthParent(path,n):
    result = os.sep.join(path.split(os.sep)[:-n])
    return result