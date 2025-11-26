# Getting Started

This guide shows you how to load and work with the OctoNet dataset programmatically.

## Quick Start

```python
from dataset_loader import get_dataset, get_dataloader

# Define configuration
config = {
    'exp_list': [1],
    'activity_list': ['dance'],
    'node_id': [1, 2, 3, 4, 5],
    'segmentation_flag': True,
    'modality': ['mmWave', 'mocap', 'imu']
}

# Load dataset
dataset = get_dataset(config, dataset_path="./dataset")
dataloader = get_dataloader(dataset, batch_size=1, shuffle=False, config=config)

```

---

## Configuration Options

The configuration dictionary controls which data subsets to load:

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `exp_list` | list[int] | Experiment IDs to include | `[1, 2, 3]` |
| `activity_list` | list[str] | Activities to filter | `['walking', 'dance']` |
| `node_id` | list[int] | Sensor nodes (1-5) | `[1, 3, 5]` |
| `segmentation_flag` | bool | Use segmented clips | `True` |
| `modality` | list[str] | Data modalities to load | `['mmWave', 'mocap']` |
| `mocap_downsample_num` | int | Downsample mocap frames | `6` |

### Complete Configuration Template

```python
config = {
    'exp_list': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 
                 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
                 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 101, 102, 
                 104, 108, 111, 112, 113, 114, 115, 117, 118, 120, 121, 201, 202, 
                 204, 208, 211, 213, 215, 217, 220, 221, 230],
    'activity_list': ['sit', 'walk', 'bow', 'sleep', 'dance', 'jog', 'falldown', 
                      'jump', 'jumpingjack', 'thumbup', 'squat', 'lunge', 'turn', 
                      'pushup', 'legraise', 'airdrum', 'boxing', 'shakehead',
                      'answerphone', 'eat', 'drink', 'wipeface', 'pickup', 
                      'jumprope', 'moppingfloor', 'brushhair', 'bicepcurl', 
                      'playphone', 'brushteeth', 'type', 'makeoksign', 
                      'makevictorysign', 'drawcircleclockwise', 
                      'drawcirclecounterclockwise', 'stopsign', 'pullhandin',
                      'pushhandaway', 'handwave', 'sweep', 'clap', 'slide',
                      'drawzigzag', 'dodge', 'bowling', 'liftupahand', 'tap', 
                      'spreadandpinch', 'drawtriangle', 'sneeze', 'cough', 
                      'stagger', 'yawn', 'blownose', 'stretchoneself', 'touchface',
                      'handshake', 'hug', 'pushsomeone', 'kicksomeone', 
                      'punchsomeone', 'conversation', 'gym', 'freestyle'],
    'node_id': [1, 2, 3, 4, 5],
    'segmentation_flag': True,
    'modality': ['mmWave', 'IRA', 'uwb', 'ToF', 'polar', 'wifi', 'depthCamera', 
                 'seekThermal', 'acoustic', 'imu', 'vayyar', 'mocap']
}
```

### Available Modalities

```python
MODALITIES = [
    'mmWave',        # FMCW mmWave radar point cloud
    'mocap',         # Motion capture skeleton
    'imu',           # Inertial measurement unit
    'acoustic',      # Ultrasonic audio
    'depthCamera',   # RGB-D camera frames
    'vayyar',        # SFCW Vayyar radar imaging
    'seekThermal',   # Thermal camera
    'ToF',           # Time-of-Flight sensor
    'IRA',           # Infrared array
    'uwb',           # Ultra-wideband radar
    'wifi',          # WiFi CSI
    'polar'          # Polar heart rate
]
```

---

## Example: Loading Specific Subsets

### Motion Capture Only

```python
config = {
    'exp_list': [1],
    'activity_list': ['walk', 'run', 'jump'],
    'modality': ['mocap'],
    'segmentation_flag': True
}
dataset = get_dataset(config, dataset_path="./dataset")
```

### Single Node Multi-Modal

```python
config = {
    'exp_list': [1, 2],
    'activity_list': ['dance'],
    'node_id': [1],  # Only node 1
    'modality': ['mmWave', 'depthCamera', 'acoustic'],
    'segmentation_flag': True
}
dataset = get_dataset(config, dataset_path="./dataset")
```

### All Modalities for Specific Activity

```python
config = {
    'exp_list': [1],
    'activity_list': ['boxing'],
    'node_id': [1, 2, 3, 4, 5],
    'modality': ['mmWave', 'IRA', 'uwb', 'ToF', 'polar', 'wifi', 
                 'depthCamera', 'seekThermal', 'acoustic', 'imu', 
                 'vayyar', 'mocap'],
    'segmentation_flag': True
}
dataset = get_dataset(config, dataset_path="./dataset")
```

### With Mocap Downsampling

```python
config = {
    'exp_list': [1],
    'activity_list': ['dance'],
    'modality': ['mocap', 'depthCamera'],
    'segmentation_flag': True,
    'mocap_downsample_num': 6  # Downsample to 6 fps
}
dataset = get_dataset(config, dataset_path="./dataset")
```
