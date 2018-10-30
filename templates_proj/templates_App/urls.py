from django.urls import path
from templates_App import views


#TEMPLATE TAGGING
app_name = 'templates_App'

urlpatterns= [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
