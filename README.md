# Yolo Object Detection on NVIDIA Jetson Nano 

This repository provides a simple and easy process for camera installation, software and hardware setup, and object detection using Yolov5 on NVIDIA Jetson Nano.
This project uses [CSI-Camera](https://github.com/JetsonHacksNano/CSI-Camera) to create a pipeline and receive a frame from the CSI camera, and [Yolov5](https://github.com/ultralytics/yolov5) to detect objects, implementing a complete and executable code on the Jetson Development Kits.
Check out [CodePlay jetson nano youtube playlist](https://www.youtube.com/watch?v=5-SIV7r2uiU&list=PLZIi3Od9VUwW49q6T1VjShktoOgrDi3O4) for more. 

## Download Model


Select the desired model based on model size, required speed, and accuracy.
You can find available models [here](https://github.com/ultralytics/yolov5/releases) in the **Assets** section.
Download the model using the command below and move it to the **weights** folder.
```
$ wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5s.pt
```

## Requirements

#### Camera Setup
Install the camera in the MIPI-CSI Camera Connector on the carrier board.
The pins on the camera ribbon should face the Jetson Nano module.
You can use this [camera setup guide](https://www.arducam.com/docs/camera-for-jetson-nano/native-jetson-cameras-imx219-imx477/imx477/) for more info.

#### Camera Driver
By default, NVIDIA JetPack supports several cameras with different sensors, one of the most famous of which is the Raspberry Pi camera v2.
But if you use other cameras, you need to install a sensor driver.
A 12.3 MP camera with an IMX477-160 sensor is used in this project which requires an additional driver to connect. 
[Arducam IMX477 driver](https://www.arducam.com/docs/camera-for-jetson-nano/native-jetson-cameras-imx219-imx477/imx477-how-to-install-the-driver/) is IMX477 driver driver along with its easy installation guide.
Use the following command to check if the camera is recognized correctly.
```
$ ls /dev/video0
```
##### PyTorch
[PyTorch & torchvision for jetson](https://forums.developer.nvidia.com/t/pytorch-for-jetson-version-1-9-0-now-available/72048)

## Inference

Run
```
$ python3 JetsonYolo.py
```


