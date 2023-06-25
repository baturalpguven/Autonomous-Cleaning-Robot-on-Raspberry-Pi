# Autonomous-Cleaning-Robot-on-Raspberry-Pi


Cleaning the environment takes time and requires physical effort. Traditional cleaning techniques often demand a lot of work and can be difficult for people with mobility or health difficulties. Additionally, manual cleaning frequently results in missed spots or insufficient cleaning in specific regions. Homeowners who are busy, have mobility issues, or are ill may find it difficult to keep their houses clean on a regular basis. The goal of this project is to solve these problems by creating an intelligent cleaning robot that uses IoT technologies. With such a robot, cleaning activities would need a great deal less time and effort while also being done better overall. Homeowners would be able to spend more time on other things and experience less bodily stress as a result. This initiative would be advantageous to homeowners as well as office and building managers, as well as the hotel sector. It takes a lot of time and effort to clean large public and commercial venues, thus using an automated cleaning solution is incredibly beneficial. This concept could also be useful for hospitals and other healthcare facilities, which must maintain a high standard of cleanliness to ward off illnesses. Thus, a diverse group of people make up the target audience.

A Raspberry Pi-based autonomous cleaning robot that can identify objects, locate them, transmit information to a specially built app, and be remotely controlled is used to complete this challenging task. Three crucial aspects are taken into account during the development process: processing power, software speed for data collecting, and robot indoor localization. Using the devices at hand, appropriate solutions are presented and partially implemented to address these restrictions. Quantized object detection models (TensorFlow Lite) [5] are used for processing power. Given the necessary low speed, an updated speed of 15 seconds is judged adequate to guarantee comprehensive cleaning. Due to GPS's limitations, UWB-based [7] techniques are used for indoor localization. As required by the class, the primary strategy for the development process is to complete the work using Bluetooth and Wi-Fi, two wireless communication protocols. UWB is additionally included to address localization needs.
The robot can now move partially independently, which is one of the project's accomplishments (although there are still some flaws, so more work needs to be done). The robot's manual movement runs without a hitch. Despite the chosen model's subpar classification accuracy, the transmission of detected objects to the app and object classification are successful. Additionally, the built-in software can recognize objects accurately, however, our team's app has lesser object localization accuracy.


![image](https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/df55a3d0-2942-4f4b-af58-b3e1d00a4f23)

![image](https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/88fa07fd-02c2-48ef-8dd4-7a03682d9eb3)

![image](https://github.com/baturalpguven/Autonomous-Cleaning-Robot-on-Raspberry-Pi/assets/77858949/2e8f80d6-0c2c-4712-9a08-4266b5f3bfc5)


Raspberry Pi 3B+
Raspberry Pi is placed in the second layer of the robot to control all of the functions of the robot. A power bank which has a capacity of 50000 mAh is placed near the Raspberry Pi and connected to it with GPIO USB to supply power to Raspberry Pi and other components such as sonar sensors, Pi Camera, and UWB anchors. 

DC Motors and Motor Driver
There were four different DC motors combined with plastic wheels connected to the motor driver for the movement of the product, and all of them were placed in the first layer of the body. The motor driver is connected to the Raspberry Pi with a breadboard via GPIO pins as can be seen in the hardware block diagram. To give power to the motor driver, a 17V DC battery is placed in the first layer of the robot and connected to the motor driver GPIO. 


Sonar Sensor
Sonar sensors connected to Raspberry Pi via a GPIO pin and placed in the second layer of the robot, are used for facilitating the autonomous movement and safety of the product. Whenever they detect an object closer than 20 centimeters, the robot stops towards the direction and changes its route. 

UWB Anchor
As can be seen in Figure 3, four different UWB anchors are connected to Raspberry Pi via GPIO USB and placed in the second layer of the product, which are used in the autonomous movement of the product. They are basically indoor GPS to be used in determining the route and location of the product. 
Broomstick
The cleaning would be done by the broomstick which is placed in the first layer of the robot’s body. 
USB Camera
The USB camera will be used to utilize object detection and will be on the second floor of the robot so that it can detect objects with a wider view angle.
Android Mobile Phone
For manual control, an Android mobile phone is used which will be connected to the Raspberry Pi via Bluetooth protocol to control the robot manually when it is needed. Also, the data about the encountered object which comes from Raspberry Pi via Google Firebase can be seen in the mobile phone via Wi-Fi communication protocol. 



You can see the demonstration of the project:

<p align="center">
  <a href="https://youtu.be/4zjsMoJlkdo">
    <img src="https://img.youtube.com/vi/-4zjsMoJlkdo/0.jpg" alt="Thumbnail">
  </a>
</p>


