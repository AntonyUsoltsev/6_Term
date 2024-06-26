from torch import nn


class ConvBlockA(nn.Module):
    def __init__(self, in_channels, out_channels, pool_ker_size=2, pool_stride=2,
                 conv_ker_size=3, conv_stride=1, padding=1):
        super(ConvBlockA, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=conv_ker_size, stride=conv_stride, padding=padding)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=pool_ker_size, stride=pool_stride)

    def forward(self, x):
        x = self.conv(x)
        x = self.relu(x)
        x = self.pool(x)
        return x


class ConvBlockB(nn.Module):
    def __init__(self, in_channels, out_channels, pool_ker_size=2, pool_stride=2,
                 conv_ker_size=3, conv_stride=1, padding=1):
        super(ConvBlockB, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels // 2, kernel_size=conv_ker_size, stride=conv_stride, padding=padding)
        self.relu1 = nn.ReLU()
        self.conv2 = nn.Conv2d(out_channels // 2, out_channels, kernel_size=conv_ker_size, stride=conv_stride, padding=padding)
        self.relu2 = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=pool_ker_size, stride=pool_stride)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool(x)
        return x
