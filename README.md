# Analyzing the Effects of Music Therapy on Prefrontal Alpha Band Power: A Comparative Study of Pre- and Post-Task EEG Activity

## introduction

 This project aims to analyze brain activity in brun patients, comparing three phases, pre-music, music therapy and post-music, focusing on alpha band(8-13 Hz) in the prefrontal region(channels Fp1,Fp2)associated with relaxation.
 Link to project report: [Document](https://docs.google.com/document/d/1OiuVH0cCUNCZ87sU4yiWL3F3qq7HtI8Oq92h5-Gz_1g/edit?usp=sharing)

## dataset description

 The dataset contains EEG recordings from 9 burn patients who participated in
music assisted relaxation therapy. The EEG signals recorded are
FP1,FP2,T3,T4,C3,C4,O1,O2 with reference at Cz.
They examined the brainwave during three phases: pre-task, music listening (during) and
post-task.
project sources:
raw data, [OpenNeuro Dataset](https://openneuro.org/datasets/ds004840/versions/1.0.1)
article [Nature Scientific Reports](https://www.nature.com/articles/s41598-024-73211-3)

## research question

How does pre-task brain activity differ from post-task brain activity
during music-listening sessions in patients, focusing on alpha band power in the prefrontal region?

## Results

The analysis exposed a significant change in alpha power between pre and post-music therapy phases. The T-statistic was -2.38, and the P-value was 0.031(), which indicates that the difference in alpha power between the phases is statistically significant at the 0.05 level.

## Installation and Requirements

**1. insure you have the correct python version** "Python.3.12"
**2.Clone the repository:** git clone <repository-url>

**3.To ensure compatibility, the following Python packages are required:**  
• mne
• pandas
• matplotlib
• numpy
• scipy
• seaborn
**-Run the following commands in your terminal or command prompt:**
pip install mne  
pip install pandas  
pip install matplotlib  
pip install numpy  
pip install scipy  
pip install seaborn

## project structure

FINAL PROJECT/
├── .mypy_cache/
│   ├── 3.12/
│   ├── 3.13/
├── .gitignore
├── CACHEDIR.TAG
├── missing_stubs
├── sub01/
│   ├── ses1/
│   │   ├── sub-01_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-01_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-01_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-01_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-01_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-01_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-01_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-01_ses-02_task-musicTherapy_eeg.json
│       ├── sub-01_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-01_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-01_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-01_ses-02_task-preMusicTherapy_eeg.json
├── sub02/
│   ├── ses1/
│   │   ├── sub-02_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-02_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-02_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-02_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-02_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-02_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-02_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-02_ses-02_task-musicTherapy_eeg.json
│       ├── sub-02_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-02_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-02_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-02_ses-02_task-preMusicTherapy_eeg.json
├── sub03/
│   ├── ses1/
│   │   ├── sub-03_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-03_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-03_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-03_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-03_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-03_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-03_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-03_ses-02_task-musicTherapy_eeg.json
│       ├── sub-03_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-03_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-03_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-03_ses-02_task-preMusicTherapy_eeg.json
├── sub04/
│   ├── ses1/
│   │   ├── sub-04_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-04_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-04_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-04_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-04_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-04_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-04_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-04_ses-02_task-musicTherapy_eeg.json
│       ├── sub-04_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-04_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-04_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-04_ses-02_task-preMusicTherapy_eeg.json
├── sub05/
├── ses1/
│   │   ├── sub-05_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-05_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-05_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-05_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-05_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-05_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-05_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-05_ses-02_task-musicTherapy_eeg.json
│       ├── sub-05_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-05_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-05_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-05_ses-02_task-preMusicTherapy_eeg.json
├── sub06/
├── ses1/
│   │   ├── sub-06_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-06_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-06_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-06_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-06_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-06_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-06_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-06_ses-02_task-musicTherapy_eeg.json
│       ├── sub-06_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-06_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-06_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-06_ses-02_task-preMusicTherapy_eeg.json
├── sub07/  
├── ses1/
│   │   ├── sub-07_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-07_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-07_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-07_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-07_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-07_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-07_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-07_ses-02_task-musicTherapy_eeg.json
│       ├── sub-07_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-07_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-07_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-07_ses-02_task-preMusicTherapy_eeg.json
├── sub08/  
├── ses1/
│   │   ├── sub-08_ses-01_task-musicTherapy_eeg.edf
│   │   ├── sub-08_ses-01_task-musicTherapy_eeg.json
│   │   ├── sub-08_ses-01_task-postMusicTherapy_eeg.edf
│   │   ├── sub-08_ses-01_task-postMusicTherapy_eeg.json
│   │   ├── sub-08_ses-01_task-preMusicTherapy_eeg.edf
│   │   ├── sub-08_ses-01_task-preMusicTherapy_eeg.json
│   ├── ses2/
│       ├── sub-08_ses-02_task-musicTherapy_eeg.edf
│       ├── sub-08_ses-02_task-musicTherapy_eeg.json
│       ├── sub-08_ses-02_task-postMusicTherapy_eeg.edf
│       ├── sub-08_ses-02_task-postMusicTherapy_eeg.json
│       ├── sub-08_ses-02_task-preMusicTherapy_eeg.edf
│       ├── sub-08_ses-02_task-preMusicTherapy_eeg.json
├── venv/ (virtual environment)
├── notebookfinal.ipynb
├── project_py.py
└── README

### usage

**1.preapear the Dataset:**

- organize the EEG files into a folder structure matching the parics dictionary format in the code.
**2. Run the script:**
  -Place the script in a .py file, for example, eeg_analysis.py.
  -In the terminal, run the script:
   python eeg_analysis.py
**3. Analyze an visualize results:**
    -The script will process EEG data, calculate alpha power,         and generate visualizations, including:
        -Bar and Line Plots: Display alpha band power across participants and sessions.
        -Heatmaps: Compare alpha power across phases.
        -Statistical Analysis: A paired t-test to evaluate differences between pre- and post-music therapy.
**4.Output:**
    -Key results, including the alpha power mean for each phase, will be displayed in the terminal.
    -Plots will be generated and displayed.
**Example Command**
    -If you want to test a specific EEG file for alpha power:

        ```python

        raw = load_eeg("path_to_eeg.edf")
        print(alpha_power(raw))
        ```

    -To run for all participants in the dictionary:

        ```python

        main()
        ```
