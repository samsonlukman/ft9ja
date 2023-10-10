from django.urls import path

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('simulate_profit_or_loss/', views.simulate_profit_or_loss_api, name='simulate_profit_or_loss'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
    
]