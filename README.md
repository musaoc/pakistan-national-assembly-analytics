# National Assembly of Pakistan — Parliamentary Demographics & Politics EDA

An exploratory demographic and political analytics study examining educational profiles, party distributions, and provincial allocations within the National Assembly of Pakistan.

[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-Notebook-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/lazer999/national-assembly-pakistan-data-analysis)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Field](https://img.shields.io/badge/Field-Exploratory%20Data%20Analysis%20/%20Public%20Sector-brightgreen)](#)

---

## Table of Contents
- [Project Overview](#project-overview)
- [Key Highlights & Results](#key-highlights--results)
- [System Architecture & Workflow](#system-architecture--workflow)
- [Repository Structure](#repository-structure)
- [Quickstart & Reproduction](#quickstart--reproduction)
- [Dataset Details](#dataset-details)
- [Author & Acknowledgments](#author--acknowledgments)

---

## Project Overview

This repository provides the complete, production-structured implementation of the **[National Assembly of Pakistan — Parliamentary Demographics & Politics EDA](https://www.kaggle.com/code/lazer999/national-assembly-pakistan-data-analysis)** project originally published on Kaggle. 

The primary focus of this work is translating complex data into actionable machine learning solutions using disciplined data engineering, rigorous validation strategies, and clean, leak-free preprocessing pipelines.

---

## Key Highlights & Results

- Extracted and standardized parliamentary membership rosters and educational records.
- Educational attainment distribution analysis across parliamentarians and ministerial offices.
- Party-level representation and coalition balance breakdown across provinces (Punjab, Sindh, KP, Balochistan, Federal Capital).
- Aesthetic dark-themed data visualizations summarizing governance representation.

---

## System Architecture & Workflow

The pipeline follows a structured, modular execution path:

```mermaid
flowchart LR
    A[Parliamentary Excel Records] --> B[Data Cleaning & Normalization]
    B --> C[Party Seat Share Distribution]
    B --> D[Education Level Classification]
    B --> E[Provincial Representation Breakdown]
    C --> F[Demographic & Political Findings]
    D --> F
    E --> F
```

---

## Repository Structure

```plaintext
pakistan-national-assembly-analytics/
├── notebooks/
│   └── pakistan-national-assembly-analytics.ipynb      # Original Jupyter notebook with full exploratory visuals
├── src/
│   └── main.py                # Modular, executable Python pipeline
├── .gitignore                 # Standard Python/Jupyter ignores
├── LICENSE                    # MIT License
├── README.md                  # Human-friendly documentation
└── requirements.txt           # Verified Python dependencies
```

---

## Quickstart & Reproduction

### 1. Clone the Repository
```bash
git clone https://github.com/musaoc/pakistan-national-assembly-analytics.git
cd pakistan-national-assembly-analytics
```

### 2. Set Up a Virtual Environment
```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Pipeline
You can run the end-to-end script directly:
```bash
python src/main.py
```

Or open and run the interactive notebook:
```bash
jupyter lab notebooks/pakistan-national-assembly-analytics.ipynb
```

---

## Dataset Details

- **Dataset / Competition**: [National Assembly of Pakistan Dataset](https://www.kaggle.com/datasets/uzairadamjee/national-assembly-of-pakistan)
- **Origin Platform**: Kaggle
- For automated dataset downloading via Kaggle CLI:
  ```bash
  kaggle datasets download -d uzairadamjee/national-assembly-of-pakistan
  ```

---

## Author & Acknowledgments

- **Author**: **Muhammad Musa Khan** (Kaggle Master)
- **Kaggle Profile**: [@lazer999](https://www.kaggle.com/lazer999)
- **GitHub**: [@musaoc](https://github.com/musaoc)
- **Original Kaggle Solution**: [National Assembly of Pakistan — Parliamentary Demographics & Politics EDA](https://www.kaggle.com/code/lazer999/national-assembly-pakistan-data-analysis)

If you found this project helpful or insightful, please consider starring the repository ⭐!
