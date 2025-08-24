from django.urls import path
from . import views

app_name = "carbium_reader"

urlpatterns = [
    path("", views.index, name="index"),            # homepage / library
    path("upload/", views.upload_book, name="upload"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("reader/<int:book_id>/", views.reader, name="reader"),
]
