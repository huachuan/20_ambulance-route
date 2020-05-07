# Smart traffic light
## [Check our Youtube demo video](https://youtu.be/kPmq3VhWfX8)
Using Raspberry Pis, sound sensors and cameras to control the traffic lights. This project aims to secure the emergency vehicles. When detecting the siren and image of the emergency vehicle, green light will turn on for the emergency vehicles.

<p align="center">
  
  <img width="400" src="doc/camera_position_facing.png"> <img width="400" src="doc/top_view.JPG">
  
  Figure 1. Setup. Each camera detect the emergency vehicle in one direction. 
</p>
  
## Hardware Requirements
- **Four Raspberry Pis with Micro SD cards**
- **LED Traffic lights**
- **Cameras**
- **Sound detectors**
- **AC Police car**

## Setup
- **Rename Raspberry Pis**: Rename the Raspberry Pis according to the camera facing, e.g. North facing pi's hostname is pi@north. 
- **Set static IP**: [Click here for details](https://www.ionos.com/digitalguide/server/configuration/provide-raspberry-pi-with-a-static-ip-address/)
- **Traffic light**: [Installation and coding](https://projects.raspberrypi.org/en/projects/traffic-lights-python)
- **Sound detectors**: [Installation and test](https://www.youtube.com/watch?v=GiXNUYPrQ7I)
- **Camera**:[Getting started with Pi cameras](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
- **Install Tensorflow LITE for real time object detection**: Please check this reference for details [Real-time Object Tracking with TensorFlow, Raspberry Pi, and Pan-Tilt HAT](https://towardsdatascience.com/real-time-object-tracking-with-tensorflow-raspberry-pi-and-pan-tilt-hat-2aeaef47e134)

## Client and Server

Use a laptop as the server to communicate with the Pis (Python code). On the server side, the server determines the mode of the current situation. 
- **Regular Mode**: Normal traffic light, each color will last 5 seconds. Lights in north & south direction are orthogonal to west and east. 
- **Flashing Mode**: Sound detector is triggered. Amber lights in all directions are turned on and blinking for 10 seconds.
- **Emergency Mode**: Both sound detector and camera is triggered. When Flashing Mode is on, if the camera detects the objects within 10 seconds, the Emergency mode will be turned on. The traffic light in the direction of that moving emergency vehicle will trun green, the orthogonal direction will turn red for 10 seconds.

## Demo

<p align="center">
  
  <img width="300" src="doc/car_detect.gif"> 
  
  Camera detect the emergency vehicle using Tensorflow LITE. 
</p>
<p align="center">
  
  <img width="600" src="doc/flashmode.gif">
  
When the sound sensor detects the siren, amber light of all directions will be on to warn the pedestrians and other vehicles. The flashing mode will last 10 seconds, if the camera does not detects the emergency vehicle on any direction, the regular mode will be recovered. 

</p>

<p align="center">
  
<img width="600" src="doc/emergency_mode.gif">

When the flashing mode is on and the camera detects the emergency vehicle on one direction, the emergency mode will be on. Green lights is given to the emergency vehicle. When flashing mode is off, the camera cannot turn on emergency mode.

</p>
