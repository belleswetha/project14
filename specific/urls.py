from specific.views import *
from django.urls import path

app_name='something'

urlpatterns=[
    path('gangubhai/',gangubhai,name='gangubhai'),
    path('rajiyabhai/',rajiyabhai,name='rajiyabhai'),
]