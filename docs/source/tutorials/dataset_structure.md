# Dataset Structure

This page provides a comprehensive overview of the OctoNet dataset organization, metadata, and file formats.

## Overview

OctoNet is a large-scale multi-modal dataset containing synchronized data from **12 different sensor modalities** across **5 distributed sensor nodes**.

---

## Directory Layout

```text
./dataset
├── mocap_csv_final/          # Ground-truth motion capture (CSV)
├── mocap_pose/               # Ground-truth motion capture (NumPy)
├── node_1/                   # Sensor node 1
│   ├── acoustic/             # Ultrasonic audio
│   ├── depthCamera/          # RGB-D camera frames
│   ├── mmWave/               # FMCW mmWave radar
│   ├── seekThermal/          # Thermal camera
│   ├── ToF/                  # Time-of-Flight sensor
│   ├── IRA/                  # Infrared array sensor
│   ├── uwb/                  # Ultra-wideband radar
│   ├── wifi/                 # WiFi CSI data
│   └── polar/                # Polar heart rate sensor
├── node_2/                   # Sensor node 2
│   └── ...
├── node_3/                   # Sensor node 3
│   └── ...
├── node_4/                   # Sensor node 4
│   └── ...
├── node_5/                   # Sensor node 5
│   └── ...
├── imu/                      # Wearable IMU sensors
├── vayyar_pickle/            # SFCW Vayyar mmWave radar
└── cut_manual.csv            # Activity segmentation metadata
```

---

## Sensor Modalities

OctoNet includes **12 sensor modalities** for comprehensive human activity capture:

| Modality | Key | Location | Format | Description |
|----------|-----|----------|--------|-------------|
| **Motion Capture** | `mocap` | `mocap_csv_final/` | CSV | Ground-truth 3D skeleton poses from OptiTrack |
| **RGB-D Camera** | `depthCamera` | `node_*/depthCamera/` | MP4/PNG | RGB video and depth images from Intel RealSense |
| **FMCW Radar** | `mmWave` | `node_*/mmWave/` | Pickle | Point cloud from TI mmWave sensors |
| **Acoustic** | `acoustic` | `node_*/acoustic/` | WAV | Ultrasonic audio signals |
| **Thermal Camera** | `seekThermal` | `node_*/seekThermal/` | PNG | Thermal imaging from Seek Thermal |
| **Time-of-Flight** | `ToF` | `node_*/ToF/` | Pickle | ToF depth measurements |
| **Infrared Array** | `IRA` | `node_*/IRA/` | Pickle | Low-resolution thermal array (8x8) |
| **UWB Radar** | `uwb` | `node_*/uwb/` | Pickle | Ultra-wideband radar signals |
| **WiFi CSI** | `wifi` | `node_*/wifi/` | Pickle | Channel State Information |
| **IMU** | `imu` | `imu/` | Pickle | 6-axis inertial measurements (accelerometer + gyroscope) |
| **SFCW Radar** | `vayyar` | `vayyar_pickle/` | Pickle | Vayyar high-resolution mmWave imaging |
| **Polar HR** | `polar` | `node_*/polar/` | Pickle | Heart rate data from Polar sensor |

### Modality Path Summary

Each modality follows a consistent path structure:

| Modality | Path Pattern |
|----------|-------------|
| **IRA** | `node_{1-5}/IRA/data/{timestamp}_node_{id}_modality_ira_subject_{user}_activity_{act}_trial_{n}.pickle` |
| **UWB** | `node_{1-5}/uwb/data/{timestamp}_node_{id}_modality_uwb_subject_{user}_activity_{act}_trial_{n}.pickle` |
| **WiFi** | `node_{1-5}/wifi/exp-{timestamp}_node_{id}_modality_wifi_subject_{user}_activity_{act}_trial_{n}/{filename}.pickle` |
| **mmWave** | `node_{1-5}/mmWave/data/{timestamp}_node_{id}_modality_mmwave_subject_{user}_activity_{act}_trial_{n}.pickle` |
| **Polar** | `node_{1-5}/polar/data/{timestamp}_node_{id}_modality_heartrate_subject_{user}_activity_{act}_trial_{n}.pickle` |
| **ToF** | `node_{1-5}/ToF/data/{timestamp}_node_{id}_modality_ToF_subject_{user}_activity_{act}_trial_{n}.pickle` |
| **Acoustic** | `node_{1-5}/acoustic/data/{timestamp}_node_{id}_modality_acoustic_subject_{user}_activity_{act}_trial_{n}/{filename}.wav` |
| **Thermal** | `node_{1-5}/seekThermal/data/{timestamp}_node_{id}_modality_seekthermal_subject_{user}_activity_{act}_trial_{n}/` |
| **Depth Camera** | `node_{1-5}/depthCamera/data/{timestamp}_node_{id}_modality_depthcam_subject_{user}_activity_{act}_trial_{n}/` |
| **Vayyar** | `vayyar_pickle/{timestamp}_node_1_modality_vayyarmmwave_subject_{user}_activity_{act}_trial_{n}.pickle` |
| **MoCap** | `mocap_csv_final/mocap_S{scene}/{name}/Take {datetime}_subject_{user}.csv` |
| **IMU** | `imu/{timestamp}_node_1_modality_imu.pickle` |

