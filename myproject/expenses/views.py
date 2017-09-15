# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Expenses
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, ExpensesSerializer
from django.http import HttpResponse, JsonResponse




@csrf_exempt
def apiregister(request):
    data = JSONParser().parse(request)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)





@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
@csrf_exempt
def day_expenses(request):
    try:
        expenses = Expenses.objects.filter(user=request.user)
    except Expenses.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExpensesSerializer(expenses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        #for data in lis:
        serializer = ExpensesSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, status=400)