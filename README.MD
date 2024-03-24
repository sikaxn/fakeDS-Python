# Fake Driver Station (robot enabler) Python (2024 DS protocol)

Origional idea: [FakeDS](https://github.com/Team-5176/testbench/blob/master/src/main/java/frc/robot/FakeDS.java)

## IMPORTANT SAFETY WARNING

**THIS SCRIPT COULD CREATE A RUN AWAY ROBOT!!!!! USE AT YOUR OWN RISK!!!**

**Using this script in an official FRC event could be illegal and is unsafe!!!**

Please make sure you absolutely know what you're doing. Most FRC robot code for competition will not be suitable for the use of this script.

**It is strongly NOT recommanded to run this script direct on the robot** (unless you absolutely know what you're doing) either on roboRIO or on a coprocessor because it's hard to disable the robot (close this script) in such case.

**Alternative e-stop should be implimented. Space bar for E-STOP is nonexist.** If you use this script, there's no way to stop the robot unless you have the roboRIO or motors physically deenergized. A cheap Amazon wireless relay board hooked up to roboRIO power could do this job. However it is your responsibility to determain the best way to have the robot disabled. 

If you are using this script to enable robot for off season demo, etc which you really don't want to have a DS please use the official DS during testing and only use this script in the very last after you had throughly tested your code. Please 

**Robot can be dangerous.** By using the this script, you understand that **there's no safety feature built into this script ** thus you, the operator, play a critical part in making sure that the environment around you is safe before enabling robots. You should only enable robots (run this script) **when the robots are in a contained area and segregated from humans, who may be injured due to the robot's motion. If you disagree, or are not willing to use the software under these conditions, you should not proceed.**

## What this script does

This script send raw UDP packet to roboRIO to put it to enabled teleop mode. Potential use of this script would be using wpilib without driver station for full autonomous unattended situation under non FRC event. 

## How to use this script
replace``your_roboRIO_IP_address`` at ``ip_address = "your_roboRIO_IP_address"  `` to the ip address or mDNS address of your roboRIO and run this script would put robot in teleop.


## Known issue:

 - Script could crash if mDNS address is used. Using IP address would
   fix this.
 - You can't use any joystick or controllers unless you want to do some deep diving in Network Tables

