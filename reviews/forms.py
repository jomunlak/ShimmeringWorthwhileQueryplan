from django import forms 
from django.db import models
from reviews.models import Review


class ReviewCreateForm(forms.ModelForm):
  
  class Meta:
    model = Review
    fields = ["text", "rating"]

    
  def clean_rating(self):
    rating = self.cleaned_data.get("rating")
    if rating< 0 or rating > 5:
      raise forms.ValidationError("Rating must be in 0 and 5")
    else:
      return rating




  def save(self, *args, **kwargs):
    review = super().save(commit=False)
    user = kwargs.get("kwargs").get("user")
    book = kwargs.get("kwargs").get("book")
    movie = kwargs.get("kwargs").get("movie")
    review.created_by = user
    review.book = book
    review.movie = movie

    review.save()
