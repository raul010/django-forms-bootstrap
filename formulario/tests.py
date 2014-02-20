from django.test.client import Client

from formulario.models import AuthorForm


client = Client();
f = AuthorForm()

new_author = f.save(commit=False)

new_author.some_field = 'some_value'

new_author.save()

f.save_m2m()

