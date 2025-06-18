import torch
import torch.nn as nn
import torch.nn.functional as F

# Define the model architecture
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Load the trained model
net = Net()
net.load_state_dict(torch.load("tinyNet_trained.pth"))
net.eval()

# Dummy input
dummy_input = torch.randn(1, 3, 32, 32)

# Export ONNX model
torch.onnx.export(
    net,
    dummy_input,
    "C:/zkml/model.onnx",
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}},
    opset_version=13,
)

print("✅ ONNX model re-exported with dynamic axes and opset 13.")
