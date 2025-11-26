Welcome to OctoNet's documentation!
===================================

# Installation

This guide walks you through setting up the OctoNet environment and downloading the dataset.

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Ubuntu 18.04+ | Ubuntu 20.04/22.04 |
| **Python** | 3.9 | 3.9 - 3.11 |
| **RAM** | 16 GB | 32 GB+ |
| **Storage** | 1.5 TB free | 2 TB+ SSD |
| **GPU** | Optional | NVIDIA GPU with CUDA 11.x |

```{warning}
The full dataset is approximately **768 GB**. During download and extraction, you may need up to **1.5 TB** of free disk space temporarily.
```

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/aiot-lab/OctoNet.git
cd OctoNet
```

---

## Step 2: Set Up the Environment

We recommend using Conda to manage dependencies.

### Option A: Using Conda (Recommended)

```bash
# Create the OctoNet environment from the provided specification
conda env create -f environment.yaml

# Activate the environment
conda activate octonet

# Install additional Python packages
pip install -r requirements.txt
```

### Option B: Using pip

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Verify Installation

```python
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
```

---

## Step 3: Download the Dataset

The OctoNet dataset is hosted on [Hugging Face](https://huggingface.co/datasets/hku-aiot/OctoNet).

### Automated Download (Recommended)

We provide a one-command script that handles downloading, merging, and extraction automatically:

```bash
bash -c "$(wget -qO- https://huggingface.co/datasets/hku-aiot/OctoNet/resolve/main/download_octonet.sh)"
```

```{note}
The script supports **resume on interruption** using `wget -c`. If your download is interrupted, simply re-run the same command.
```

### What the Script Does

1. **Downloads** 16 chunks (~48 GB each) from Hugging Face
2. **Merges** all chunks into `octonet.tar`
3. **Cleans up** temporary chunk files to save space
4. **Extracts** the final dataset


## Step 4: Verify Dataset Structure

After extraction, verify your directory structure:

```text
./dataset
├── mocap_csv_final/     # Motion capture data (CSV format)
├── mocap_pose/          # Motion capture data (NumPy .npy format)
├── node_1/              # Multi-modal sensor node 1
├── node_2/              # Multi-modal sensor node 2
├── node_3/              # Multi-modal sensor node 3
├── node_4/              # Multi-modal sensor node 4
├── node_5/              # Multi-modal sensor node 5
├── imu/                 # Inertial measurement unit data (.pickle)
├── vayyar_pickle/       # Vayyar mmWave radar data (.pickle)
└── cut_manual.csv       # Manually curated data segments
```

Run the verification script:

```bash
python -c "
import os
expected_dirs = ['mocap_csv_final', 'mocap_pose', 'node_1', 'node_2', 
                 'node_3', 'node_4', 'node_5', 'imu', 'vayyar_pickle']
dataset_path = './dataset'
for d in expected_dirs:
    path = os.path.join(dataset_path, d)
    status = '✓' if os.path.exists(path) else '✗'
    print(f'{status} {d}')
"
```

---

## Troubleshooting

### Download Issues

| Problem | Solution |
|---------|----------|
| Download interrupted | Re-run the script; it will resume automatically |
| Slow download speed | Use a VPN or try during off-peak hours |
| Checksum mismatch | Delete the corrupted chunk and re-download |

### Environment Issues

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| CUDA not found | Install CUDA toolkit or use CPU-only mode |
| Conda env fails | Try `conda update conda` first |

---

