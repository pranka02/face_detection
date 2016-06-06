# Face Detection Node for ROS using Rviz #

This is a ROS node which reads images from a given directory, detects faces, and publishes the images with the detected faces encircled to the <code>sensor_msgs/Image</code> topic which can be subscribed by Rviz to view them.


## Prerequisites ##

###1. [Install and configure ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)###

###2. Install  [Rviz](http://wiki.ros.org/rviz)###


## Getting Started ##

###1. Download or clone the package into your [catkin](http://wiki.ros.org/catkin)workspace###
 
###2. Initialisation ##
Source yur environment setup file.
```
$ source /opt/ros/%your distro%/setup.bash
```
From your catkin workspace, enter the following.
```
$ catkin_make
$ source ./devel/setup.bash
```
If you do not have OpenCV-2 versions installed, edit the find_package line in CMakeLists.txt.

###3.Running the code###
Open
```
$ source /opt/ros/%your distro%/setup.bash
```
```
$ rosrun face_detector imag_pub.py <OpenCV dir> <Database dir>

```

