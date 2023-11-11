from django.shortcuts import render

# Create your views here.
def startapp(request):
    return render(request, 'index.html')