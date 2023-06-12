from django.urls import path
from .views import bog_list, blog_detail


urlpatterns = [
    path('blogs/', bog_list, name='home'),
    path('', bog_list, name='home1'),
    path('blogs/<int:pk>/', blog_detail, name='details_blog')

]

