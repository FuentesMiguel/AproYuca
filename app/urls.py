from django.urls import path
from app.views import AboutView

urlpatterns = [
    path('about/', AboutView.as_view()),
]