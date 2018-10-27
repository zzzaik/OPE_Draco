from django.urls import path
from core.views import ListImagensView

urlpatterns = [
    path('getImagens/', ListImagensView.as_view(), name="imagens-all")
]