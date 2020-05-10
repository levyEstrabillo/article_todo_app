from django.urls import path
from . import views

app_name='articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('<id>', views.article_detail, name='detail'),
    path('delete/<int:id>', views.article_delete, name='delete'),   
    #path('edit/<int:id>', views.article_edit, name='edit'),   
]