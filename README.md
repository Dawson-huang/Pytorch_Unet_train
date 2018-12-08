# Pytorch_Unet_train
Pytorch implementation of the U-Net for cellular medical image segmentation

# Prediction
   You can easily test the output masks on your images via the CLI.

   To see all options: `python predict.py -h`

   To predict a single image and save it:

    python predict.py -i image.jpg -o output.jpg

   To predict a multiple images and show them without saving them:

    python predict.py -i image1.jpg image2.jpg --viz --no-save

   You can use the cpu-only version with `--cpu`.

   You can specify which model file to use with `--model checkpoints/CP21.pth`.
# Results
   Use the trained model to do segmentation on test images.<br>
   test image:
   
   ![Image text](https://github.com/Dawson-huang/Pytorch_Unet_train/blob/master/images/image.png)
   
   label image:
   
   ![Image text](https://github.com/Dawson-huang/Pytorch_Unet_train/blob/master/images/label.png)
   
   result image of model `CP21.pth`:
   
   ![Image text](https://github.com/Dawson-huang/Pytorch_Unet_train/blob/master/images/output21.jpg)

# Data process
   Gray image and label image of `data/membrane/` is 512*512, we can get more data by random crop image to 256*256.It means the network is training the shape of 256*256.Date processing code is `data/data_process.py` and crop images are saved in `data/prepare/`.
  
# Training
   `python train.py -h` should get you started. A proper CLI is yet to be added.<br>
   
   You can run:  `python train.py --gpu True -b 1 -s 1`
   
   `-b` options is batch size<br>
   `-s` options is scaling ratio

# Dependencies
   This package depends on [pydensecrf](https://github.com/lucasb-eyer/pydensecrf), available via `pip install`.

# Reference
   Learn from [Pytorch-Unet](https://github.com/milesial/Pytorch-UNet)
