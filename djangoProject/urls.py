from bakecake import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    ]
