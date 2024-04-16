from django.shortcuts import render
 #instrucion quese le muestra al usuario para poder verla en web
from django.http import HttpResponse

#declarar un funcion
def  inicio(request):
    return render(request,'paginas/inicio.html')

    #funcion que conecta la los html
def usuario (request):
    return render(request,'paginas/usuario.html')

#esta es la carpeta de donde esta el index
def cliente(request):
    return render(request,"cliente/index.html")

#esta es la carpeta de donde esta el crear.html 
def crear(request):
    return render(request,"cliente/crear.html")

#esta es la carpeta de donde esta el crear.html 
def editar(request):
    return render(request,"cliente/editar.html")
