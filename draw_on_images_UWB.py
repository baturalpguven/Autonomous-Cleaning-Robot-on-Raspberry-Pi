import cv2
import serial
import time 
import os
import pyrebase



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

storage = firebase.storage()
database = firebase.database()

# Load image
image = cv2.imread("Lab_diagram.jpg")

# input_str = "DIST,3,AN0,8182,7.18,0.30,0.00,0.83,AN1,0F8C,4.18,3.10,0.00,0.18,AN2,5C2F,0.20,0.20,0.00,0.59,POS,0.83,0.52,0.00"

DWM = serial.Serial(port = "/dev/ttyACM0",baudrate = 115200)
print("connected to " + DWM.name)
DWM.write("\r\r".encode())
print("Encode")
time.sleep(1)
DWM.write("lec\r".encode())
print("Encode")
time.sleep(1)
try:
    while True:
        try:
            input_str = DWM.readline()
            
            if(input_str):
                # print(input_str)
                
                input_list = input_str.decode().replace("\r\n","")
                input_list = input_list.split(",")
                print(input_list)
                if ("DIST" in input_list and "AN0" in input_list  and "AN1" in input_list  and "AN2" in input_list ): 
                    # os.remove("location.jpg")
                # Split the string by comma separator

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
                    # x, y = int(tag[0] * 100), int(tag[1] * 100)
                    image[y:y+50, x:x+50] = robot_icon

                    # cv2.putText(image, "MyRobot", (x-20, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)
                    cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

                    # Show the image with the circles drawn on it
                    # cv2.imshow("Image with Circles", image)

                    
                    time.sleep(1)
                    cv2.imwrite("location.jpg", image)
                    storage.child('location.jpg').put('location.jpg')
                    os.remove("location.jpg")
                    print("--------------------------img_saved----------------------------")
                else:
                    break
        except:
            DWM = serial.Serial(port = "/dev/ttyACM0",baudrate = 115200)
            print("connected to " + DWM.name)
            DWM.write("\r\r".encode())
            print("Encode")
            time.sleep(1)
            DWM.write("lec\r".encode())
            print("Encode")
            time.sleep(1)


except KeyboardInterrupt:
    print("\n Stop")
    DWM.write("\r".encode())
    DWM.close()