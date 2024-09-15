from django.urls import path
from .views import MenuView, SingleMenuView, BookingView

urlpatterns = [
  path('menu/', MenuView.as_view()),
  path('menu/<int:pk>', SingleMenuView.as_view()),
  path('booking/', BookingView.as_view()),
]
