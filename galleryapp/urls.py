
from django.urls import path
from . import views

urlpatterns = [

    path('', views.login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup', views.user_singup, name='signup'),

    path('index/', views.index, name='index'),
    # path('add/',views.add_new_gallery,name="add"),
]
