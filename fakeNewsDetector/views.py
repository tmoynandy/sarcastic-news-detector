from django.shortcuts import render
from django.views.generic import TemplateView
from .webscraper import webscraper


# Create your views here.
# def home(request):
#     return render(request, 'fakeNewsDetector/home.html', {'title' : 'Home'})

class HomeView(TemplateView):
    template_name = "fakeNewsDetector/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     return context

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        error = ''
        if not q:
            error = "error message"
        else:
            print(q)
            print(type(q))
            # print(webscraper)
            # print(dir(webscraper))
            # print(webscraper.headlinescraper)
            #print(webscraper.headlinescraper('aaaaa'))
            print(webscraper.headlinescraper(q))
            headline = webscraper.headlinescraper(q)
            
        return render(request, self.template_name, {
            'error': error,
            'headline': headline,
        })
