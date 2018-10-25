from django.urls import path

from . import views

app_name='mysite'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:category_id>/results', views.category_filter, name='results'),
    ]
