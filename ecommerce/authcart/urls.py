from django.urls import path
from authcart import views

urlpatterns = [
     path('signin/',views.signin, name = "signin"),
     path('register/',views.register, name = "register"),
     path('handlelogout/',views.handlelogout, name = "handlelogout")
]
