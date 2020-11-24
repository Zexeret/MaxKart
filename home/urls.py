from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home),
    path('card/<int:myid>', views.card),
    path('order', views.order),
    path('updateorder', views.updateorder),
    path('deleterow', views.deleterow),
    path('handleSignup',views.handleSignup),
    path('signup',views.signup),
    path('login',views.Login),
    path('handleLogin',views.handleLogin),
    path('logout', views.handelLogout),
    path('bookOrder',views.bookOrder)

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)