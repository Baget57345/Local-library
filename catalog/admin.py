from django.contrib import admin
from .models import Author, Book, Genre, Language, BookInstance


#admin.site.register(Book)
admin.site.register(Language)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BooInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'due_back','borrower','id',)
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint','id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

