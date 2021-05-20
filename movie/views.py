from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie, MovieLinks


class  MovieList(ListView): 
    paginate_by = 1
    model = Movie
    # template_name = 'movie_list.html'

class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        return context
    

    # template_name ='movie_detail.html'

class MovieCategory(ListView):
    model = Movie
    # template_name 

    def get_queryset(self):
        self.category_id = self.kwargs['pk']
        movies = Movie.objects.filter(category = self.category_id)
        return movies
    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category_id
        return context













