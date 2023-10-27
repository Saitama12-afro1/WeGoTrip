from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name="products"),
    path('create_order/', views.OrderView.as_view(), name="order"),
    path('create_payment', views.PaymentView.as_view(), name="payment"),
]