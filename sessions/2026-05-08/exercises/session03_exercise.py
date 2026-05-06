# =============================================================
# Session 3 exercise: reproducibility and project workflow
# ZAS Pythonistas working group
# =============================================================
# Work through each part in order. Read the instructions in the
# comments, then write your code below each TODO.
# Run the script from the terminal: python scripts/session03_exercise.py
# =============================================================

import pandas as pd
from pathlib import Path

# =============================================================
# PART A: check your environment
# =============================================================

# A1. In the terminal, run:
#     conda info --envs
#     The asterisk shows your active environment. Is it zas_python_wg?

# A2. In the terminal, export your full environment and inspect it:
#     conda env export > environment-full.yml
#     Open environment-full.yml and look at what is in there.

# A3. Now export only what you explicitly installed:
#     conda env export --from-history > environment-minimal.yml
#     Compare the two files. What is the difference?

# A4. Restart session:
#     Close and re-open your IDE (VS Code/Positron). Open your project 
#     folder, activate conda your environment in the terminal 
#     (`conda activate env_name`), and select the relevant interpreter.

# =============================================================
# PART B: fix the broken file path
# =============================================================

# This path is hardcoded and will break on every machine except
# the one it was written on. Your task is to fix it.

# B1. Run this script as-is and read the error:
#     python scripts/session03_exercise.py

# TODO B2: replace the broken path below with a relative path
# using pyprojroot or pathlib (see the session handout for the pattern)

data_path = "/Users/replace-me/projects/zas_python_wg/data/readtion_times.csv"

# B3. Once you have fixed the path, run the script again.
# If it works you should see the data printed below.

df = pd.read_csv(data_path)
print(f"Loaded {len(df)} rows")
print(df.describe())

# B4. Save your environment to environment.yml. Inspect it; is pyprojroot there?

# =============================================================
# PART C: git hygiene
# =============================================================

# C1. In the terminal, check what git sees:
#     git status
#     Do you see any files that should not be committed?

# C2. Create or update .gitignore to exclude:
#     __pycache__/
#     *.pyc
#     .ipynb_checkpoints/
#     .venv/

# C3. Stage your fixed script and .gitignore and commit:
#     git add scripts/session03_exercise.py .gitignore
#     git commit -m "fix: use relative paths in exercise script"

# =============================================================
# STRETCH: move this into a Quarto document
# =============================================================

# Open session03_exercise.qmd and render it to HTML:
#     quarto render session03_exercise.qmd
# Compare the experience of running code here vs in Quarto.
