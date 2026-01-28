from django.urls import path
from .views import HairChatbotView

urlpatterns = [
    path('hair-chatbot/', HairChatbotView.as_view()),
]
