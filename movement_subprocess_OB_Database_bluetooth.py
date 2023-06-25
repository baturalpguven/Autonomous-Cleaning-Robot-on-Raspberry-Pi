# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Main script to run image classification."""

import bluetooth
import argparse
import sys
import time

import pyrebase

import cv2

import RPi.GPIO as GPIO          
from time import sleep
import time
import sys
import signal


from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import logging

# Visualization parameters
_ROW_SIZE = 20  # pixels
_LEFT_MARGIN = 24  # pixels
_TEXT_COLOR = (0, 0, 255)  # red
_FONT_SIZE = 1
_FONT_THICKNESS = 1
_FPS_AVERAGE_FRAME_COUNT = 10

def signal_handler(signal, frame): # ctrl + c -> exit program
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def sonar_sensor(trig,echo):
    GPIO.output(trig, False)
    time.sleep(0.1)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    while GPIO.input(echo) == 0 :
        pulse_start = time.time()
    while GPIO.input(echo) == 1 :
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    # if pulse_duration >=0.01746:
    #     print('time out')
    # elif distance > 300 or distance==0:
    #     print('out of range')
    distance = round(distance, 3)
    tmp = 'Distance : {:.2f} cm'.format(distance)
    print(tmp)
    # logging.debug('Distance : %f cm'%distance)
    return distance,tmp
