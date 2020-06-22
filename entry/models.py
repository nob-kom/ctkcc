from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
TOWER_CHOICES = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C')
)

class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField()

class User(models.Model):
    tower = models.IntegerField(choices=TOWER_CHOICES)
    room_number = models.IntegerField()
    name = models.CharField(max_length=30)
    email_1 = models.EmailField(null=True, blank=True, unique=True)
    email_2 = models.EmailField(null=True, blank=True, unique=True)
    tel_number_regex = RegexValidator(regex=r'^[0-9]+$', message = ("Tel Number must be entered in the format: '09012345678'. Up to 15 digits allowed."))
    tel_1 = models.CharField(null=True, blank=True, validators=[tel_number_regex], max_length=15, verbose_name='電話番号1')
    tel_2 = models.CharField(null=True, blank=True, validators=[tel_number_regex], max_length=15, verbose_name='電話番号2')
    admission_date = models.DateField()
    secession_date = models.DateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
