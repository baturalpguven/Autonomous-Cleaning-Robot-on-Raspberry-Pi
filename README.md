# Autonomous-Cleaning-Robot-on-Raspberry-Pi


This project aims to address the time-consuming and physically demanding nature of traditional cleaning techniques by developing an intelligent cleaning robot using IoT technologies. The robot's capabilities would not only reduce the time and effort required for cleaning but also improve the overall quality of cleaning. This would benefit homeowners, office and building managers, the hotel sector, as well as hospitals and healthcare facilities that require high cleanliness standards. The target audience is diverse.

To achieve this goal, a Raspberry Pi-based autonomous cleaning robot is utilized. The robot is designed to identify and locate objects, transmit information to a dedicated app, and be remotely controlled. Three crucial aspects are considered during the development process: processing power, software speed for data collection, and robot indoor localization. Quantized object detection models based on TensorFlow Lite are used to optimize processing power. A 15-second speed for comprehensive cleaning is deemed sufficient. Indoor localization is achieved using UWB-based techniques due to the limitations of GPS. The development process primarily relies on Bluetooth and Wi-Fi for wireless communication, with the addition of UWB for localization needs.

The project has achieved partial autonomy in the robot's movement, although further improvements are required. Manual movement of the robot functions smoothly. Despite some limitations in the chosen object detection model's classification accuracy, the transmission and classification of detected objects to the app are successful. The built-in software accurately recognizes objects, while the object localization accuracy of the team's app is comparatively lower.


![workflow](https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/88fa07fd-02c2-48ef-8dd4-7a03682d9eb3)

![implemantation](https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/2e8f80d6-0c2c-4712-9a08-4266b5f3bfc5)


## 1. Raspberry Pi 3B+
Raspberry Pi is placed in the second layer of the robot to control all of the functions of the robot. A power bank which has a capacity of 50000 mAh is placed near the Raspberry Pi and connected to it with GPIO USB to supply power to Raspberry Pi and other components such as sonar sensors, Pi Camera, and UWB anchors. 

## 2. DC Motors and Motor Driver
There were four different DC motors combined with plastic wheels connected to the motor driver for the movement of the product, and all of them were placed in the first layer of the body. The motor driver is connected to the Raspberry Pi with a breadboard via GPIO pins as can be seen in the hardware block diagram. To give power to the motor driver, a 17V DC battery is placed in the first layer of the robot and connected to the motor driver GPIO. 


## 3. Sonar Sensor
Sonar sensors connected to Raspberry Pi via a GPIO pin and placed in the second layer of the robot, are used for facilitating the autonomous movement and safety of the product. Whenever they detect an object closer than 20 centimeters, the robot stops towards the direction and changes its route. 

## 4. UWB Anchor
As can be seen in Figure 3, four different UWB anchors are connected to Raspberry Pi via GPIO USB and placed in the second layer of the product, which are used in the autonomous movement of the product. They are basically indoor GPS to be used in determining the route and location of the product. 
## 5. Broomstick
The cleaning would be done by the broomstick which is placed in the first layer of the robot’s body. 
## 6. USB Camera
The USB camera will be used to utilize object detection and will be on the second floor of the robot so that it can detect objects with a wider view angle.
## Android Mobile Phone
For manual control, an Android mobile phone is used which will be connected to the Raspberry Pi via Bluetooth protocol to control the robot manually when it is needed. Also, the data about the encountered object which comes from Raspberry Pi via Google Firebase can be seen in the mobile phone via Wi-Fi communication protocol. 

<img src="https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/df55a3d0-2942-4f4b-af58-b3e1d00a4f23" align = "center" >


![app](https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/df55a3d0-2942-4f4b-af58-b3e1d00a4f23)



You can see the demonstration of the project:

<p align="center">
  <a href="https://youtu.be/4zjsMoJlkdo">
    <img src="https://img.youtube.com/vi/4zjsMoJlkdo/0.jpg" alt="Thumbnail">
  </a>
</p>



