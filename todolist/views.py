from django.shortcuts import render

# Create your views here.
def loginn(request):
    return render(request, 'loginn.html')

def signn(request):
    return render(request, 'signn.html')