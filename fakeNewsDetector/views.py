from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     return render(request, 'fakeNewsDetector/home.html', {'title' : 'Home'})

class HomeView(TemplateView):
    template_name = "fakeNewsDetector/home.html"
