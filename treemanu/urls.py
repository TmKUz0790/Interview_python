from django.urls import path
from .views import draw_menu_view

urlpatterns = [
    path('draw_menu/', draw_menu_view, name='draw_menu'),
]
