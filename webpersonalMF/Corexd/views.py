from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi Web Personal</h1>
     <ul>
         <li><a href="/">Portada</a></li>
         <li><a href="/about/">Acerca de....</a></li>
         <li><a href="/portafolio/">Arcihivos del proyecto</a></li>
         <li><a href="/Contact/">Contacto Personal</a></li>
         </ul>
"""
# Create your views here.
def home(request):
    return render(request, "Corexd/home.html")

def about(request):
    return render(request, "Corexd/about.html")

def Contact(request):
    return render(request, "Corexd/Contact.html")
