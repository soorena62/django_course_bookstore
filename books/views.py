from django.views import generic
from .models import Book
# from .forms import NewBookForm
# Create your views here:


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    # form_class = NewBookForm
    template_name = 'books/book_create.html'
    model = Book
    fields = ['title', 'author', 'description', 'price']
