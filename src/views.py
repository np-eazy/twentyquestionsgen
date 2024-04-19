from django.http import JsonResponse
from django.shortcuts import render
from twentyquestionsgen.mlp import SimpleMLP
import torch

def index(request):
    return render(request, 'index.html')
