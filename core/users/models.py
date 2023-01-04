from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField("el nombre de la persona",max_length=30)
    last_name = models.CharField("el apellido de la persona",max_length=30)
    cars = models.ManyToManyField("Car", verbose_name="los carros de la persona")

STATUS_CHOICES = (
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Approved')
)

class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Car(models.Model):
    brand = models.CharField(max_length=50, primary_key=True)
