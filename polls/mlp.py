import torch
import torch.nn as nn

class SimpleMLP(nn.Module):
    def __init__(self):
        super(SimpleMLP, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(10, 5),  # Example input size of 10 and hidden layer size of 5
            nn.ReLU(),
            nn.Linear(5, 2)    # Output layer size of 2
        )

    def forward(self, x):
        return self.layers(x)
