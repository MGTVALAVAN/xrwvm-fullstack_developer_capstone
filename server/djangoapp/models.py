# Imports for Django models
from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# CarMake Model - Represents a car manufacturer
class CarMake(models.Model):
    """
    CarMake model to store information about car manufacturers
    """
    # Name of the car make (e.g., Toyota, Mercedes, Audi)
    name = models.CharField(max_length=100)
    
    # Description of the car make
    description = models.TextField()
    
    # String representation of the model
    def __str__(self):
        """Return the name of the car make"""
        return self.name


# CarModel Model - Represents a specific car model
class CarModel(models.Model):
    """
    CarModel model to store information about specific car models
    """
    # Car type choices - limited options for the 'type' field
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
    ]
    
    # Many-to-One relationship with CarMake
    # One CarMake can have many CarModels
    # on_delete=models.CASCADE means if a CarMake is deleted, 
    # all its CarModels will also be deleted
    car_make = models.ForeignKey(
        CarMake, 
        on_delete=models.CASCADE
    )
    
    # Dealer ID - reference to the dealer (stored as integer)
    dealer_id = models.IntegerField()
    
    # Name of the car model (e.g., Corolla, Camry, A4)
    name = models.CharField(max_length=100)
    
    # Type of car - must be one of the choices defined in CAR_TYPES
    type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default='Sedan'
    )
    
    # Year of manufacture - must be between 2015 and 2023
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    
    # String representation of the model
    def __str__(self):
        """Return the car make and model name"""
        return f"{self.car_make.name} {self.name}"
