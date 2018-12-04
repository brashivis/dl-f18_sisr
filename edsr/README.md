## Enhanced Deep Super Resolution Network

This repository is based off of an official PyTorch implementation of the paper [EDSR](https://arxiv.org/abs/1707.02921) that can be found [here](https://github.com/thstkdgus35/EDSR-PyTorch). This PyTorch implementation is itself based off of an original Lua implementation, which can be found [here](https://github.com/LimBee/NTIRE2017). Our ablation study did not include large changes to the architecture of the network, so the bulk of the model's code remains the same (beyond fixing a few bugs to get it up and running) as in the official PyTorch implementation above. To implement the perceptual loss function from Johnson et al.'s [paper](https://arxiv.org/abs/1603.08155), we wrote the code in `src/loss/perceptual.py`. To implement an upsampling block that used interpolation rather than pixel shuffling (sub-pixel convolution based on the paper [here](https://arxiv.org/abs/1609.05158)), we wrote the AblationUpsampler class, which can be found in `src/model/common.py`. The model's primary code and structure can be found in the `edsr/src/loss/` folder and the `edsr/src/model/` folder (specifically `edsr/src/model/edsr.py` and `edsr/src/model/common.py`).


### Dependencies

* Python 3.6
* PyTorch >= 0.4.0
* numpy
* skimage
* imageio
* matplotlib
* tqdm
* cv2 >= 3.xx


### EDSR Architecture

We used PyTorch to implement the architecture from the paper ["Enhanced Deep Residual Networks for Single Image Super-Resolution"](https://arxiv.org/abs/1707.02921) as depicted here:

<div align="center">
	<img src="img/EDSR_arch.png" width="80%" height="10%"/>
</div>


### Preparing the Data

* Download the data and update the defaults for arguments in `src/option.py`.
	* In this experiment, we used images from [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/), a dataset that provides 800 high resolution images for training and 200 for testing as well as various downsampled versions of the same images. We used the bicubic downscaling x2 data (Track 1, downscaling x2 in the link above).
 	* Make sure to change the default path for the `--dir_data` argument in `src/option.py` so that it points to the correct dataset directory.
	* If you want to use your own images for training or validation, simply organize your data in the same way as DIV2K and set new default names (the name of your new dataset) for the `--data_train` and `--data_test` arguments.
* It is recommended that on the first training run, the `--ext sep_reset` argument be used in order to decode all **png** files and save them as binaries.
  * On future training runs, the `--ext sep` argument can be used to skip the decoding and use saved binaries instead.
  * If you have enough RAM (>= 32GB), you can use the `--ext bin` argument to pack all DIV2K images into one binary file.


### Training and Testing

* Common training and testing scripts are commented out in `src/demo.sh`. In order to train or test, uncomment the appropriate line and run

```bash
sh demo.sh   # Assuming you are in edsr/src
```

* Otherwise, look in `src/option.py` for all possible arguments and run

```bash
python main.py <your custom arguments>	# Assuming you are in edsr/src
```

* For each of our experiments, we trained from scratch used the following arguments (in addition to experiment-specific arguments, such as loss):

```bash
python main.py --model EDSR --epochs 200 --batch_size 16 --scale 2 --n_resblocks 32 --n_feats 256 --res_scale 0.1 --print_every 1 --reset
```

* To use one of Lim et al.'s pre-trained models for training or testing, use the argument `--pre_train download`, which will automatically download a model of your specifications (number of residual blocks, number of features, and scale) from the server
	* Specifically, a download of the EDSR model with our specifications (32 residual blocks, 256 features, and scale x2) can be found [here](https://cv.snu.ac.kr/research/EDSR/models/edsr_x2-0edfb8a3.pt)
* To test a model on your own images, place the desired images (either **png** or **jpeg**) in the `test` folder (`edsr/test/<your_image>`) and run the `src/demo.sh` file with the appropriate line uncommented (a line with the `--data_test` argument set). The resulting images will be saved in the `experiment/test/results` folder.


### References
* [1] [Enhanced Deep Residual Networks for Single Image Super-Resolution](https://arxiv.org/abs/1707.02921)
* [2] [Perceptual Losses for Real-Time Style Transfer and Super-Resolution](https://arxiv.org/abs/1603.08155)
* [3] [Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/abs/1609.05158)
