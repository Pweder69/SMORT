

# S.M.O.R.T. abstract
The goal of this project is to create a launch system for a rocket of our design were we can target the rocket to land in a predetermined area. Using a rasbery pi to collect information and adjust our drag calculation.


## Rocket Design
The rocket is designed to be modular and easy to print as to enable us to iterate as fast as possible. Each part being modular will allow us to fix problems easily and for example change the rocket motor or even alter the mode of propulsuon all together.



### Launch System
The launch system has several possible designs. The main mode used right now is a rocket and all designs revolve around that system. The diffrent ideas of launch systems are as follows:


- external 9v to power an interal launcher 
<img src="Images/Diagrams/Launch diagram.png" width =200>

- Heated resisistor to ignite rocket motor
- primers


### Body
The body isnt really compicated it just contains all of the electronics and potentialy fins. It should eaither be threaded or use a pin to connect to the nose cone 


## Nose Cone
The nose cone is a part that will be deisgned to absorbe all of the shock it will contain a spring and a pin that will absorbe the brunt of the landing shock. (it will not be filled with any explosive compound). 

<img src= "Images/Diagrams/Untitled-2023-11-28-1409.png" width = 300> 


## Targeting System
The targeting system will just control the angle of the launch tube relative to the ground eaither using a threaded rod or other method. If the project completes early you can also add a rotation system to the rocket to control the direction of the rocket.

## Risk Mitigation
The printable document for our risk mitigations is linked [here](https://docs.google.com/document/d/1zc1QNFviahBiOCXemDb18Xyl-Bo_QezTwZ_n9gg8yH8/edit#heading=h.g7bat7v5y0lc).
### Concerns
The rocket might accidentally interference with humans during a launch.
Shorting electronics.

### Mitigations
* Before Launch find the wind direction and fire in the direction of the wind so they shell wont come back towards us.
* Make sure any spectators are clear of the landing area and there are no objects that shouldn't be destroyed down range.
* The rocket stand is also engineered to have a max angle of 75 degrees to ensure the rocket will not fire straight up, considering we do not have a parachute that will deploy.
  
LAUNCH STEPS
* Step 1) Safety glasses and ear protection
* Step 2) Make sure all members in the launch group understand what their role is
* Step 3) Arm Tube and make sure tone is on
* Step 4) Drop The Shell down the tube
* Step 5) Wait for ignition and cover head
* Step 6a) If launch is successfull disarm tube and inspect the landing area
* Step 6b) If launch is unsuccessfull disarm tube and slowly dump the shell out the front





# Schedule

## End of January 
- [x] Finish the rocket design
- [x] First Shell printed 
- [ ] Interal Wiring prototype done.
- [ ] Rocket code done (just data collection)

## Mid February
- [ ] First Launch without lanucher to collect data 
- [ ] Final Rocket design done
- [ ] beginig of lanucher iteration and code
- [ ] 

## End of February
- [ ] First Launch with lanucher
- [ ] Fix issues with rocket
- [ ] rocket to work issueless and consistently

## May 
- [ ] Accurate targeting system
- [ ] Final Launch
- [ ] finish documentation



# Materials 


## Shell
- Nose cone
- Impact Spring
- Stabilization fins
- Ignition Pins
- Ignighter
- 2 Picos and other onboard electronics
- Rocket motor (A,B,C)

## Tube + Targeting 

- 4in/101.6mm PVC pipe
- Pipe end cap
- Blast Plate/Rotation Plate (1m x 1m minimum size)
- rotation motor (stepper)
- rotation bearing
- rotation gears
- Angle legs (metal/wood a frame)
- Angle motor (stepper 1 or 2)
- Angle gears

## Launcher

- 12 Volt battery
- Conductor plates
- Saftey Switch
-
-
-

# Code blocks
<img src = "https://github.com/Pweder69/SMORT/blob/main/docs/Images/Diagrams/Code%20diagram%201.png" width=300>

---

<img src = "https://github.com/Pweder69/SMORT/blob/main/docs/Images/Diagrams/Diagram%202.png" width=300>
