from django.urls import path
from AppWeb.views import home, servicio, tienda, blog, contacto


urlpatterns = [

    path('', home, name='home'),
    path('servicios/', servicio,  name='servicios'),
    path('tienda/', tienda, name='tienda'),
    path('blog/', blog,  name='blog'),
    path('contacto/', contacto,  name='contacto'),

]
