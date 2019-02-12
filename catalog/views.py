from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic
#from django.http import Http404


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_books_word = Book.objects.filter(title__exact='Ведьмак').count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request, 'index.html',
        context={'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors,
                 'num_genre': num_genre,
                 'num_books_word': num_books_word,
                 'num_visits': num_visits,}
    )


def book_l(request):
    book_list = Book.objects.order_by('title')
    context = {'book_list': book_list,}
    return render(request, 'book_l.html', context)


def author_l(request):
    author_list = Author.objects.order_by('first_name')
    context = {'author_list':author_list,}
    return render(request, 'author_l.html', context)

class BookDetailView(generic.DetailView):
    model = Book

#class AuthorListView(generic.ListView):
#    model = Author

#class AuthorDetailView(generic.DetailView):
#    model = Author

