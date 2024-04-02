from django.urls import path
from venkateswara.views  import *
app_name='anything'

urlpatterns=[
    path('saturday/',saturday, name='saturday'),
]