def init():
    GPIO.setmode(GPIO.BCM)
    trig = 27 # 7th
    echo = 17 # 6th

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    time.sleep(0.5)


    in1 = 22 #PIN31
    in3 = 24 #PIN35
    in2 = 16 #PIN10
    in4 = 10 #PIN24
    en = 23   #PIN18
    en2 = 2  #PIN3
    temp1=1

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(en,GPIO.OUT)
    GPIO.setup(en2,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    p=GPIO.PWM(en,1000)
    p1=GPIO.PWM(en2,1000)
    p.start(100)
    p1.start(100)
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
    print("\n")    
    return in1,in2,in3,in4,en,en2,p,p1,trig,echo

def manual_override_bluetooth(in1,in2,in3,in4,en,en2):
    # Set up Bluetooth server
    # in1,in2,in3,in4,en,en2,p,p1,trig,echo = init()
    host = ""
    port = 1
    server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print('Bluetooth Socket Created')
    try:
        server.bind((host, port))
        print("Bluetooth Binding Completed")
    except:
        print("Bluetooth Binding Failed")
        

    # Start listening for incoming connections
    server.listen(1)
    client, address = server.accept()
    print("Connected To", address)
    print("Client:", client)
    return client,address


    client.close()
    server.close()

    return x

    # Clean up GPIO and Bluetooth resources before exiting
    # GPIO.cleanup()
 

def UWB(input_str):
    # Load image
    image = cv2.imread("lab_diagram.jpg")

    # input_str = "DIST,3,AN0,8182,7.18,0.30,0.00,0.83,AN1,0F8C,4.18,3.10,0.00,0.18,AN2,5C2F,0.20,0.20,0.00,0.59,POS,0.83,0.52,0.00"

    # Split the string by comma separator
    input_list = input_str.split(',')

    # Get the number of anchors
    num_anchors = int(input_list[1])

    input_list = input_list[2:]

    # Extract the anchors' information
    anchors = []
    for i in range(num_anchors):
        anchor_name = input_list[0 + i * 6]
        anchor_id = input_list[1 + i * 6]
        x_pos = float(input_list[2 + i * 6])
        y_pos = float(input_list[3 + i * 6])
        z_pos = float(input_list[4 + i * 6])
        distance = float(input_list[5 + i * 6])
        anchors.append((anchor_name, anchor_id, x_pos, y_pos, z_pos, distance))
    # print("Anchors:", anchors)

    # Extract the POS tag information
    x_pos_tag = float(input_list[-3])
    y_pos_tag = float(input_list[-2])
    z_pos_tag = float(input_list[-1])
    tag = (x_pos_tag, y_pos_tag, z_pos_tag)

    # Draw circles for each anchor and the tag
    for anchor in anchors:
        x, y = int(anchor[2] * 100), int(anchor[3] * 100)
        cv2.putText(image, f"{anchor[0]} ({anchor[1]})", (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
        cv2.circle(image, (x, y), 5, (0, 0, 0), -1)

    x, y = int(tag[0] * 100), int(tag[1] * 100)
    # Load the image
    robot_icon = cv2.imread('tentative_model_of_robot.jpg', cv2.IMREAD_UNCHANGED)

    # Resize the image
    robot_icon = cv2.resize(robot_icon, (50, 50))

    # Draw the image at the robot's position
    x, y = int(tag[0] * 100), int(tag[1] * 100)
    image[y:y+50, x:x+50] = robot_icon

    cv2.putText(image, "MyRobot", (x-20, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)
    cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

    # Show the image with the circles drawn on it
    # cv2.imshow("Image with Circles", image)
    img_name = "location.jpg"
    cv2.imwrite(img_name, image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img_name

def run(model: str, max_results: int, score_threshold: float, num_threads: int,
        enable_edgetpu: bool, camera_id: int, width: int, height: int) -> None:
  """Continuously run inference on images acquired from the camera.

  Args:
      model: Name of the TFLite image classification model.
      max_results: Max of classification results.
      score_threshold: The score threshold of classification results.
      num_threads: Number of CPU threads to run the model.
      enable_edgetpu: Whether to run the model on EdgeTPU.
      camera_id: The camera id to be passed to OpenCV.
      width: The width of the frame captured from the camera.
      height: The height of the frame captured from the camera.
  """
    
  # Initialize the image classification model
  base_options = core.BaseOptions(
      file_name=model, use_coral=enable_edgetpu, num_threads=num_threads)
  in1,in2,in3,in4,en,en2,p,p1,trig,echo = init()
  
  config = {
  "apiKey": "AIzaSyDuTEnDXi0VFMYh5CTjyA1iLbcM2pVnBTo",
  "authDomain": "smartcleaningrobot-522d3.firebaseapp.com",
  "databaseURL": "https://smartcleaningrobot-522d3-default-rtdb.firebaseio.com",
  "projectId": "smartcleaningrobot-522d3",
  "storageBucket": "smartcleaningrobot-522d3.appspot.com",
  "messagingSenderId": "570884986702",
  "appId": "1:570884986702:web:47653519fabe2fca16301f"
}
  firebase = pyrebase.initialize_app(config)
#   cnt = 1

  storage = firebase.storage()
  database = firebase.database()
#   client,server,use_bluetooth = bluetooth_connect()

#   database.child("First Connection with DB")

  # Enable Coral by this setting
  classification_options = processor.ClassificationOptions(
      max_results=max_results, score_threshold=score_threshold)
  options = vision.ImageClassifierOptions(
      base_options=base_options, classification_options=classification_options)

  classifier = vision.ImageClassifier.create_from_options(options)

  logging.basicConfig(filename="./log.txt",level=logging.DEBUG)
  with open("./log.txt",mode="w") as file:
     file.write("")


  # Variables to calculate FPS
  counter, fps = 0, 0
  start_time = time.time()



  # Start capturing video input from the camera
  cap = cv2.VideoCapture(camera_id)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


  
  # Continuously capture images from the camera and run inference
  x=input("raw_input: ")
  client,_=manual_override_bluetooth(in1,in2,in3,in4,en,en2)
  while cap.isOpened():
    success, image = cap.read()
    distance,tmp = sonar_sensor(trig,echo)
    if distance<5:
        x='s'
    if not success:
      sys.exit(
          'ERROR: Unable to read from webcam. Please verify your webcam settings.'
      )

    counter += 1
    image = cv2.flip(image, 1)

    # Convert the image from BGR to RGB as required by the TFLite model.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create TensorImage from the RGB image
    tensor_image = vision.TensorImage.create_from_array(rgb_image)
    # List classification results
    categories = classifier.classify(tensor_image)
    database.child("Scene")


    # Show classification results on the image
    for idx, category in enumerate(categories.classifications[0].categories):
      category_name = category.category_name
      score = round(category.score, 2)
      result_text = category_name + ' (' + str(score) + ')'
      database.set({"Scene": category_name +"--"+tmp})
      logging.debug(result_text+tmp)
      text_location = (_LEFT_MARGIN, (idx + 2) * _ROW_SIZE)
      cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                  _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)


    # if use_bluetooth == "Bluetooth Binding Completed":
    #     data = client.recv(1024) # 1024 is the buffer size.
    #     data = data.decode("utf-8")
    # else:
    #     data ="Z"
    # Calculate the FPS
    if counter % _FPS_AVERAGE_FRAME_COUNT == 0:
      end_time = time.time()
      fps = _FPS_AVERAGE_FRAME_COUNT / (end_time - start_time)
      start_time = time.time()

    # Show the FPS
    fps_text = 'FPS = ' + str(int(fps))
    text_location = (_LEFT_MARGIN, _ROW_SIZE)
    cv2.putText(image, fps_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)

    # Stop the program if the ESC key is pressed.
    if cv2.waitKey(1) == 27:
      break
    cv2.imshow('image_classification', image)
    cv2.imwrite('scene.jpg', image)
    storage.child('scene.jpg').put('scene.jpg')
    # cnt +=1


    data = client.recv(1024)
    if not data:
        x='f'  # No more data from client
    
    data_str = data.decode('utf-8').strip()
    print("Received:", data_str)
                
    if data_str=='S':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        # x=input("raw_input: ")
        # distance = sonar_sensor(trig,echo)

    elif data_str == "U":
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(en,GPIO.HIGH)
        GPIO.output(en2,GPIO.HIGH)
    
    elif data_str == "D":
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(en,GPIO.HIGH)
        GPIO.output(en2,GPIO.HIGH)

    elif data_str == "R":
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(en,GPIO.HIGH)
        GPIO.output(en2,GPIO.HIGH)

    elif data_str == "L":
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(en,GPIO.HIGH)
        GPIO.output(en2,GPIO.HIGH)

    elif data_str == "e":
        x='f'

    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x=input("raw_input: ")
        # distance = sonar_sensor(trig,echo)



    elif x=='f':
        print("forward")
        logging.debug("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(en,GPIO.HIGH)
        GPIO.output(en2,GPIO.HIGH)
        # temp1=1
        x='z'
        # print(distance)


    elif x=='b':
        print("backward")
        logging.debug("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in4,GPIO.HIGH)
        # temp1=0
        x='z'
        

    elif x=='1':
        print("left")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
    elif x=='2':
        print("right")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        p1.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        p1.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(125)
        p1.ChangeDutyCycle(125)
        x='z'
    
    
    elif x=='e':
        cap.release()
        GPIO.cleanup()
        cv2.destroyAllWindows()
        # client.close()
        # server.close()
        break

  cap.release()
  GPIO.cleanup()
#   client.close()
#   server.close()
  cv2.destroyAllWindows()


def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument(
      '--model',
      help='Name of image classification model.',
      required=False,
      default='efficientnet_lite0.tflite')
  parser.add_argument(
      '--maxResults',
      help='Max of classification results.',
      required=False,
      default=3)
  parser.add_argument(
      '--scoreThreshold',
      help='The score threshold of classification results.',
      required=False,
      type=float,
      default=0.0)
  parser.add_argument(
      '--numThreads',
      help='Number of CPU threads to run the model.',
      required=False,
      default=4)
  parser.add_argument(
      '--enableEdgeTPU',
      help='Whether to run the model on EdgeTPU.',
      action='store_true',
      required=False,
      default=False)
  parser.add_argument(
      '--cameraId', help='Id of camera.', required=False, default=0)
  parser.add_argument(
      '--frameWidth',
      help='Width of frame to capture from camera.',
      required=False,
      default=640)
  parser.add_argument(
      '--frameHeight',
      help='Height of frame to capture from camera.',
      required=False,
      default=480)
  args = parser.parse_args()

  run(args.model, int(args.maxResults),
      args.scoreThreshold, int(args.numThreads), bool(args.enableEdgeTPU),
      int(args.cameraId), args.frameWidth, args.frameHeight)


if __name__ == '__main__':
  main()
