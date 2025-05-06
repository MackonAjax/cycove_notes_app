from django.urls import path
from . import views

app_name = 'notes1'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add, name='add'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<int:note_id>/delete', views.delete, name='delete'),
]