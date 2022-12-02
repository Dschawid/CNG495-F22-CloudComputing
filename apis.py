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