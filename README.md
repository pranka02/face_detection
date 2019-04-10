# Face Detection ROS Node using OpenCV #

This is a ROS node which reads images from a given directory, detects faces, and publishes the images with the detected faces encircled, to the <code>sensor_msgs/Image</code> topic which can be subscribed by Rviz for visualisation.

### Prerequisites ###

1. [Install and configure ROS](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

2. Install  [Rviz](http://wiki.ros.org/rviz)


### Getting Started ###

#### 1. Download or clone the package into your [catkin](http://wiki.ros.org/catkin) workspace
 
#### 2. Initialisation
Open a new terminal and source your environment setup file by typing the following: 
```
$ source /opt/ros/%your_distro%/setup.bash
```
From your catkin workspace, enter the following:
```
$ catkin_make
$ source ./devel/setup.bash
```
If you do not have OpenCV-2 versions installed, edit the find_package line in CMakeLists.txt.

#### 3. Running the code
Open a new terminal and run [roscore](http://wiki.ros.org/rviz).
Do not forget to source the environmental setup file in each of the new terminals.
```
$ roscore
```
Open another terminal and run the code with arguments as shown below.
```
$ rosrun face_detector imag_pub.py <OpenCV dir> <Database dir>
```
Use another terminal to open rviz.
```
$ rosrun rviz rviz
```
Setup your rviz to subscribe to images from the <code>sensor_msgs</code> topic 

#### WORKING VIDEO ####

Watch the working [here](https://www.youtube.com/watch?v=4uYur-Mt1IQ)

#### DOCUMENTATION ####

Find the documentation link at <code>face_detection_documentation/documentation/index.html <code>
