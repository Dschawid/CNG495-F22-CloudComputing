from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import *
from serializers import *


class FoodApi(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response({"foods": serializer.data})

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({"data": serializer.errors}, status=400)


class StoreApi(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({"stores": serializer.data})

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({"data": serializer.errors}, status=400)


class DrinkApi(APIView):
    def get(self, request):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response({"drinks": serializer.data})

    def post(self, request):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({"data": serializer.errors}, status=400)


class OrderApi(APIView):
    def get(self, request):
        store_id = request.GET.get("store_id")
        if store_id:
            orders = Order.objects.filter(store=store_id)
        else:
            orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({"orders": serializer.data})
    

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response({"data": serializer.errors}, status=400)



class OrderDetailApi(APIView):
    def patch(self, request, order_id):
        try:
            order = Order.objects.get(pk=order_id)
            serializer = OrderSerializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"order": serializer.data})
            return Response({"error": serializer.errors})
        except Order.DoesNotExist:
            return Response({"error": "Order does not exist"})
