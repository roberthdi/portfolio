from django.shortcuts import render
from .models import Certificados

# Create your views here.
def certificates(request):
    certificado = Certificados.objects.all()
    return render (request, "certificados/certificates.html", {'certificado':certificado})