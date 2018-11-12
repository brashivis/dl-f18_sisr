# Single-Image Super Resolution

This repository has two main folders, srgan and edsr. 

The first, srgan, is based on [SRGAN](https://github.com/tensorlayer/srgan), a Super Resolution model built using a GAN (Generative Adversarial Network). The paper this model is based on can be found [here](https://arxiv.org/abs/1609.04802).

The second, edsr, is based on [EDSR](https://github.com/thstkdgus35/EDSR-PyTorch), another Super Resolution model. This model is based on SRResNet. The paper on which this model is based can be found [here](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w12/papers/Lim_Enhanced_Deep_Residual_CVPR_2017_paper.pdf). The code we are using here (and the link above) is the PyTorch implmentation of the paper. The original code repository, which mainly uses Lua, can be found [here](https://github.com/LimBee/NTIRE2017).

Entering either folder will display the original README file for each project. The goal of this project is to perform an ablation study and test whether various hypotheses improve on the results achieved by these models. We plan on investigating at least the following:

* Using upscaling methods other than pixel shufﬂe
* Using a higher volume of data to train
* Tuning convolutional layer parameters and adding more convolutional layers
* Integrating noise, such as blurring, in pre-processing
* Using speciﬁc types of images, such as landscapes, to train a specialized model
* Using the perceptual loss function as suggested in Johnson et al. instead of PSNR

## Trained Models

We have run the training scripts for both these models. Our pre-trained models are not available on GitHub right now due to their size.

For instructions on how to train each model, please read their respective README files.