from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Book
from .form import BookForm

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)

# version 1
# def book_detail_view(request, book_id, *args, **kwargs):
#     try:
#         obj = Book.objects.get(id=book_id)
#     except:
#         raise Http404
#     return HttpResponse(f'<h1>Book: {obj.name} author: {obj.author} </h1>')

# version 2
def book_detail_view(request, book_id, *args, **kwargs):
    data = {
        "id": book_id
    }
    status = 200
    try:
        obj = Book.objects.get(id=book_id)
        data['name']=obj.name
        data['author']=obj.author
        data['description'] = obj.description

    except:
        data['message'] = 'Not Found'
        status = 404
    return JsonResponse(data, status=status)

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def book_create_view(request, *args, **kwargs):
    form = BookForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = BookForm()
    return render(request, 'components/form.html', context={'form': form})

def books_list(request, *args, **kwargs):
    blist = Book.objects.all()
    books = [{
        'id': x.id,
        'name': x.name,
        'author': x.author,
        'description': x.description
    } for x in blist]
    data = {
        'response': books
    }
    return JsonResponse(data)

