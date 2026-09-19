"""
National Assembly of Pakistan — Parliamentary Demographics & Politics EDA
An exploratory demographic and political analytics study examining educational profiles, party distributions, and provincial allocations within the National Assembly of Pakistan.

Original Kaggle Notebook: https://www.kaggle.com/code/lazer999/national-assembly-pakistan-data-analysis
Author: Muhammad Musa Khan (Kaggle Master: https://kaggle.com/lazer999)
"""

import os
import sys
import warnings
warnings.filterwarnings("ignore")

# --- Smart Dataset Path Resolution ---
def _resolve_data_path(file_path):
    """Checks local and data/ directories if dataset path is missing."""
    if os.path.exists(file_path):
        return file_path
    base = os.path.basename(file_path)
    candidates = [
        base,
        os.path.join("data", base),
        os.path.join("..", "data", base),
        file_path.replace("/kaggle/input/", "data/"),
        file_path.replace("../input/", "data/"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return file_path

# --- Pipeline Execution ---

# --- Cell 1 ---

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
#To give the graph some dark color.
sns.set_style('darkgrid')

# --- Cell 3 ---
df = pd.read_excel('/kaggle/input/national-assembly-of-pakistan/NA_list.xlsx')
df.head()

# --- Cell 4 ---
df.shape

# --- Cell 5 ---
df.info()

# --- Cell 6 ---
df.isnull().sum()

# --- Cell 7 ---
df=df.drop('Contact',axis=1)

# --- Cell 8 ---
sns.histplot(df['Party'])
plt.ylabel('Number of candidates');

# --- Cell 9 ---
candidates_per_party=df.groupby(['Party'])['Party'].count().sort_values(ascending=False)
candidates_per_party

# --- Cell 10 ---
plt.figure(figsize=(15, 9))
sns.barplot(y=candidates_per_party.index,x=candidates_per_party)
plt.xlabel('Candidates in the National Assembly of Pak')
;

# --- Cell 11 ---
education = df.groupby('Profession/Education')['Party'].count().sort_values(ascending=False)
education

# --- Cell 12 ---
plt.figure(figsize=(15, 9))
sns.barplot(y=education.index[:10],x=education[:10])
plt.xlabel('Candidates in the National Assembly of Pak')
;

# --- Cell 13 ---
Education_party=df.groupby(['Party','Profession/Education'])['Party'].count().sort_values(ascending=False).unstack(level=1).fillna(0)
Education_party



if __name__ == "__main__":
    print("Pipeline execution complete.")
