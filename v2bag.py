#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import rospy
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

# 初始化节点
rospy.init_node('camera_node')

# 创建 ROS 发布者对象、图片消息桥接
image_publisher = rospy.Publisher('/image', Image, queue_size=10)
bridge = CvBridge()

# 创建 ROS 记录器
bag = None

# 打开摄像头
cap = cv2.VideoCapture(0)

# 是否正在记录 rosbag
is_recording = False

# 循环读取图像
while True:
    # 读取图像
    ret, frame = cap.read()

    # 如果读取失败，则跳过
    if not ret:
        continue

    # 将图像转换成 ROS 消息
    try:
        image_msg = bridge.cv2_to_imgmsg(frame, 'bgr8')
    except CvBridgeError as e:
        print(e)
        continue

    # 发布消息
    image_publisher.publish(image_msg)

    # 如果正在记录 rosbag，则将消息保存到 rosbag 文件中
    if is_recording and bag is not None:
        bag.write('/image', image_msg)

    # 显示图像
    cv2.imshow('Camera', frame)

    # 响应键盘事件
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        # 终止循环并停止录制 rosbag
        break 
    elif key == ord('s'):  
        # 开始记录 rosbag 
        if bag is None or not is_recording: 
            bag = rosbag.Bag('camera.bag', 'w')
            is_recording = True
            print('正在录制 rosbag')
        else:
            print('已经开始录制 rosbag')

# 如果正在录制 rosbag，则关闭文件
if is_recording and bag is not None:
    bag.close()
    print('停止录制 rosbag')

# 释放资源
cap.release()
cv2.destroyAllWindows()