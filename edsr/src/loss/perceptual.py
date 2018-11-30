from model import common
from functools import reduce
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as models

#usage in bash file: --loss 1*perceptual-start-end
class Perceptual(nn.Module):
    def __init__(self, start_conv_index, end_conv_index, rgb_range=1):
        super(Perceptual, self).__init__()
        vgg_features = models.vgg19(pretrained=True).features
        self.vgg_modules = list(vgg_features.modules())
        self.vgg_weights = []
        activation_layers = set(1,3,6,8,11,13,15,17,20,22,24,26,29,31,33,35) #indices of VGG19 ReLU layers
        for i in range(len(self.vgg_modules)):
            #if this is before or after the layers that will be weighted for perceptual loss
            if (i < start_conv_index) or (i > end_conv_index):
                self.vgg_weights.append(0)
            #elif this is not after the activation of a convolutional layer
            elif i not in activation_layers:
                self.vgg_weights.append(0)
            else:
                self.vgg_weights.append(1)

        vgg_mean = (0.485, 0.456, 0.406)
        vgg_std = (0.229 * rgb_range, 0.224 * rgb_range, 0.225 * rgb_range)
        self.sub_mean = common.MeanShift(rgb_range, vgg_mean, vgg_std)

    def forward(self, sr, hr):
        total_loss = float(0)
        sr = self.sub_mean(sr)
        hr = self.sub_mean(hr)

        #run through the VGG network and sum the MSE loss at each layer
        with torch.no_grad():
            for i,layer in enumerate(self.vgg_modules):
                sr = layer(sr)
                hr = layer(hr.detach())
                #add to total loss the MSE at this layer of VGG19 multiplied by a normalization term (1/batch_size*channels*height*width)
                total_loss += F.mse_loss(sr, hr)*self.vgg_weights[i]*reduce(lambda x,y: x*y, sr.shape)

        return total_loss