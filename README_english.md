# OpenMV-Autonomous-Vision

This repository contains the code, documentation, and resources for a visual processing system designed to support an autonomous intelligent car. The system utilizes the OpenMV H7 Plus module to perform real-time object detection and classification, helping the car identify objects like directional arrows, traffic lights, obstacles, and stop lines. This enables autonomous navigation in a controlled environment, making this project an important contribution to the field of autonomous vehicles.

## Key Features

- **Arrow Detection**: Recognizes directional arrows on the road to guide the car at intersections.
- **Traffic Light Recognition**: Identifies traffic lights and their colors to control the car’s movement.
- **Pedestrian and Obstacle Detection**: Detects pedestrians, dogs, and other obstacles, helping avoid potential collisions.
- **Door and Stop Line Detection**: Detects specific objects like doors and stop lines for controlled stopping and navigation adjustments.
- **Real-time Processing**: Optimized for low-latency detection, making the system suitable for embedded applications.

## Usage

1. Connect the OpenMV module to the main controller (e.g., a microcontroller or microprocessor) via UART to enable communication.
2. Power up the system, and the module will automatically start detecting objects as the car navigates its path.
3. As objects are detected, the OpenMV module sends corresponding data (e.g., object type and location) to the main controller for navigation and decision-making.

The system is designed to operate autonomously, adjusting its actions based on the objects it detects in real time.

## Project Structure

- `main.py`: The primary script that coordinates the detection processes and integrates the detection algorithms.
- `templates/`: Contains image templates used for object detection through template matching (e.g., arrow and obstacle shapes).
- `models/`: Pre-trained neural network models, specifically MobileNetV2, stored here for more complex object detection tasks, such as pedestrian and dog detection.

## Troubleshooting

If you encounter issues with the module or detection accuracy, consider the following:

- **Check Template and Model Load**: Ensure templates and models are correctly loaded into memory. You may need to reduce memory usage by unloading unnecessary templates.
- **Adjust Detection Thresholds**: Fine-tune thresholds for template matching and color blob recognition in OpenMV IDE to improve detection accuracy.
- **Update Firmware**: Ensure your OpenMV H7 Plus is running the latest firmware to benefit from performance improvements and bug fixes.
