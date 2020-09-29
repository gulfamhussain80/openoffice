from django.urls import path

from index import views

urlpatterns = [
        path('',views.userView,name='index'),
        path('home/',views.home,name='home'),
]
