from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FormulaDetailSerializer
from .models import FormulaDetail
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .scraper import get_data_detail

class FormulaListCreateAPIView(APIView):

    def get_object(self, pk):
        formula_instance = get_object_or404(FormulaDetail, pk=pk)
        return formula_instance

    def get(self, request):
        formula = FormulaDetail.objects.all()
        serializer = FormulaDetailSerializer(formula)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormulaDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.http import HttpResponse
# from rest_framework.views import APIView
# from .models import FormulaDetail
# from .serializers import FormulaDetailSerializer
# from bs4 import BeautifulSoup
# from rest_framework.response import Response
# from .scraper import get_data_detail

# import requests 
# import json

# def index(request):
#     return HttpResponse("Success")

# class FormulaListCreateAPIView(APIView):

#     def get(self, request):
#         formula = FormulaDetail.objects.all()
#         serializer = FormulaDetailSerializer(formula)

#         return Response(serializer.data)


