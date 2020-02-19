# Project work distribution & timeline
Huachuan Wang, Cuidi Wei, Andrew Nguyen

## Brief project description
While emergency vehicles speed up to save lives, they put themselves in a dangerous condition. We plan to develop a smart traffic light system to guarantee the safety of the emergency vehicles. When emergency vehicles will pass a crossroad, the sensors of traffic light will know and send the message to cloud so that cloud will control the traffic lights in order to let emergency vehicles to pass the traffic light in higher speed.

## Components breakdown

### Sensor
*Camera*. A camera is to detect the motion of the emergency vehicles.

*Sound detector*. A sound detector is able to perform detection of siren sounds. 

### Computing capabilities
*Raspberry Pi*. A raspberry pi is connected to wifi, it receives the data from camera and sound detector and sends the information to the cloud. 

*Cloud*. The cloud processes the information received from the raspberry pi. The sound and image information is processed and the cloud generates instructions to the rasberry pi accordingly. 

### Actuator
*Traffic lights*. The cloud sends instructions to raspberry pi. Raspberry pi controls the traffic light depending on the cloud instructions. The traffic light can be turned on, off or flashing.

### Connections
The camera, sound detector and traffic lights are conncected to the raspberry pi. A raspberry pi is connected to the wifi and cloud.

### Interfaces
*Sound Detection*
Monitor the ambulance's sound and notify the camera to detect whether an ambulance is in the road.

*Image Processing*
Check if an ambulance is in a picture so that it will know whether an ambulance is in the current road. In this module, Tensorflow is used and the helpful code is in the code directory.

*Computing I: Check ambulance's moving direction*
When an ambulance rings, the nearby sound sensors will detect. So we need to check the ambulance's moving direction in order to only change the traffic lights to green in its direction. Some helpful code is in the Tensorflow module.

*Computing II: Identify ambulance's sound*
A sound sensor will receive many many various sounds, so the Siren Detection API is important to check if it is ambulance's sound. The helpful code is also attached in the code directory.

*Computing III: Control Traffic lights*
In the road, there are only traffic lights which an ambulance will pass to get the front pictures of the ambulance. So the traffic light that detects the existence of an ambulance will send messages to the cloud. After getting the message from the traffic lights, the cloud will control the other traffic light in the crossroad to red to guarantee that other cars will make a way for the ambulance. The code will be developed by us later.

### Security
Security often focusses on the very interesting vulnerabilities and exploits, but there is usually less focus on common misconfigurations or bad implementations. A misconfiguration such as a simple or default password, an insecure API or a badly implemented and unpatched hypervisor can also lead to a security compromise. The best method to deal with these misconfigurations is to have proper Change Control systems in place, to include Security experts in the review panel and to have solid, secure configuration standards in place. But in our environment, it's efficient for us to configure correctly and prevent from attacks due to the misconfigurations.
DDos attacks will crash the cloud to prevent the cloud from working normally. Therefore, it is important to prevent DDoS attacks for the cloud to make sure the traffic lights can work normally. To achieve this, setting up specific rules to filter out illegal attacks is a necessary step. 


|          | Timeline                                                    |
|----------|-------------------------------------------------------------|
|2.13-2.20 |Planning with logistics and specifications in order to provide sufficient and efficient properties |
|          |Proper work distribution                                     |
|2.20      |Checkpoint 1|
|2.20-2.27 |Proceed work with constructive criticism and recommendations|
||Allocate proper costs and necessities for the Project|
|2.20-2.27|Proceed work with constructive criticism and recommendations|
||Allocate proper costs and necessities for the Project|
|2.27-3.6|Continue working along with applying the sound detection along with the light|
||Camera Should have substantial progress|
|3.6-3.24|Cloud Control should be working to some degree|
||Majority of Components should be working together|
||Sound and Traffic Light should have substantial progress|
|3.24|Checkpoint 2|
|3.24-3.31|Continue working with the criticism and feedback|
||Camera, Light, and Sound should be completed|
||Cloud Control should have progress|
||Ensurance that everything is running smoothly|
|3.31-4.20|Work on presentations and write-ups|
||Finalizations & debuggings on the design/project|
|4.21-4.23|Final presentations and Demo|
