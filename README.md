# Autonomous-Cleaning-Robot-on-Raspberry-Pi


This project aims to mitigate the time-consuming and physically demanding aspects of conventional cleaning methods by developing an intelligent cleaning robot that utilizes IoT technologies. By reducing the required time and effort while improving cleaning quality, this project offers benefits to homeowners, office and building managers, the hotel sector, as well as hospitals and healthcare facilities with high cleanliness standards. The target audience is diverse.

To achieve this objective, an autonomous cleaning robot based on Raspberry Pi is employed. The robot is equipped with capabilities for object identification, localization, information transmission to a dedicated app, and remote control. The development process focuses on three crucial aspects: processing power, software speed for data collection, and indoor localization. Quantized object detection models based on  <a href="https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md"> TensorFlow Lite</a> , a widely-used framework for machine learning, are utilized to optimize processing power. For comprehensive cleaning, a 15-second update time is deemed sufficient for the app. Indoor localization leverages UWB-based techniques due to the limitations of GPS. Firebase serves as the primary database, and a pre-trained object detection model is employed. The development process utilizes Bluetooth and Wi-Fi for wireless communication, with the inclusion of UWB to address localization requirements.

## Running the Code
To execute the code, a working understanding of  <a href="https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md"> TensorFlow Lite</a>  is necessary. The classif.py file and the provided pre-trained weights can be utilized. The movement_subprocess_OB_Database_bluetooth.py, movement_subprocess.py, and draw_on_images.py files should be executed in the same directory. Please note that while the app developed by our team is not available, a custom Android Studio app will suffice for running the project.

# Diagram of the Working Principle of the Project


<p align="center">
<img src="https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/369dfb3e-08f8-4986-ae45-eb2d100597a0" align = "center" width="50%" height="50%">
</p>

# Implemantation of the Project


<p align="center">
<img src="https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/19868ea5-7dca-4f5f-8f5e-0956e88f6101" align = "center" width="50%" height="50%">
</p>




## 1. Raspberry Pi 3B+

In this project, the Raspberry Pi is positioned in the second layer of the robot to oversee and manage all of its functions. To provide power to the Raspberry Pi and other components like sonar sensors, Pi Camera, and UWB anchors, a power bank with a capacity of 50000 mAh is situated in close proximity to the Raspberry Pi. The power bank is connected to the Raspberry Pi via GPIO USB for an efficient power supply.

## 2. DC Motors and Motor Driver

In this project, the first layer of the robot contains four DC motors, each coupled with plastic wheels, responsible for the movement of the device. These motors are connected to a motor driver, which is situated in the same layer. To establish the connection between the motor driver and the Raspberry Pi, a breadboard is employed, utilizing GPIO pins as depicted in the hardware block diagram. In order to supply power to the motor driver, a 17V DC battery is positioned within the first layer of the robot and connected to the motor driver via GPIO.

## 3. Sonar Sensor
Sonar sensors are employed in the second layer of the robot and connected to the Raspberry Pi via a GPIO pin. These sensors play a crucial role in facilitating  autonomous movement and ensuring the safety of the robot. By detecting objects within proximity of fewer than 20 centimeters, the robot promptly halts its movement in that direction and adjusts its path accordingly.

## 4. UWB Anchor
Ultra-Wideband (UWB) technology plays a crucial role in the autonomous movement of the robot in this project. Four UWB anchors are strategically positioned in the second layer of the robot, as depicted in the "Diagram of the Working Principle of the Project". These anchors are connected to the Raspberry Pi through GPIO USB connections.

UWB technology is employed as an indoor GPS system for the robot. It utilizes short-range radio waves with a wide spectrum to precisely measure the time of flight (TOF) of signals. By measuring the time it takes for the signals to travel between the UWB anchors and the robot, the system can accurately calculate the robot's position in real time.

The UWB anchors act as reference points in the environment, providing distance and positioning information to the Raspberry Pi. This information is used to determine the most efficient routes for the robot to navigate and make informed decisions regarding its movement.

With the aid of UWB technology, the robot can determine its precise location within the environment, enabling it to effectively navigate and perform cleaning tasks autonomously. By utilizing UWB as an indoor GPS system, the robot can achieve accurate localization and improve the overall efficiency and effectiveness of its movement within the designated space.

## 5. Broomstick
The cleaning mechanism is executed by a broomstick, which is positioned in the first layer of the robot's body. It plays a pivotal role in carrying out the cleaning tasks assigned to the robot.

## 6. USB Camera

 <a href="https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md"> TensorFlow Lite</a>  is employed to facilitate object detection capabilities in this project, specifically for edge devices like the USB camera utilized by the robot. TensorFlow Lite is a lightweight and optimized version of the TensorFlow framework, designed specifically for running machine learning models on resource-constrained devices, such as edge devices and mobile devices.

Model compression techniques are applied to enable the efficient deployment of machine learning models on edge devices. These techniques aim to reduce the size of the model without significantly compromising its performance. By compressing the model, it becomes more suitable for deployment on edge devices with limited computational resources, such as the USB camera in this project.

The USB camera, situated on the second floor of the robot, provides a broader field of view, allowing for effective object detection and recognition. Through the utilization of TensorFlow Lite and model compression techniques, the USB camera can efficiently process the captured images and leverage the object detection capabilities to identify and recognize objects within its field of view. This enables the robot to perform tasks such as object tracking, obstacle avoidance, or any other relevant functionality required for its autonomous operation.

## Android Mobile App
An Android mobile phone is employed for manual control of the robot. It is connected to the Raspberry Pi via the Bluetooth protocol, allowing users to manually control the robot when necessary. Furthermore, the mobile phone serves as a display interface for viewing data regarding encountered objects, which is transmitted from the Raspberry Pi via the Google Firebase platform using Wi-Fi communication protocols.
![image](https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/1a420a87-a0f4-4864-92b1-00f6535a6e9f)



<p align="center">
<img src="https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/1a420a87-a0f4-4864-92b1-00f6535a6e9f" align = "center" width="50%" height="50%">
</p>


## Demo of the Project

<p align="center">
  <a href="https://youtu.be/4zjsMoJlkdo">
    <img src="https://img.youtube.com/vi/4zjsMoJlkdo/0.jpg" alt="Thumbnail">
  </a>
</p>



