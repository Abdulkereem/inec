from django.shortcuts import render, HttpResponse
from idcard.models import Id_Card
import weasyprint
from os import getcwd
from random import randint
from .utils import Render

# Create your views here.
url = []
def home(request):
    ids = Id_Card.objects.all()
    context ={
        "ids":ids
    }
    return render(request,'id.html',context) #Render.render('id.html',context)


def convert(request):
    filename =getcwd()+'/templates/pdf/laide.pdf'
    pdf = weasyprint.HTML(url[-1]).write_pdf(str(filename))
    response = HttpResponse(filename, mimetype='application/pdf')
    return response


