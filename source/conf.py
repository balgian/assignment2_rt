# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../first_part'))
sys.path.insert(0, os.path.abspath('../first_part/scripts'))
show_authors = True

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'first_part'
copyright = '2025, Gian Marco Balia'
author = 'Gian Marco Balia'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo'
]

# Mock ROS modules to avoid import errors
autodoc_mock_imports = [
    'rospy',
    'std_msgs',
    'geometry_msgs',
    'sensor_msgs',
    'first_part.srv',
    'actionlib',
    'first_part.msg',
    'nav_msgs',
    'assignment_2_2024.msg'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

highlight_language = 'python3'
source_suffix = '.rst'
master_doc = 'index'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_show_sourcelink = False

html_context = {
    "display_github": True,
    "github_user": "balgian",
    "github_repo": "assignment2_rt",
    "github_version": "ROS-Noetic",
    "conf_py_path": "/source/"
}