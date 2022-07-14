from apps.users import views
from django.urls import path


urlpatterns = [
    path('', views.home),
    path('api/users', views.UserView.as_view()),
    path('api/users/<int:pk>', views.UserDetailsView.as_view()),
    path('api/users/', views.UserDetailsView.as_view()),
]
