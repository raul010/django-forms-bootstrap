# -*- coding: utf-8 -*-
from django.shortcuts import render

from formulario.models import AuthorForm, Author


def formUser(request):
    
    author = Author.objects.all()
    
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.some_field = 'some_value'
            new_author.save()
            form.save_m2m()
            print('Válido')
#             HttpResponseRedirect(reverse('form:form-user'))
    else:
        form = AuthorForm()
        print('Inválido')
    
    return render(request, 'formulario/form-user.html', {
                                                         
         "author": author,
         "form": form,
    })          


def formUm(request):
    return render(request, 'formulario/index.html', {})
