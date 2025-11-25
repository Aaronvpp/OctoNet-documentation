# Installation

## Prerequisites

- Linux (tested on Ubuntu 20.04)
- Python 3.9+
- Conda

## Environment Setup

Create the conda environment using the provided yaml file:

```bash
conda env create -f environment.yaml
conda activate octonet
```

## Download Dataset

Use the automated script to download and extract the dataset:

```bash
bash download_octonet.sh
```