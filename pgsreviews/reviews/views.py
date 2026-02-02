from django.shortcuts import render
from django.http import JsonResponse

def greet(request):
    return JsonResponse({"message": "hello"})

