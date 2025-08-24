from django.shortcuts import render

def index(request):
    return render(request, "carbium_reader/index.html")

def upload_book(request):
    return render(request, "carbium_reader/upload.html")

def book_detail(request, book_id):
    return render(request, "carbium_reader/book_detail.html", {"book_id": book_id})

def reader(request, book_id):
    return render(request, "carbium_reader/reader.html", {"book_id": book_id})
