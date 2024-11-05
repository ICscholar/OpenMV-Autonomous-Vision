# Detailed description of this vision project with OPENMV H7Plus is in "README_chinese.md" and "README_english.md". In this part, some of the results would be displayed.
## The openmvH7 plus camera is used in our intelligent car as shown below:
<div align="center">
    <img src="https://raw.githubusercontent.com/ICscholar/OpenMV-Autonomous-Vision/main/images%20for%20README/system_link.png" alt="System Link Diagram" width="300"/>
</div>

## The flowchart of the detecting process and logic running of the main.py
<div align="center">
    <img src="https://raw.githubusercontent.com/ICscholar/OpenMV-Autonomous-Vision/main/images%20for%20README/flowchart.png" alt="Flowchart" width="300"/>
</div>

## Small trick in traffic light detection task: 
First step: use template matching to find the area of the whole traffic light in the environment. 
Second Step: use color detection to detect the expected color in the target area from first step. 
<div align="center">
    <img src="https://github.com/ICscholar/OpenMV-Autonomous-Vision/blob/main/images%20for%20README/traffic_light_detect.png" alt="Flowchart" width="600"/>
</div>
 
