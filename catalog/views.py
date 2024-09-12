from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_geners=Genre.objects.all().count()
    num_BooksContains_the = Book.objects.filter(title__icontains = 'the').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_geners':num_geners,
        'num_BooksContains_the':num_BooksContains_the,
        'num_visits': num_visits,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2 #it displays the 2 data only in the page


    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='s')[:5] # Get 5 books containing the title war
    
    # def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        # context = super(BookListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        # context['some_data'] = 'This is just some data'
        # return context

from django.shortcuts import get_object_or_404

class BookDetailView(generic.DetailView):
    model=Book

    #this can use when we are not using generic view because automatically it takes 
    # def book_detail_view(request, primary_key):
    #     book = get_object_or_404(Book, pk=primary_key)
    #     return render(request, 'catalog/book_detail.html', context={'book': book})

class AuthorListView(generic.ListView):
    model=Author
    paginate_by = 2 #it displays the 2 data only in the page

class AuthorDetailView(generic.DetailView):
    model=Author
    
