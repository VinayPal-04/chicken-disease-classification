import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "chicken_disease_classifier"

list_of_files = [
    ".github/workflows/.gitkeep", # To keep the GitHub workflows directory in version control
    f"src/{project_name}/__init__.py", # Initialize the package directory
    f"src/{project_name}/components/__init__.py", # Initialize components sub-package
    f"src/{project_name}/utils/__init__.py", # Initialize utils sub-package
    f"src{project_name}/config/__init__.py", # Initialize config sub-package
    f"src/{project_name}/config/configuration.py", # Configuration file for the project
    f"src/{project_name}/pipeline/__init__.py", # Initialize pipeline sub-package
    f"src{project_name}/entity/__init__.py", # Initialize entity sub-package
    f"src/{project_name}/constants/__init__.py", # Initialize constants sub-package
    "config/config.yaml", # Main configuration file
    "dvc.yaml", # DVC pipeline file
    "params.yaml", # Parameters file for experiments
    "requirements.txt", # Requirements file for dependencies
    "setup.py", # Setup file for packaging
    "research/trials.ipynb", # collab notebook for research trials
]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir, filename = os.path.split(filepath) # Split into directory and file name

  if filedir != "":
    os.makedirs(filedir, exist_ok=True) # Create directory if it doesn't exist
    logging.info(f"Created directory: {filedir} for the file: {filename}")

  if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    with open(filepath, "w") as f:
      pass # Create an empty file
    logging.info(f"Created empty file: {filepath}")

  else:
    logging.info(f"File already exists: {filepath}, skipping creation.")