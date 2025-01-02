from django.urls import path
from . import views

urlpatterns = [
    # path('', views.app, name='app'),

    path('login/', views.log_user, name='login'),
    path('register/', views.createUser, name='register'),
    path('app/', views.app, name='app'),
    path('logout/', views.logout_user, name='logout'),

    path('add/', views.dataForm, name='datain'),
    path('<str:nic>', views.view_child, name='child'),
    path('search/', views.item_search, name='search'),
    path('<int:pk>/update/', views.item_update, name='update'),
    path('<int:pk>/delete/', views.item_delete, name='delete'),
]