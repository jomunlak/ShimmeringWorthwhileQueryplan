from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.paginator import Paginator
from movies.models import Movie
from reviews.models import Review

class MoviesView(ListView):

    model = Movie
    paginate_by = 15
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Movies"
        return context


class MovieDetail(DetailView):
  model = Movie
  context_object_name = 'movie'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    movie = Movie.objects.get(pk=self.kwargs.get("pk"))
    print(movie.pk)

    reviews = Review.objects.filter(movie=movie)
    
    paginator = Paginator(reviews, 5)
    requested_page = int(self.request.GET.get("page", 1))
    
    page = paginator.get_page(requested_page)
    
    print(requested_page, page)
    context["page_obj"] = page
    return context  

class CreateMovie(CreateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )


class UpdateMovie(UpdateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )
