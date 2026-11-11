from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("business/new/", views.business_create, name="business_create"),
    path("business/<int:business_id>/", views.dashboard, name="dashboard"),
    path("business/<int:business_id>/transactions/", views.transaction_list, name="transaction_list"),
    path("business/<int:business_id>/transactions/new/", views.transaction_create, name="transaction_create"),
    path("language/<str:language>/", views.language_switch, name="language_switch"),
]
