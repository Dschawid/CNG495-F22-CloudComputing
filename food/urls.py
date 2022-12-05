from django.urls import path, re_path

from apis import *



app_name = "Canteen"

urlpatterns = [
    re_path(r"foods/$", FoodApi.as_view()),
    re_path(r"drinks/$", DrinkApi.as_view()),
    re_path(r"stores/$", StoreApi.as_view()),
    re_path(r"orders/$", OrderApi.as_view()),
    re_path(r"orders/(?P<order_id>\d+)/$", OrderDetailApi.as_view()),
]