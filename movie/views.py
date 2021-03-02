from django.shortcuts import render, redirect
from .models import MovieModel
from django.views.generic import ListView

# Create your views here.
class LearningListView(ListView):
    model = MovieModel
    template_name = "learning_list.html"

    def get(self, request, **kwargs):
        # アクティブユーザーでなければログインページ
        if not request.user.is_active:
            return redirect('/accounts/login/')
        return super().get(request)