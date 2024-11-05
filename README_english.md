# OpenMV-Autonomous-Vision

This repository contains the code and documentation for a visual processing system designed to support an autonomous intelligent car. The system utilizes the OpenMV H7 Plus module to perform real-time object detection and classification, helping the car identify objects like arrows, traffic lights, obstacles, and stop lines, enabling autonomous navigation.

## Project Overview

This project is part of the 'TDPS'(Team Design Project and Skills in our college) initiative, aimed at developing a reliable, real-time visual processing system for autonomous navigation in simulated environments. The primary functions of the system include detecting various objects and providing navigation guidance to the car’s main controller, enabling it to make accurate driving decisions based on the environment.

## Key Features

- **Arrow Detection**: Recognizes directional arrows on the road to guide the car at intersections.
- **Traffic Light Recognition**: Identifies traffic lights and their colors, controlling the car’s movement accordingly.
- **Pedestrian and Obstacle Detection**: Detects pedestrians, dogs, and other obstacles to avoid potential collisions.
- **Door and Stop Line Detection**: Detects specific objects like doors and stop lines for controlled stopping and navigation adjustments.
- **Real-time Processing**: Achieves low-latency detection using efficient algorithms suitable for embedded systems.

## Technologies Used

- **OpenMV H7 Plus**: A machine vision module based on ARM Cortex M7, suitable for real-time visual processing.
- **Template Matching**: Used for basic object detection tasks such as arrow and obstacle detection.
- **Color Blob Recognition**: Employed to recognize specific colors, particularly useful for traffic light recognition.
- **Neural Networks (MobileNetV2)**: Leverages a lightweight neural network model, achieving efficient object recognition on limited computational resources.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/ICscholar/OpenMV-Autonomous-Vision.git
