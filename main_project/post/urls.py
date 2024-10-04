from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('create/',views.post_create,name='create'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),  
    path('comment/<int:post_id>', views.comment, name='comment'),
    path('update_post/<int:id>/',views.update_post,name='update_post'),  
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'), 
] 