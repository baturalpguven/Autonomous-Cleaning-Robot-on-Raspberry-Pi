# Autonomous-Cleaning-Robot-on-Raspberry-Pi


This project aims to mitigate the time-consuming and physically demanding aspects of conventional cleaning methods by developing an intelligent cleaning robot that utilizes IoT technologies. By reducing the required time and effort while improving cleaning quality, this project offers benefits to homeowners, office and building managers, the hotel sector, as well as hospitals and healthcare facilities with high cleanliness standards. The target audience is diverse.

To achieve this objective, an autonomous cleaning robot based on Raspberry Pi is employed. The robot is equipped with capabilities for object identification, localization, information transmission to a dedicated app, and remote control. The development process focuses on three crucial aspects: processing power, software speed for data collection, and indoor localization. Quantized object detection models based on TensorFlow Lite, a widely-used framework for machine learning, are utilized to optimize processing power. For comprehensive cleaning, a 15-second update time is deemed sufficient for the app. Indoor localization leverages UWB-based techniques due to the limitations of GPS. Firebase serves as the primary database, and a pre-trained object detection model is employed. The development process utilizes Bluetooth and Wi-Fi for wireless communication, with the inclusion of UWB to address localization requirements.

##Running the Code
To execute the code, a working understanding of TensorFlow Lite is necessary. The classif.py file and the provided pre-trained weights can be utilized. The movement_subprocess_OB_Database_bluetooth.py, movement_subprocess.py, and draw_on_images.py files should be executed in the same directory. Please note that while the app developed by our team is not available, a custom Android Studio app will suffice for running the project.

## Diagram of the Working Principle of the Project
<p align="center">
<img src="https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/88fa07fd-02c2-48ef-8dd4-7a03682d9eb3" align = "center" width="50%" height="50%">
</p>

# Implemantation of the Project
<p align="center">
<img src="https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/2e8f80d6-0c2c-4712-9a08-4266b5f3bfc5" align = "center" width="50%" height="50%">
</p>




## 1. Raspberry Pi 3B+

In this project, the Raspberry Pi is positioned in the second layer of the robot to oversee and manage all of its functions. To provide power to the Raspberry Pi and other components like sonar sensors, Pi Camera, and UWB anchors, a power bank with a capacity of 50000 mAh is situated in close proximity to the Raspberry Pi. The power bank is connected to the Raspberry Pi via GPIO USB for an efficient power supply.

## 2. DC Motors and Motor Driver

In this project, the first layer of the robot contains four DC motors, each coupled with plastic wheels, responsible for the movement of the device. These motors are connected to a motor driver, which is situated in the same layer. To establish the connection between the motor driver and the Raspberry Pi, a breadboard is employed, utilizing GPIO pins as depicted in the hardware block diagram. In order to supply power to the motor driver, a 17V DC battery is positioned within the first layer of the robot and connected to the motor driver via GPIO.

## 3. Sonar Sensor
Sonar sensors are employed in the second layer of the robot and connected to the Raspberry Pi via a GPIO pin. These sensors play a crucial role in facilitating  autonomous movement and ensuring the safety of the robot. By detecting objects within proximity of fewer than 20 centimeters, the robot promptly halts its movement in that direction and adjusts its path accordingly.

## 4. UWB Anchor
Four UWB anchors, situated in the second layer of the robot as shown in Figure 3, are connected to the Raspberry Pi via GPIO USB. These anchors are integral to the autonomous movement of the robot, functioning as indoor GPS systems to determine the most efficient routes and accurately ascertain the location of the robot within the environment.

## 5. Broomstick
The cleaning mechanism is executed by a broomstick, which is positioned in the first layer of the robot's body. It plays a pivotal role in carrying out the cleaning tasks assigned to the robot.

## 6. USB Camera
A USB camera is utilized to enable object detection capabilities. It is placed on the second floor of the robot, providing a wider field of view for effective object detection and recognition.

## Android Mobile App
An Android mobile phone is employed for manual control of the robot. It is connected to the Raspberry Pi via the Bluetooth protocol, allowing users to manually control the robot when necessary. Furthermore, the mobile phone serves as a display interface for viewing data regarding encountered objects, which is transmitted from the Raspberry Pi via the Google Firebase platform using Wi-Fi communication protocols.

<p align="center">
<img src="https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/df55a3d0-2942-4f4b-af58-b3e1d00a4f23" align = "center" width="50%" height="50%">
</p>


## Demo of the Project

<p align="center">
  <a href="https://youtu.be/4zjsMoJlkdo">
    <img src="https://img.youtube.com/vi/4zjsMoJlkdo/0.jpg" alt="Thumbnail">
  </a>
</p>



