from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.auth import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='myapp/signin.html'), name='login'),
    path('', include('myapp.urls')),
    path('logout/', authentication_views.LogoutView.as_view(), name='logout'),

]
