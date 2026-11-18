from django.urls import path
from . import views
urlpatterns=[
    path('',views.add_crackers,name="crack"),
    path('home/',views.home,name="home")
    
]