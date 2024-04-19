from django.http import JsonResponse
from django.shortcuts import render
from .mlp import SimpleMLP
import torch

def index(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        model = SimpleMLP()
        model.eval()
        test_data = torch.randn(1, 10)
        with torch.no_grad():
            output = model(test_data)
        return JsonResponse({'output': output.numpy().tolist()})
    return render(request, 'twentyquestionsgen/index.html')
