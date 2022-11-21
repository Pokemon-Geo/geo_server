import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Net(nn.Module):
    def __init__(self):
        super().__init__()

        # 3 input image channel, 6 output channels, 5x5 square convolution

        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 29 * 29, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

PATH = './machine/test_3.pth'

transform = transforms.Compose([transforms.ToTensor(), transforms.Resize(128), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

net = Net()
net.load_state_dict(torch.load(PATH))

classes = ['footway', 'primary']

def predict_image(uuid, timestamp):

    img = Image.open('./upload/photos/' + uuid + '/' + timestamp + '.jpg')

    img = img.resize((256, 256), Image.Resampling.LANCZOS)

    #convert to tensor
    img = transform(img).float()
    img = img.unsqueeze(0)

    outputs = net(img)

    print(type(img))
    print(img.shape)

    index = outputs.argmax()

    return classes[index]    