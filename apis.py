from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import *
from serializers import FoodSerializer


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
