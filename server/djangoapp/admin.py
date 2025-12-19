from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class - allows editing CarModels inline when editing a CarMake
class CarModelInline(admin.TabularInline):
    """
    Inline admin interface for CarModel.
    This allows you to add/edit CarModels directly from the CarMake admin page.
    """
    model = CarModel
    extra = 1  # Number of empty forms to display for adding new CarModels


# CarModelAdmin class - admin interface for CarModel
class CarModelAdmin(admin.ModelAdmin):
    """
    Admin interface for CarModel.
    Customizes how CarModel is displayed in the admin panel.
    """
    # Fields to display in the list view
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    
    # Fields that can be used to filter the list
    list_filter = ['car_make', 'type', 'year']
    
    # Fields that can be searched
    search_fields = ['name', 'car_make__name']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    """
    Admin interface for CarMake.
    Includes inline editing of related CarModels.
    """
    # Fields to display in the list view
    list_display = ['name', 'description']
    
    # Fields that can be searched
    search_fields = ['name']
    
    # Include CarModelInline to show related car models
    inlines = [CarModelInline]


# Register models with their admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)