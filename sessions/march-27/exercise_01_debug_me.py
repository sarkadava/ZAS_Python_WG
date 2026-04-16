# ============================================================
#  TASK: Run this script. Several things will break.
#        Find and fix each error, one at a time.

#  HINT: Read the error messages carefully — Python usually
#        tells you exactly what is wrong and on which line.
# ============================================================


# --- 0. IMPORTS -------------------------------------------


import numpy as np
import pandas as pd
import seaborn as sns         


# --- 1. LOAD DATA -----------------------------------------
#
# Make sure you are running the script from the project root,
# or adjust the path below.

df = pd.read_csv("data/scores.csv")


# --- 2. QUICK LOOK ----------------------------------------

print("Shape:", df.shape)
print(df.head())


# --- 3. FILTER ROWS -----------------

# Keep only rows where condition is TRUE
good_rows <- df["score"] > 50        

print("Rows passing filter:", len(good_rows))


# --- 4. COMPUTE A SUMMARY ---------------------------------

mean_score = df["score"].mean()
max_score  = df["score"].max()

print("Mean score:", round(mean_score, 2)       
print("Max score: ", max_score)


# --- 5. ADD A NEW COLUMN ----------------------------------

# Normalise scores to 0–1 range
df["score_norm"] = (df["score"] - df["score"].min()) / \
                   (df["score"].max() - df["score"].min)  


# --- 6. PLOT ----------------------------------------------

sns.histplot(data=df, x="score_norm")