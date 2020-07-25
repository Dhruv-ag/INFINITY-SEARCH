from django.views.generic import TemplateView, ListView

from .models import Post
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):

    template_name = 'search_result.html'
    def get_queryset(self):
        query=self.request.GET.get('q')

        # object_list=Post.objects.filter(title__istartswith=query,cast__istartswith=query2)
        object_list=Post.objects.filter(title__istartswith=query)
        return object_list
