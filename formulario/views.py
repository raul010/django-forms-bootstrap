from django.shortcuts import render

# Create your views here.
def formUser(request):
    return render(request, 'formulario/index.html', {})