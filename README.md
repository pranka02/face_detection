# Face Detection Node for ROS using Rviz #

This is a ROS node which reads images from a given directory, detects faces, and publishes the images with the detected faces encircled to the <code>sensor_msgs/Image</code> topic which can be subscribed by Rviz to view them.


## Prerequisites ##

###1. [Install and configure ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)###

###2. Run [ROS Core](http://wiki.ros.org/roscore)###

Enter the following into the terminal:

```
$ roscore
```

###3. Run [Rviz](http://wiki.ros.org/rviz)###

Open a new terminal and enter the following:

```
$ rosrun rviz rviz
```


## Getting Started ##

###1. Download or clone the package###

###2. Run the package on ROS###
Open a new terminal and enter the following:

```
$ rosrun face_detector imag_pub.py <OpenCV dir> <Database dir>

```

