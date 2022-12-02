from django.urls import path

from apis import FoodApi



app_name = "Canteen"

urlpatterns = [
    path('foods/', FoodApi.as_view()),
]