from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    'src/__init__.py',
    'src/helper.py',
    'src/propmt.py',
    '.env',
    'setup.py',
    'app.py',
    'research/hit_and_trial.ipynb',
    'test.py',
    'requirements.txt',
    'Dockerfile',
    'templates/chat.html',
    'static/style.css'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)

    # import code;code.interact(local=locals())
    '''crete the directory'''
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")

    '''creating the filepath'''
    if not os.path.exists(filepath) or os.path.getsize(filepath) ==0:
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating file: {filepath}")

    else:
        logging.info(f"{file_name} already exists")
