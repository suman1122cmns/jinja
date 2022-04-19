from django.shortcuts import render

# Create your views here.
def first (reqest):
    d={'name':'suman'}
    return render(reqest,'jinja.html',context=d)