---

## Dataset Metadata & Statistics

### Participant Information

OctoNet includes **41 participants** with diverse demographics:

| User (Gender) | Exp ID | Scene 1: Activity IDs | Scene 1: PA&F | Scene 2: Activity IDs | Scene 2: PA&F | Scene 3: Activity IDs | Scene 3: PA&F |
|---------------|--------|:---------------------:|:-------------:|:---------------------:|:-------------:|:---------------------:|:-------------:|
| 1 (M) | 1, 11, 101, 201 | all 62 | ✓ | 1–23 | | 1–23, 57–62 | ✓* |
| 2 (M) | 2, 12, 102, 112, 202 | all 62 | ✓ | 9–29 | ✓ | 9–29 | |
| 3 (M) | 3, 13, 113, 213 | all 62 | ✓ | | ✓ | | ✓ |
| 4 (F) | 4, 14, 104, 114, 204 | all 62 | ✓ | 30–56 | ✓ | 30–56 | |
| 5 (M) | 5, 15, 115, 215 | all 62 | ✓ | | ✓ | | ✓ |
| 6 (F) | 6, 16 | all 62 | ✓ | | | | |
| 7 (M) | 7, 17, 117, 217 | all 62 | ✓ | | ✓ | | ✓ |
| 8 (M) | 8, 18, 108, 118 | all 62 | ✓ | 24–62 | ✓ | 24–62 | |
| 9 (M) | 9 | all 62 | | | | | |
| 10 (M) | 10, 20, 120, 220 | all 62 | ✓ | | ✓ | | ✓ |

```{note}
**Legend:**
- **Gender:** Male (M) and Female (F) participants
- **PA&F:** Programmed Aerobics and Freestyle activities
- **Asterisk (*):** Subjects who performed only Programmed Aerobics (no Freestyle)
- **Scene Mapping:** Scene 1: IDs 1-99, Scene 2: IDs 101-199, Scene 3: IDs 201-299
```

### Activity Classes

OctoNet supports **62 fine-grained activities**. 
The additional labels **"gym" and "freestyle"** correspond to programmed aerobics and freestyle motions described in the paper.

```python
ACTIVITIES = [
    'sit', 'walk', 'bow', 'sleep', 'dance', 'jog', 'falldown', 'jump', 
    'jumpingjack', 'thumbup', 'squat', 'lunge', 'turn', 'pushup', 'legraise', 
    'airdrum', 'boxing', 'shakehead', 'answerphone', 'eat', 'drink', 'wipeface', 
    'pickup', 'jumprope', 'moppingfloor', 'brushhair', 'bicepcurl', 'playphone', 
    'brushteeth', 'type', 'makeoksign', 'makevictorysign', 'drawcircleclockwise', 
    'drawcirclecounterclockwise', 'stopsign', 'pullhandin', 'pushhandaway', 
    'handwave', 'sweep', 'clap', 'slide', 'drawzigzag', 'dodge', 'bowling', 
    'liftupahand', 'tap', 'spreadandpinch', 'drawtriangle', 'sneeze', 'cough', 
    'stagger', 'yawn', 'blownose', 'stretchoneself', 'touchface', 'handshake', 
    'hug', 'pushsomeone', 'kicksomeone', 'punchsomeone', 'conversation', 
    'gym', 'freestyle'
]
```

