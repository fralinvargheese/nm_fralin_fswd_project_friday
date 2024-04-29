from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index.html',views.home,name='index'),
    path('car.html',views.car,name='car'),
    path('contact.html',views.contact,name='contact'),
    path('about.html',views.about,name='about'),
    path('login.html',views.handlelogin,name='handlelogin'),
    path('logout.html',views.handlelogout,name='handlelogout'),
    path('signup.html',views.handlesignup,name='handlesignup'),
    path('carindex1.html',views.carindex1,name='carindex1'),
    path('carindex2.html',views.carindex2,name='carindex2'),
    path('carindex3.html',views.carindex3,name='carindex3'),
    path('carindex4.html',views.carindex4,name='carindex4'),
    path('carindex5.html',views.carindex5,name='carindex5'),
    path('carindex6.html',views.carindex6,name='carindex6'),
    path('reviews.html',views.reviews,name='reviews'),
    path('service.html',views.service,name='service'),


    
]