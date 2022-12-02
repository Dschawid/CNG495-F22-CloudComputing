from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name="username", max_length=32, unique=True, null=True)
    email = models.EmailField(verbose_name="email", unique=True, null=True)
    first_name = models.CharField(verbose_name="first", max_length=30, blank=True)
    last_name = models.CharField(verbose_name="last", max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name="date", auto_now_add=True)
    is_active = models.BooleanField(verbose_name="active", default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    pplink = models.CharField("pplink", max_length=500)
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name="user"
        verbose_name_plural="users"


class Store(models.Model):
    name = models.CharField(verbose_name="name", max_length=30, blank=True)
    location = models.CharField(verbose_name="location", max_length=300, blank=True)
    owner = models.ForeignKey(User, verbose_name="owner", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Food(models.Model):
    CATEGORY_CHOICES = (
            ("Main Dishes", "Main Dishes"),
            ("Wraps", "Wraps"),
            ("Pastas", "Pastas"),
            ("Meat", "Meat"),
            ("Vegetarian", "Vegetarian"),
            ("Salads", "Salads"),
        )

    name = models.CharField(verbose_name="name", max_length=30, blank=True)
    price = models.DecimalField(verbose_name="price", max_digits=10, decimal_places=2)
    size = models.CharField(verbose_name="size", max_length=50, null=True, blank=True)
    is_available = models.BooleanField(verbose_name="is_available", default=True)
    duration = models.IntegerField(verbose_name="duration", default=0)
    store = models.ForeignKey(Store, verbose_name="store", on_delete=models.CASCADE)
    category = models.CharField(verbose_name="category", choices=CATEGORY_CHOICES, max_length=50)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(verbose_name="name", max_length=30, blank=True)
    price = models.DecimalField(verbose_name="price", max_digits=10, decimal_places=2)
    is_available = models.BooleanField(verbose_name="is_available", default=False)
    volume = models.DecimalField(verbose_name="volume", max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, verbose_name="store", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (
            ("Completed", "Completed"),
            ("Preparing", "Preparing"),
            ("Cancelled", "Cancelled"),
        )

    owner = models.ForeignKey(User, verbose_name="owner", on_delete=models.CASCADE)
    store = models.ForeignKey(Store, verbose_name="store", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name", max_length=30, blank=True)
    food = models.ManyToManyField(Food, verbose_name="food", related_name="order_foods")
    drink = models.ManyToManyField(Drink, verbose_name="drink", related_name="order_drinks")
    price = models.DecimalField("price", max_digits=10, decimal_places=2)
    estimated_duration = models.IntegerField("duration", default=0)
    created_at = models.DateTimeField("created_at", auto_now=True)
    status = models.CharField("status", choices=STATUS_CHOICES, max_length=50)
    notes = models.CharField(verbose_name="notes", max_length=500, null=True)

    def __str__(self):
        return self.name