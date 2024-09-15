from django.urls import path
from .views import MenuView, SingleMenuView

urlpatterns = [
  path('menu/', MenuView.as_view()),
  path('menu/<int:pk>', SingleMenuView.as_view())
]
