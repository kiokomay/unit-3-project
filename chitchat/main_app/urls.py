from django.urls import path
from . import views

urlpatterns = [
  path('', views.login, name='login'),
  path('signup/', views.signup, name='signup'),
  path('home/', views.home, name='home'),
  path('profile/', views.profile, name='profile'),
  path('post/', views.post, name='post'),
  path('edit-post/', views.edit_post, name='edit_post'),
  path('post-confirm-delete/', views.post_confirm_delete, name='post_confirm_delete'),
  path('comment-confirm-delete/', views.comment_confirm_delete, name='comment_confirm_delete'),
]

# path('/', views., name=''),