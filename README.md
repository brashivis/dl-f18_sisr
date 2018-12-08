# Single-Image Super Resolution Using EDSR and SRGAN

## Structure

This repository has two main folders, edsr and srgan. 

The first, edsr, is based on EDSR (Enhanced Deep Super Resolution network), a Super Resolution model built with a ResNet-like architecture that utilizes successive convolutional layers and residual connections. EDSR was first presented in a paper by Lim et al. that can be found [here](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Lim_Enhanced_Deep_Residual_CVPR_2017_paper.pdf). The code in this folder is based off of a PyTorch implementation of the paper that can be found [here](https://github.com/thstkdgus35/EDSR-PyTorch). The original, official code repository for EDSR primarily uses Lua and can be found [here](https://github.com/LimBee/NTIRE2017). The model's primary code and structure can be found in the `edsr/src/loss/` folder and the `edsr/src/model/` folder (specifically `edsr/src/model/edsr.py` and `edsr/src/model/common.py`).

The second, srgan, is based on SRGAN (Super Resolution Generative Adversarial Network), a Super Resolution model built using a GAN architecture. SRGAN was first presented in a paper by Ledig et al. that can be found [here](https://arxiv.org/abs/1609.04802). The code in this folder is heavily based off of a TensorFlow implementation of SRGAN that can be found [here](https://github.com/tensorlayer/srgan). The model's primary code and structure can be found in `srgan/main.py` and `srgan/model.py`.


## Ablation Study

Entering either folder will display a modified version of the original README file for each project. For more information on our changes to the code of either model, please refer to these README's. The goal of this project was to perform an ablation study on both models. We implemented and tested the following:

* Training Lim et al.'s SRGAN model using MSE in order to provide a direct comparison to the state-of-the-art EDSR model
* Using interpolation rather than pixel shuffle in EDSR to upsample the final output
* Testing images with noise, including salt-and-pepper, speckle, and blurring, in order to compare how the models perform under different conditions 
* Using the perceptual loss function suggested in Johnson et al. [here](https://arxiv.org/abs/1603.08155) instead of MSE to train EDSR
* Qualitatively (rather than quantitatively) comparing the images produced using perceptual loss against those produced by the baseline (MSE) EDSR model


## Trained Models

For instructions on how to train each model, please refer to each project's respective README file. Our own pre-trained models are not available on GitHub due to their size. 
