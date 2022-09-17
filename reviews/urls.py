from django.urls import path
from reviews.views import ReviewCreateView, review_delete

app_name="reviews"

urlpatterns = [
  path("new", ReviewCreateView.as_view(), name="create-review"),
  path("delete", review_delete, name="delete-review")
]
