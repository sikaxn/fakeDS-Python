# Fake Driver Station (robot enabler) Python (2024 DS protocol)

## IMPORTANT SAFETY WARNING (Please read though this entire thing)

**THIS SCRIPT COULD CREATE A RUN AWAY ROBOT!!!!! USE AT YOUR OWN RISK!!!**

**Using this script in an official FRC event could be illegal and is unsafe!!!**

Please make sure you absolutely know what you're doing. Most FRC robot loaded with competition code are not suitable for using this script.

**It is strongly NOT recommanded to run this script direct on the robot** (unless you absolutely know what you're doing) either on roboRIO or on a coprocessor because it's hard to disable the robot (close this script) in such case.

**Alternative e-stop should be implimented. Space bar for E-STOP is nonexist.** If you use this script, there's no way to stop the robot unless you have the roboRIO or motors physically deenergized. A cheap Amazon wireless relay board hooked up to roboRIO power could do this job. However it is your responsibility to determain the best way to have the robot disabled. 

If you are using this script to enable robot for off season demo, etc which you really don't want to have a DS please use the official DS during regular testing and only impliment this script at the very last after you had throughly tested your code.   

**Robot can be dangerous.** By using the this script, you understand that **there's no safety feature built into this script** thus you, the operator, play a critical part in making sure that the environment around you is safe before enabling robots. You should only enable robots (run this script) **when the robots are in a contained area and segregated from humans, who may be injured due to the robot's motion. If you disagree, or are not willing to use the software under these conditions, you should not proceed.**

## Why this script is here

The origional Driver Station includes a lot of safety feature which could cause some trouble if you're trying to use roboRIO with WPILIB under some very niche case where the use of a operator console (Driver Station computer) or the official Driver Station software is not ideal. Say you're using roboRIO and raspberry pi to make a vending machine for a school project and you don't want to hookup a Driver Station computer all the time. This script could keep roboRIO enabled (CAN and PWM could control motors) without a DS computer.

## What this script does

This script send raw UDP packet to roboRIO to put it to enabled teleop mode. 


## How to use this script

replace``your_roboRIO_IP_address`` at ``ip_address = "your_roboRIO_IP_address"`` to the ip address or mDNS address of your roboRIO and run this script would put robot in teleop.

Before starting this script, you MUST close any Driver Station software connected to the robot, or this script night not work. This script and other DS would not work at the same time.

## Known issue:

 - Script could crash if mDNS address is used. Using IP address would
   fix this.
 - You can't use any joystick or controllers. To control the robot, you would use something like NetworkTable or have it run fully automonously
 - Sometimes after running this script, roboRIO won't enable and official DS won't even connect. In this case, reboot roboRIO would fix this problem. Make sure you don't have any other DS or this script running while reboot.

## Attribution

Some idea and concept of this script was inspired by 

-[Is there a way to create a motor testing board using standard FRC components without using the RoboRIO?](https://www.chiefdelphi.com/t/is-there-a-way-to-create-a-motor-testing-board-using-standard-frc-components-without-using-the-roborio/412788)

-[FakeDS Java script by SLUH Robotics - FRC 5176](https://github.com/Team-5176/testbench/blob/master/src/main/java/frc/robot/FakeDS.java)

-[LibDS](https://github.com/FRC-Utilities/LibDS)