from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # def __str__(self):
    #     return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    AVABILITY = (
        ('in stock', 'in stock'),
        ('to order','to order'),
    )

    BODYSTYLE = (
        ('sedan', 'sedan'),
        ('coupe','coupe'),
        ('convertible','convertible'),
        ('hatchback','hatchback'),
        ('SUV','SUV'),
        ('VAN','VAN'),
        ('combi','combi'),
        ('crossover','crossover'),
    )

    CAR_COLOR = (
        ('red', 'red'),
        ('white','white'),
        ('black','black'),
        ('yellow','yellow'),
        ('green','green'),
        ('pink','pink'),
        ('blue','blue'),
        ('orange','orange'),
    )

    FUEL = (
        ('diesel', 'diesel'),
        ('petrol','petrol'),
        ('LPG','LPG'),
        ('EV','EV'),
    )
    NAME_BRAND = (
        ('Volkswagen', 'Volkswagen'),
    )
    NAME_MODEL = (
        ('Passat', 'Passat'),
        ('Scirocco','Scirocco'),
        ('Golf','Golf'),
        ('Eos','Eos'),
        ('Tuareg','Tuareg'),
        ('Golf Sportsvan','Golf Sportsvan'),
        ('Arteon','Arteon'),
        ('Tiguan','Tiguan'),
    )

    name = models.CharField(max_length=200, null=True, choices=NAME_BRAND)
    name_model = models.CharField(max_length=200, null=True, choices=NAME_MODEL)
    engine_fuel = models.CharField(max_length=200, null = True, choices=FUEL)
    car_color = models.CharField(max_length=200, null = True, choices=CAR_COLOR)
    body_style = models.CharField(max_length=200, null = True, choices = BODYSTYLE)
    price = models.PositiveIntegerField(null=True)
    avability = models.CharField(max_length=200, null=True, choices = AVABILITY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        # lista = [self.name, self.name_model, self.engine_fuel]
        # return f'{self.name} {self.name_model}'
        return self.name + ' ' + self.name_model + ' ' + self.engine_fuel + ' ' + self.car_color + ' ' + self.body_style


class Order(models.Model):
    STATUS = (
        ('reserved', 'reserved'),
        ('available', 'available'),
        ('sold', 'sold'),
    )
    client = models.ForeignKey(Client, null = True, blank= True, on_delete = models.SET_NULL)
    product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null = True)
    status = models.CharField(max_length=200, null= True, choices = STATUS)

    def __str__(self):
        return self.product.name
