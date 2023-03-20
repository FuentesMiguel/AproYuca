from django.urls import path
from app.views import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='about'),
]