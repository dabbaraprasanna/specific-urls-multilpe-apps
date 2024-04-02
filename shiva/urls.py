from django.urls import path
from shiva.views  import *
app_name='everthing'

urlpatterns=[
    path('god/', god, name='god'),
]