---

## Metadata File: `cut_manual.csv`

This CSV file contains all data paths and manual activity segmentation information. Each row represents one recording session.

### Column Descriptions

#### Basic Information

| Column | Type | Description |
|--------|------|-------------|
| `user_id` | int | Participant ID (1-41) |
| `activity` | string | Activity label (e.g., 'sit', 'walk', 'dance') |
| `recording_time` | string | Recording timestamp (e.g., '2024/5/18 13:43') |
| `start_time` | string | Recording start time within the session (e.g., '43:59.3') |

#### Sensor Data Paths

Each sensor modality has corresponding path columns for each node:

| Column Pattern | Description |
|----------------|-------------|
| `node_{1-5}_IRA_data_path` | Path to Infrared Array sensor data |
| `node_{1-5}_uwb_data_path` | Path to Ultra-Wideband radar data |
| `node_{1-5}_wifi_data_path` | Path to WiFi CSI data |
| `node_{1-5}_mmWave_data_path` | Path to FMCW mmWave radar data |
| `node_{1-5}_polar_data_path` | Path to Polar heart rate data |
| `node_{1-5}_ToF_data_path` | Path to Time-of-Flight sensor data |
| `node_{1-5}_acoustic_data_path` | Path to ultrasonic audio data |
| `node_{1-5}_seekThermal_data_path` | Path to thermal camera data |
| `node_{1-5}_depthCamera_data_path` | Path to RGB-D camera data |
| `node_{1-5}_vayyar_data_path` | Path to Vayyar radar data (only on node_1) |
| `mocap_data_path` | Path to motion capture CSV file |
| `imu_data_path` | Path to IMU sensor data |

```{note}
**Empty cells** indicate that the sensor was not available or not recording during that session. Not all nodes have all sensors deployed.
```

#### Manual Segmentation Columns

These columns contain **manual segmentation information** for repeated activity trials, derived from motion capture data analysis:

| Column | Type | Description |
|--------|------|-------------|
| `cut_points` | list[int] | Frame indices where activity repetitions are segmented |
| `cut_ratio` | list[float] | Normalized position (0.0-1.0) of each cut point within the recording |
| `cut_timestamps` | list[string] | Exact timestamps for each segmentation point |

```{important}
**Manual Segmentation:** During data collection, participants repeated the same activity multiple times in a single recording. The `cut_timestamps` column provides manually annotated timestamps (derived from motion capture analysis) to segment these repetitions into individual activity instances.
```

### Example Row Interpretation

```text
user_id: 2
activity: sit
cut_points: [429, 1476, 2631, 3835, 5000, 6056, 7231, 8287, 9363, 10203]
cut_timestamps: ['2024-05-18 13.44.02.848', '2024-05-18 13.44.11.573', ...]
```

This means:
- **User 2** performed the **"sit"** activity
- The recording contains **9 repetitions** of the sitting activity
- Each timestamp in `cut_timestamps` marks the boundary between consecutive repetitions
- These boundaries were manually annotated using the motion capture data as ground truth

---

## Data Availability by Node

Not all modalities are available on every node. Here's the sensor deployment:

| Modality | Node 1 | Node 2 | Node 3 | Node 4 | Node 5 |
|----------|:------:|:------:|:------:|:------:|:------:|
| IRA | ✓ | ✓ | ✓ | ✓ | ✓ |
| UWB | ✓ | | | | |
| WiFi | ✓ | ✓ | ✓ | ✓ | |
| mmWave | ✓ | ✓ | ✓ | ✓ | ✓ |
| Polar | ✓ | | | | |
| ToF | | | | ✓ | |
| Acoustic | ✓ | | | ✓ | |
| Thermal | ✓ | | ✓ | | |
| Depth Camera | ✓ | | ✓ | | ✓ |
| Vayyar | | | ✓* | | |

```{note}
**Vayyar Radar Naming Convention:** Although the Vayyar radar is physically placed at **Node 3's location**, the file paths are named with `node_1` prefix (e.g., `vayyar_pickle/{timestamp}_node_1_modality_vayyarmmwave_...`). This is a naming convention from data collection and does not reflect the actual sensor placement. The Vayyar radar captures data from Node 3's perspective.
```

---

