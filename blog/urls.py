from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
     path('', views.post_list, name='post_list'),
     path('like/',views.like,name='like'),
     path('save-comment',views.save_comment,name='save_comment'),
     path('contact/',views.contact,name='contact'),
     path('<slug:category_slug>', views.post_list, name='post_by_category'),
     path('<int:id>/', views.post_detail, name='post_detail'),

 

]