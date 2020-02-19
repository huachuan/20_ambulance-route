# Project work distribution & timeline
Huachuan Wang, Cuidi Wei, Andrew Nguyen

## Brief project description
While emergency vehicles speed up to save lives, they put themselves in a dangerous condition. We plan to develop a smart traffic light system to guarantee the safety of the emergency vehicles.   

## Components breakdown

### Sensor
*Camera*. A camera is to detect of motion of the emergency vehicles.

*Sound detector*. A sound detector is able to perform detection of siren sounds. 

### Computing capabilities
*Raspberry Pi*. A raspberry pi is connected to wifi, it receive the data from camera and sound detector and send the information to the cloud. 

*Cloud*. The cloud process the infromation recived from the raspberry pi. The sound and image information is processed and the cloud generate instructions to the rasberry pi accordingly. 

### Actuator
*Traffic lights*. The cloud sends instructions to raspberry pi. Raspberry pi controls the traffic light depending on the cloud instructions. The traffic light can be turned on, off or flashing.

### Connections
The camera, sound detector and traffic lights are conncected to the raspberry pi. A raspberry pi is connected to the wifi and cloud.

### Interfaces

*Tensorflow* for image processing.

*Siren detection API*

*Cloud connection API*


|          | Timeline                                                    |
|----------|-------------------------------------------------------------|
|2.13-2.20 |Planning with logistics and specifications in order to provide sufficient and efficient properties |
|          |Proper work distribution                                     |
|2.20      |Checkpoint 1|
|2.20-2.27 |Proceed work with constructive criticism and recommendations|
||Allocate proper costs and necessities for the Project|
||Meet with Gabe for logistic and feedback|
|2.20-2.27|Proceed work with constructive criticism and recommendations|
||Allocate proper costs and necessities for the Project|
||Meet with Gabe for logistic and feedback|
|2.27-3.6|Continue working along with applying the sound detection along with the light|
||Plan to meet with Gabe for finalization check ins|
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
||Plan to meet with Gabe for final check ins|
|4.21-4.23|Final presentations and Demo|
