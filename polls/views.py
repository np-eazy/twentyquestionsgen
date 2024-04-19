from django.shortcuts import render
from django.http import HttpResponse
from .mlp import SimpleMLP
import torch

def index(request):
    model = SimpleMLP()
    model.eval()  # Set the model to evaluation mode
    test_data = torch.randn(1, 10)  # Generate some random test data
    with torch.no_grad():  # Ensure gradients aren't computed for inference
        output = model(test_data)
    return HttpResponse(f"MLP Output: {output.numpy()}")

    # return HttpResponse("Hello, world. You're at the polls index.")

