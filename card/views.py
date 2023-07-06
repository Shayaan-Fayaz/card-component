from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Member
# Create your views here.

class CardPageView(TemplateView):
    template_name = "card/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_members = Member.objects.all()
        context["team_members"] = team_members
        return context