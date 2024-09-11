from django.contrib import admin

# Register your models here.

from .models import Author,Book,BookInstance,Language,Genre

#task2
class BookInline(admin.StackedInline):
    model = Book



# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines=[BookInline]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance



# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') 
    #Unfortunately we can't directly specify the genre field in list_display because it is a ManyToManyField
    inlines = [BooksInstanceInline]  #book instance model also comes in the same page in book model itself



# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'status', 'borrower', 'due_back',]
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# admin.site.register(Book)
admin.site.register(Author,AuthorAdmin)

# admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)

