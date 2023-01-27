from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>/add_picture/', views.add_picture, name='add_picture'),
    path('dogs/<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:dog_id>/add_comment/', views.add_comment, name='add_comment'),
    path('dogs/<int:dog_id>/delete_comment/<int:comment_id>/',views.delete_comment, name='delete_comment'),
]
