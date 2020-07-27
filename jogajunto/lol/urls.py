from django.urls import path
from .import views
from .views import PlayerView, button

urlpatterns = [
    path('', views.home, name='home'),
    path('external/', views.external),
    path('lista-jogadores', PlayerView.as_view(), name='lista-jogadores'),
    # path('lista-jogadores/', views.button)
    path('atualizado/', views.button)
]
