from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.paginator import Paginator
from books.models import Book
from reviews.models import Review


class BooksView(ListView):
  
  model = Book
  paginate_by = 15
  paginate_orphans = 5
  ordering = "-created_at"
  context_object_name = "books"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = "All Books"
    return context


class BookDetail(DetailView):
  model = Book
  context_object_name = 'book'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    book = Book.objects.get(pk=self.kwargs.get("pk"))
    reviews = Review.objects.filter(book=book)
    # self.request에서 page를 받아서 

    paginator = Paginator(reviews, 5)
    requested_page = int(self.request.GET.get("page", 1))
    
    page = paginator.get_page(requested_page)
    
    print(requested_page, page)
    context["page_obj"] = page
    
    return context
    


class CreateBook(CreateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )


class UpdateBook(UpdateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )