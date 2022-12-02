from django.urls import path

from apis import *



app_name = "Canteen"

urlpatterns = [
    path('foods/', FoodApi.as_view()),
    path('stores/', StoreApi.as_view()),
]