from .models import CarMake, CarModel


def initiate():
    """
    Populate the database with sample CarMake and CarModel data.
    This function is called automatically when get_cars is accessed and the database is empty.
    """
    # Sample CarMake data
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]
    
    # Create CarMake instances
    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
            )
        )
    
    # Sample CarModel data - 3 models for each make
    car_model_data = [
        # NISSAN models
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer_id": 1},
        
        # Mercedes models
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 2},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 2},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer_id": 2},
        
        # Audi models
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 3},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 3},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer_id": 3},
        
        # Kia models
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 4},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 4},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "dealer_id": 4},
        
        # Toyota models
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 5},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 5},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4], "dealer_id": 5},
    ]
    
    # Create CarModel instances
    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            dealer_id=data['dealer_id']
        )
    
    print("Database populated with sample car data successfully!")