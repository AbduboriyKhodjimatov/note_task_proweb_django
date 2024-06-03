from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_, name='logout'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update/', views.UpdateArticle.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteArticle.as_view(), name='delete'),
    path('search/', views.SearchResultView.as_view(), name='search')
    
]