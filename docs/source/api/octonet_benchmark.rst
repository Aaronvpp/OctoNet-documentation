OctoNet Benchmark
=================

.. automodule:: octonet.Octonet
    :members:
    :undoc-members:
    :show-inheritance:

Getting Started
===============

Configuration
-------------

OctoNet uses a dictionary configuration to filter data.

.. code-block:: python

    config = {
        'exp_list': [1], 
        'activity_list': ['dance'], 
        'node_id': [1, 2, 3, 4, 5], 
        'segmentation_flag': True,
        'modality': ['mmWave', 'mocap']
    }


Loading Data
-------------

Use the ``get_dataset`` API to load specific subsets:

.. code-block:: python

    from dataset_loader import get_dataset, get_dataloader

    dataset = get_dataset(config, dataset_path="./dataset")
    dataloader = get_dataloader(dataset, batch_size=1)

Dataset Structure
-----------------

After extraction, your directory should look like this:

.. code-block:: text

    ./dataset
    ├── mocap_csv_final # Final motion capture data (CSV)
    ├── mocap_pose      # Final motion capture data (npy)
    ├── node_1          # Multi-modal sensor node 1
    ...

name: Deploy Sphinx Documentation

on:
  push:
    branches:
      - main  # 确保这里是你存放代码的主分支名称 (main 或 master)

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
          
      - name: Install dependencies
        run: |
          pip install -r docs/requirements.txt
          # 确保安装你的代码包所需的依赖，以便 autodoc 能工作
          pip install pandas numpy scipy pyyaml
          
      - name: Build HTML
        run: |
          cd docs
          make html
          
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: docs/build/html

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4