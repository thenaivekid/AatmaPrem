from django.urls import path 
from . import views

urlpatterns = [ 
    path('',views.index,name='index'),
    path('add_item',views.add_item,name='add_item'),
    path('create_post',views.create_post,name='create_post'),
    path('completed',views.completed,name='completed'),
    path('analyzingPeople',views.analyzingPeople,name='analyzingPeople'),
    path('add_analysis',views.add_analysis,name='add_analysis'),
]