from django.urls import path
from vinayaka.views  import *
app_name='something'

urlpatterns= [
    path('wednesday/',wednesday, name='wednesday'),
]  