from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):

    return render(request, 'AppWebTemp/home.html')


def servicio(request):

    return render(request, 'AppWebTemp/servicios.html')


def tienda(request):

    return render(request, 'AppWebTemp/tienda.html')


def blog(request):

    return render(request, 'AppWebTemp/blog.html')


def contacto(request):

    return render(request, 'AppWebTemp/contacto.html')
