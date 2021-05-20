from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory

urlpatterns = [
    path('', MovieList.as_view(), name = 'movie_list'),
    path('category/<int:pk>', MovieCategory.as_view(), name = 'movie_category'),
    path('<int:pk>', MovieDetail.as_view(), name = 'movie_detail'),

]
