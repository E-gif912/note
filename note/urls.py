from . import views
from django.urls import path

urlpatterns =[
    # path('', views.main, name="main"),
    path("", views.main, name="Landing page"),
    path('home/', views.home, name="Home page"),
    path("<int:post_id>/", views.detail, name="detail"),
    path("create/", views.create_note, name="create"),
    path('login/', views.login_user, name='login'),
    path('signup/', views.create_user, name='signup'),
    path("delete/<int:post_id>/", views.delete_note, name="delete"),
    path("edit/<int:post_id>/", views.edit_note, name="edit"),
    path("logout", views.logout_user, name="logout")
]

