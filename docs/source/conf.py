# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'OctoNet'
copyright = '2024, HKU AIoT Lab'
author = 'HKU AIoT Lab'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',     # 支持 Google/NumPy 风格的 docstrings
    'sphinx.ext.viewcode',     # 添加源码链接
    'myst_parser',             # 支持 Markdown (.md) 文件
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

import os
import sys

# --- Path Setup ---
# 指向 OctoNet_code 目录，以便 autodoc 可以找到 dataset_loader.py 等文件
sys.path.insert(0, os.path.abspath('../../OctoNet_code'))
# 如果需要引用 OctonetBenchmark 下的模块
sys.path.insert(0, os.path.abspath('../../OctoNet_code/OctonetBenchmark'))
