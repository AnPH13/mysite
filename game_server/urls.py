from django.urls import path
from .views.game_view import GameView

urlpatterns = [
    # path('', views.TestView.as_view({'get':'test'})),
    path('', GameView.as_view({'get':'get_all'})),
]   