from django.shortcuts import render, redirect
from django.views.generic import CreateView
from reviews.forms import ReviewCreateForm
from django.urls import reverse
from books.models import Book
from movies.models import Movie
from users.models import User
from reviews.models import Review
# Create your views here.

# createreivew, deletereview view.

def review_delete(request):
  review = Review.objects.get(pk=request.GET.get("review"))
  book_pk = request.GET.get("book")
  movie_pk = request.GET.get("movie")
  review.delete()
  if book_pk:
    return redirect("books:book", pk=book_pk)
  else:
    return redirect("movies:movie", pk=movie_pk)

class ReviewCreateView(CreateView):
  """ Review Create View Definition """

  template_name = "reviews/create_review.html"
  success_url = "/"
  form_class = ReviewCreateForm


  def form_valid(self, form):
    user = User.objects.get(id=self.request.user.id)
    book_pk = self.request.GET.get("book")
    movie_pk = self.request.GET.get("movie")
    book= None
    movie = None
    if book_pk:
      book = Book.objects.get(pk=book_pk)
    elif movie_pk:
      movie = Movie.objects.get(pk=movie_pk)
    
    if book or movie:
      kwargs = {"user":user,"book":book, "movie":movie,}
      form.save(kwargs=kwargs)
      return redirect(reverse("core:home"))
    else:
      return redirect(reverse("core:home")) 

  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    book = self.request.GET.get("book")
    movie = self.request.GET.get("movie")
    context["page_title"] = "Review"

    

    
    if not(book or movie):
        context["no_target"] = True

    return context
