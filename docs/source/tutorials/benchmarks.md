# Benchmarks

This guide covers running reproducible benchmarks for Human Activity Recognition (HAR) and Human Pose Estimation (HPE) on the OctoNet dataset.

## Environment Setup

### Step 1: Navigate to Benchmark Directory

```bash
cd OctonetBenchmark
```

### Step 2: Create Conda Environment

```bash
# Create the benchmark environment
conda env create -f environment.yml

# Activate the environment
conda activate octo

# (Optional) Update existing environment
conda env update -f environment.yml --prune
```

```{note}
**GPU Support:** The `environment.yml` includes GPU-enabled PyTorch and CUDA libraries. For CPU-only setups, remove CUDA-related packages (`pytorch-cuda`, `cudnn`, `cuda-*`) and the `nvidia` channel.
```

---

## Dataset Preparation

### Step 1: Rename Dataset Directory

Rename the dataset directory to `octonet` and place it in the benchmark folder:

```text
./octonet
├── mocap_csv_final/
├── mocap_pose/
├── node_1/
├── node_2/
├── node_3/
├── node_4/
├── node_5/
├── imu/
├── vayyar_pickle/
├── Octonet.py          # Dataset loader script
└── cut_manual.csv
```

```{warning}
**Folder Naming:** The folder name must be exactly `octonet` as the code imports via `from octonet.Octonet import get_dataset, custom_collate`.
```

---

## Running Benchmarks

### Training + Testing (Full Pipeline)

```bash
python main.py --config_file acoustic_densenet121_10 --cuda_index 0 --mode 0
```

### Testing Only (Pre-trained Model)

```bash
python main.py --config_file acoustic_densenet121_10 --cuda_index 0 --mode 1 --pretrained_model /path/to/weights.pth
```

### Fine-tuning + Testing

```bash
python main.py --config_file ira_rf_net_pose --cuda_index 0 --mode 2 --pretrained_model /path/to/weights.pth
```

### Command Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--config_file` | Configuration file name (without `.yaml`) | `acoustic_densenet121_10` |
| `--cuda_index` | GPU device index | `0` |
| `--mode` | 0=Train+Test, 1=Test only, 2=Finetune+Test | `0` |
| `--pretrained_model` | Path to pre-trained weights | `/path/to/model.pth` |

---

## Configuration Files

Configuration files are located in `Configurations/` folder:

```text
Configurations/
├── acoustic_densenet121_10.yaml
├── acoustic_densenet121_62.yaml
├── acoustic_resnet18_10_n.yaml
├── depthCamera_densenet121_10_n_1fps_mask_withoutnorm.yaml
├── imu_densenet121_10_n.yaml
├── mmWave_densenet121_10_n.yaml
├── wifi_densenet121_10.yaml
└── ...
```

### Saving Trained Models

To save model weights, modify your configuration file:

```yaml
model_save_enable: True  # Change from False to True
trained_model_folder: ./saved_models
log_folder: ./logs
tensorboard_folder: ./runs
```

---

## Benchmark Results

### Human Activity Recognition (HAR)

Results are reported as accuracy (%) with standard deviation. Format: `10-class / 62-class`

| Modality | Protocol | ResNet | DenseNet | Swin-T | RFNet |
|----------|----------|--------|----------|--------|-------|
| **RGB** | ID | 91.5 / 93.4 | 93.2 / 91.2 | 94.9 / 93.1 | 89.7 / 60.9 |
| | CU | 46.0 / 12.3 | 68.2 / 24.7 | 37.0 / 7.7 | 45.0 / 9.2 |
| | CS | 14.9 / 4.1 | 33.3 / 11.3 | 12.1 / 1.7 | 13.5 / 3.1 |
| **Depth** | ID | 89.7 / 86.6 | 90.6 / 83.2 | 86.3 / 81.7 | 87.2 / 40.0 |
| | CU | 41.2 / 11.1 | 64.9 / 27.3 | 46.0 / 14.4 | 45.0 / 11.2 |
| | CS | 17.7 / 3.9 | 22.7 / 12.2 | 23.4 / 4.3 | 28.4 / 4.8 |
| **IMU** | ID | 96.6 / 96.5 | 97.4 / 95.7 | 98.3 / 95.7 | 94.0 / 35.8 |
| | CU | 73.5 / 43.9 | 74.4 / 34.6 | 82.9 / 40.8 | 66.4 / 13.8 |
| | CS | 62.4 / 43.1 | 62.4 / 31.5 | 47.5 / 34.4 | 54.6 / 12.4 |
| **WiFi** | ID | 93.3 / 91.1 | 90.8 / 91.0 | 91.7 / 92.3 | 81.7 / 60.5 |
| | CU | 13.3 / 3.4 | 11.4 / 4.8 | 12.3 / 2.3 | 19.9 / 4.3 |
| | CS | 19.1 / 2.4 | 11.3 / 1.9 | 13.5 / 2.8 | 11.3 / 1.1 |
| **UWB** | ID | 98.3 / 93.8 | 88.4 / 80.1 | 100.0 / 90.4 | 94.2 / 75.8 |
| | CU | 62.6 / 21.5 | 59.7 / 27.4 | 17.1 / 2.7 | 64.5 / 13.5 |
| | CS | 27.0 / 6.7 | 20.6 / 6.3 | 21.3 / 2.4 | 12.1 / 1.7 |

**Protocol Legend:**
- **ID**: In-Distribution (same users in train/test)
- **CU**: Cross-User (different users in train/test)
- **CS**: Cross-Scene (different environments in train/test)

### Human Pose Estimation (HPE)

Results are reported as MPJPE (Mean Per Joint Position Error) in mm.

| Modality | Protocol | ResNet | DenseNet | Swin-T | RFNet |
|----------|----------|--------|----------|--------|-------|
| **RGB** | ID | 133.3 | 147.2 | 269.6 | 162.8 |
| | CU | 199.8 | 204.8 | 286.2 | 223.7 |
| | CS | 473.9 | 524.6 | 273.0 | 331.8 |
| **Depth** | ID | 131.4 | 147.4 | 248.2 | 194.8 |
| | CU | 197.1 | 212.5 | 256.2 | 230.7 |
| | CS | 363.6 | 436.4 | 305.1 | 444.2 |
| **IMU** | ID | 147.9 | 159.3 | 251.6 | 180.9 |
| | CU | 252.9 | 274.3 | 259.9 | 266.3 |
| | CS | 289.7 | 324.0 | 310.8 | 328.4 |

---

## Additional Resources

### Log Files

Download complete log files from SharePoint:

[Download Logs](https://connecthkuhk-my.sharepoint.com/:f:/g/personal/zhangxie_connect_hku_hk/EvArkmSXcqFFr_3wxC2JiJoB74qWYSvguqW0ejbE7w4XxQ?e=c9yhfE)

Place the `logs` folder in the same directory as `Configurations`.

---
