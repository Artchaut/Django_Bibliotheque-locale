from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

# Register the admin class with the associated model
#admin.site.register(Author, AuthorAdmin)
# Or
# Register the Admin class using the decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
   fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), 'img_preview']
   readonly_fields = ['img_preview']


# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   list_display = ('title', 'author', 'display_genre')
   readonly_fields = ['img_preview']



# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
