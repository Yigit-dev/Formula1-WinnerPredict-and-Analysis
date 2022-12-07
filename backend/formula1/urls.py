from django.urls import path, include
from . import views as api_views

urlpatterns = [
    path('formula/', api_views.FormulaListCreateAPIView.as_view(), name='formula-list')
]

