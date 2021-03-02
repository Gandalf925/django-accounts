from django.urls import path
from .views import LearningListView

urlpatterns = [
    path("", LearningListView.as_view(), name="learning_list"),
    
]
