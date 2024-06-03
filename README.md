# S.M.O.R.T. PROJECT 
**Smart, Modular, Off-axis, Reloadable, Tube-launcher**

## Table of Contents



* [Planning](#Planning) 
* [Materials](#Materials)
* [CAD](#CAD)
* [Photos of the Shell and Cannon](#Photos)
* [Circuit Diagram](#Circuit_Diagram)
* [Code](#Code)
* [Failed launches and other issues](#Failures)
* [Plotted Data and Analysis](#Plotted_Data+Analysis)
* [Final Version](#Final_Version)



# Planning 
Here is a more detailed planning document[LINK](https://github.com/Pweder3/SMORT/tree/main/Documentation/Planning).
# Materials

- Pico
- Rocket Body
- LSMDOX sensor
- MPL3115A2 Altimeter
- Spring
- Fins
- Tube
- Tube mount
-
-
-
-
-
-
-
-


# CAD
Most of the CAD that we did was to create the shell that we would fire and the mount for the tube. Both of these items were 3d printed. All three group members worked on the CAD but most of it was done by Lucia and Cyrus

- Tube Mount

- Shell
The shell is modular and all of our versions involved 3-4 sections that could be removed and replaced if we broke them or decided on a different design. This was very useful when making the fins. We went through 5 different variations of the fin design and if we hadn't made the rocket modular we wouldn't have had to reprint a new rocket every time. Paul's thread design makes it super easy to remove the parts. The Nose and body parts remained the same the whole time. We could've made improvements to the nose but we found that the design was good enough for our purposes. The fins desperately needed a redesign. With the use of OpenRocket and internet research, we decided that deployable fins would be our best option.



Here is a link to more detailed documentation of our CAD process [LINK](https://github.com/Pweder3/SMORT/tree/main/Documentation/CAD).
Here is a link to our OnShape document where you can directly look at our CAD [LINK](https://github.com/Pweder3/SMORT/blob/main/Documentation/CAD/OnshapeLink.md)

<img src = "https://github.com/Pweder3/SMORT/blob/main/Documentation/Images/Images/Deployable%20Fins%20Packed.png" width = 500>
Here is a picture of our fin design in the folded position
<img src = "https://github.com/Pweder3/SMORT/blob/main/Documentation/Images/Images/Deployable%20Fins%20Image.png" width = 500>
This is a picture of our fins in the deployed position


# Photos

_photos that we took during the building process
_
# Circuit_Diagram



# Code

## Replication of the calibration
to calibrate you can follow [this](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-sensorlab-magnetometer-calibration.pdf) tourtial from adafruit. Use a metro M4 (I used an airlift) not a pico because it doesn't seem to be able to run the code given in the tutorial. Another thing to note is that you need a certain amount of program mem that things like the Arduino UNO don't have. To install the dependencies for Python run the following commands in the terminal

- `pip3 install matplotlib`
- `pip3 install pyserial` (Although the import message says import serial it is part of the pyserial package, not the serial package)
- `pip3 install numpy`

Note that some may have to **use Python 3.11 or lower** because of import changes in 3.12. To find the serial port that the metro is connected to use the Arduino IDE and go to tools and then port and it should be the one listed under your board. Also, note that this info is all our team's issues with the tutorial and the problems that we had.

# Failures
We had many failed launch attempts with our rocket-propelled shells and we have more documentation of those attempts here [More Launch Info](https://github.com/Pweder3/SMORT/blob/main/Documentation/Launch%20Documentation.md)


## Tube Fire
<img src = "https://github.com/Pweder69/SMORT/blob/48975b8509867a4feda575c4828a8f50840fb580/Documentation/Images/Images/ignition1.gif" width =300>
<img src = "https://github.com/Pweder69/SMORT/blob/main/Documentation/Images/Images/fullbody.ignition1.jpg" width =500>
<img src = "https://github.com/Pweder69/SMORT/blob/main/Documentation/Images/Images/endcap.ignition1.jpg" width =200><img src = "https://github.com/Pweder69/SMORT/blob/main/Documentation/Images/Images/tubeview.ignition1.jpg" width =200>


# Plotted_Data+Analysis

# Final_Version
<img src = "https://github.com/Pweder3/SMORT/blob/main/Documentation/Images/Images/launch6.gif" width = 800>


## Reflection


### Cyrus's Reflection
#### Overall Reflection

While we were ultimately successful in our goal of achieving a stable launch and collecting data we failed to meet the other goals that we had ambitiously created at the start of the year. The project was initially  supposed to use the data that we collected to make predictions of the angle we would need to launch a certain distance. I think that the shell would have been able to give us a consistent speed but I don't think that we could've figured out what that speed was just based on the sensor data. The code that the sensors use is unreliable and without filtering the data is unusable. 

#### Why Rocket Propulsion Failed
Originally we planned on using rocket motors as our main method of propulsion we used OpenRocket to give us range predictions and tell us what size motor we could use. OpenRocket was very helpful because it gave us charts that showed us lots of data and it also helped refine the fin design with its stability predictions. We attempted to get the RP to work for about 2 months and 4 launch attempts before we switched to air propulsion. Originally we planned to get the shell stable in the air cannon and then transition back to rocket motors but we decided against this because there was no need to with the performance we got from the air cannon. One of the biggest reasons that the rocket motors failed was that we were treating them as less fragile than they were. Rocket motors and igniters are finicky when you are using them for their intended purpose but when you are trying to drop them onto a plate and get them to ignite they are rarely going to perform in the way you'd want. I created 3 different methods to get the igniters to work, when I tested them in the lab they were capable of setting off LED lights but when we went outside for a real test they failed to perform. Even when we decided to do a non-drop launch we still had trouble getting the ignition working. When we did get a motor to ignite the rocket didn't leave the barrel. After that, we decided to change our propulsion method. If we had done this from the start of the project we would've been able to do much more CAD work and possibly give Paul more help with his code/wiring.

#### What Would I Change

### Lucia's Reflection



### Paul's Reflection
