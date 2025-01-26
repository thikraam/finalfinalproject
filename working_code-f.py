# importing different libraries to help with analyzing the data.
import mne
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel
import seaborn as sns

def load_eeg(path):
    '''
    Load an EEG file in EDF format using the MNE library.

    Args:
        file_path (str): The full path to the EEG file in EDF format to be loaded.

    Returns:
        mne.io.Raw or None: An MNE Raw object containing the EEG data if the file is successfully loaded.
                           Returns None if the file is not found or cannot be loaded.

    Raises:
        FileNotFoundError: If the specified file does not exist, an error message is printed.
        Exception: Catches other errors that might occur during loading (e.g., file corruption,
                   unsupported file format) and prints a detailed error message.
    '''
    try:
        raw=mne.io.read_raw_edf(path, preload=True)
        return raw
    except Exception as e:
        print(f"Error loading file {path}: {e}")
    return None


def alpha_power(raw):
    '''
Compute the mean alpha power (8-13 Hz) of EEG data from an MNE Raw object.
Args:
    raw : mne.io.Raw
        An MNE Raw object containing EEG data. Ensure the data is properly preloaded
        and has been preprocessed as needed before calling this function.
Returns:
    float or None
        The mean alpha power across all channels if the computation is successful.
        Returns None if an error occurs during the computation.
Exceptions:
    - Exception:
        Catches any error that occurs during the power spectral density (PSD)
        computation or mean calculation. Prints an error message with details
        and returns None.

    '''
    try:
        psd=raw.compute_psd(fmin=8, fmax=13)
        psd_values= psd.get_data()
        return psd_values.mean(axis=1).mean()
    except Exception as e:
        print(f"Error computing alpha power: {e}")
        return None

def participants_loops(participants):
    '''
process EEG data for the participants, filtering for specific channels and calculating alpha power.
Args:
    participants (dict): a nested dictionary where keys are participant identifiers, values are dictionaries with session identifiers as keys, and each session dictionary contains phase identifiers as keys 
                         and paths to EEG files in EDF format as values.
Returns:
        list: A list of dictionaries, each containing the following keys:
            - "Participant": The participant identifier.
            - "Session": The session identifier.
            - "Phase": The phase identifier.
            - "AlphaPowerMean": The mean alpha power for the session and phase.
    '''
    all_participants=[]
    for participant, sessions in participants.items():
        for session,eeg_files in sessions.items():
            for phase,path in eeg_files.items():

                raw =load_eeg(path)
                if raw is None:
                    continue
                if set(["Fp1","Fp2"]).issubset(raw.info['ch_names']):
                    raw.pick_channels(["Fp1", "Fp2"])
                    alpha_power_mean=alpha_power(raw)

                    if alpha_power_mean is not None:
                        all_participants.append({
                            "Participant": participant,
                            "Session": session,
                            "Phase": phase,
                            "AlphaPowerMean": alpha_power_mean
                        })
                else:
                    print("Channels Fp1 and Fp2 NOT FOUND")
    return all_participants

 
def plot1(data_frame,participants):
    '''
    creats bar and line plots of alpha band power for each participant and session.
    Args:
        data_frame (pd.DataFrame): A pandas DataFrame containing the data to be plotted(include participant Identifier, session, phase and alpha power mean)
        participants (dict): A dictionary containing participant and session information.
    Plots:
        For each participant and session:
        - A bar plot displaying the mean alpha power for each phase.
        - A line plot showing the trend of mean alpha power across phases
    '''
    for partici in participants.keys():
        partici_data=data_frame[data_frame["Participant"]==partici]
        for session in participants[partici].keys():
            s_data=partici_data[partici_data["Session"]==session]
            phases=s_data["Phase"]
            means=s_data["AlphaPowerMean"]
            f, ax= plt.subplots(1,2,figsize=(14, 6))
            ax[0].bar(phases, means, color=['pink', 'purple', 'yellow'], alpha=0.7)
            ax[0].set_title(f'Alpha Band Power (Bar)- {partici}-{session}',fontsize=14)
            ax[0].set_xlabel('Phase',fontsize=12)
            ax[0].set_ylabel('Alpha Power (Mean)',fontsize=12)
            ax[0].grid(axis='y',linestyle='--',alpha=0.6)
            ax[1].plot(phases,means, marker='o',linestyle='-',color='skyblue')
            ax[1].set_title(f'Alpha Band Power (Line)-{partici}-{session}',fontsize=14)
            ax[1].set_xlabel('Phase', fontsize=12)
            ax[1].set_ylabel('Alpha Power',fontsize=12)
            ax[1].grid(linestyle='--',alpha=0.6)
            plt.tight_layout()
            
            plt.show()



def ttest(frame):
    '''
    Perform a paired t-test to compare pre-music therapy and post-music therapy alpha power means.
    Extract alpha power mean for "Post-Music Therapy" and "Pre-Music Therapy" phase from the DataFrame,
    Ensure there are enough data points in both "Pre-Music Therapy" and "Post-Music Therapy" groups to perform the t-test
    Args:
        frame (pd.DataFrame): A pandas DataFrame containing at least the following columns:
                              - "Phase": Should include "Pre-Music Therapy" and "Post-Music Therapy".
                              - "AlphaPowerMean": Mean alpha power values corresponding to each phase.
    Visualization:
        - Bar plot displays the t-statistic and p-value.
        - Includes a critical value line at P=0.05 for visual interpretation of statistical significance.                         

    '''
    post_music=frame[frame["Phase"]=="Post-Music Therapy"]["AlphaPowerMean"].values
    pre_music=frame[frame["Phase"]=="Pre-Music Therapy"]["AlphaPowerMean"].values
    if len(pre_music)>1:
        if len(post_music) >1:
            t_stat, p_value=ttest_rel(pre_music, post_music)
            print("\nT-Test Results:")
            print(f"T-Statistic: {t_stat}")
            print(f"P-Value: {p_value}")
            plt.figure(figsize=(8, 6))
            labs =['T-Statistic','P-Value']
            plt.bar(labs,[t_stat, p_value], color=['pink', 'purple'], alpha=0.7)
            plt.axhline(y=0.05, color='green', linewidth=1, label="Critical Value (P=0.05)")
            plt.title("T-Test Results", fontsize=14)
            plt.ylabel("Value",fontsize=12)
            plt.legend(fontsize=10)
            plt.grid(axis='y', alpha=0.6)
            plt.tight_layout()
            plt.show()
    else:
        print("There is no enough data to imply T-Test")



def plot2_heatmap(data_frame):
    '''
        create a heatmap to visualize the mean alpha power for each participant across different phases.
        using Seaborn's heatmap function, generating a heatmap (participants as rows, mean alpha as columns) 
        
        Args:
        data_frame (pd.DataFrame): A pandas DataFrame containing at least the following columns:
                                   - "Participant": Identifiers for participants.
                                   - "Phase": Different phases for which alpha power is recorded.
                                   - "AlphaPowerMean": Mean alpha power values for each participant and phase.
        Visualization:
        - A heatmap where:
            - Rows correspond to participants.
            - Columns correspond to phases.
            - Cell values represent the mean alpha power for a participant in a given phase.
        - Color intensity represents the magnitude of the mean alpha power.
        - Includes annotations (numerical values) in each cell for clarity.
        - Uses the "coolwarm" colormap for visual appeal.

    '''
    hmap=(data_frame.groupby(["Participant", "Phase"])["AlphaPowerMean"].mean().reset_index())
    plt.figure(figsize=(10, 8))
    sns.heatmap(hmap.pivot(index="Participant",columns="Phase",values="AlphaPowerMean"),annot=True, cmap="coolwarm", fmt=".4f")
    plt.title("Alpha Power Mean (Heatmap)",fontsize=14)
    plt.xlabel("Phase",fontsize=12)
    plt.ylabel("Participant",fontsize=12)
    plt.show()



def plot3_comparison(data_frame, participants):
    '''
    Generate a comparison plot of alpha power means across phases for multiple participants.

    Args:
        data_frame (pd.DataFrame): A pandas DataFrame containing the data to be plotted.
                                   It must include the following columns:
                                   - "Participant": Identifiers for participants.
                                   - "Phase": Different phases for which alpha power is recorded.
                                   - "AlphaPowerMean": Mean alpha power values for each phase and participant.
     participants (dict): A dictionary containing participant identifiers as keys, where the keys match 
                            the "Participant" column in the DataFrame.
    Visualization:
        - X-axis represents the phases.
        - Y-axis represents the mean alpha power values.
        - Each line corresponds to a participant, with a legend indicating participant identifiers.
        - Includes gridlines for better readability.
    
    '''
    plt.figure(figsize=(10, 6))
    for theid in participants.keys():
        participant_data=data_frame[data_frame["Participant"]==theid]
        plt.plot(participant_data["Phase"],participant_data["AlphaPowerMean"], marker='o',linestyle='-', label=theid)
    plt.title("Alpha Band Power Comparison",fontsize=14)
    plt.xlabel("Phase",fontsize=12)
    plt.ylabel("Alpha Power (Mean)",fontsize=12)
    plt.legend(title="Participant")
    plt.grid(linestyle="--",alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    '''
    Main function to analyze EEG data for multiple participants across sessions and phases.
    Workflow:
        1. Defines a dictionary (`partics`) containing EEG file paths for participants, 
           organized by session and phase.
        2. Processes the EEG data for all participants using `participants_loops`.
        3. Converts the processed data into a pandas DataFrame for analysis and visualization.
        4. Performs the following:
            - Prints the summary DataFrame showing features extracted from EEG data.
            - Generates visualizations:
                a. Bar and line plots for individual participants (`plot1`).
                b. Heatmap comparing alpha power across participants and phases (`plot2_heatmap`).
                c. Line plots comparing alpha power across phases for all participants (`plot3_comparison`).
            - Conducts a paired t-test for pre- and post-music therapy alpha power values (`ttest`).

    Visualization and Analysis Functions:
        - `plot1`: Bar and line plots for alpha power mean by phases and sessions.
        - `ttest`: Performs statistical analysis on pre- and post-music therapy data.
        - `plot2_heatmap`: Heatmap for alpha power mean comparison across participants and phases.
        - `plot3_comparison`: Line plot for alpha power mean comparison across phases for all participants.

    '''
    partics={
      "sub1": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-01\\ses-01\\eeg\\sub-01_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-01\\ses-01\\eeg\\sub-01_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-01\\ses-01\\eeg\\sub-01_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-01\\ses-02\\eeg\\sub-01_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-01\\ses-02\\eeg\\sub-01_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-01\\ses-02\\eeg\\sub-01_ses-02_task-postMusicTherapy_eeg.edf"
        }
    },
    "sub2": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-02\\ses-01\\eeg\\sub-02_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-02\\ses-01\\eeg\\sub-02_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-02\\ses-01\\eeg\\sub-02_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-02\\ses-02\\eeg\\sub-02_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-02\\ses-02\\eeg\\sub-02_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-02\\ses-02\\eeg\\sub-02_ses-02_task-postMusicTherapy_eeg.edf"
        }
    },
    "sub3": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-03\\ses-01\\eeg\\sub-03_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-03\\ses-01\\eeg\\sub-03_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-03\\ses-01\\eeg\\sub-03_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-03\\ses-02\\eeg\\sub-03_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-03\\ses-02\\eeg\\sub-03_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-03\\ses-02\\eeg\\sub-03_ses-02_task-postMusicTherapy_eeg.edf"
        }
    },
    "sub4": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-04\\ses-01\\eeg\\sub-04_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-04\\ses-01\\eeg\\sub-04_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-04\\ses-01\\eeg\\sub-04_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-04\\ses-02\\eeg\\sub-04_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-04\\ses-02\\eeg\\sub-04_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-04\\ses-02\\eeg\\sub-04_ses-02_task-postMusicTherapy_eeg.edf"
        }
    },
    "sub5": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-05\\ses-01\\eeg\\sub-05_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-05\\ses-01\\eeg\\sub-05_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-05\\ses-01\\eeg\\sub-05_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-05\\ses-02\\eeg\\sub-05_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-05\\ses-02\\eeg\\sub-05_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-05\\ses-02\\eeg\\sub-05_ses-02_task-postMusicTherapy_eeg.edf"
        }
    },
    "sub6": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-06\\ses-01\\eeg\\sub-06_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-06\\ses-01\\eeg\\sub-06_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-06\\ses-01\\eeg\\sub-06_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-06\\ses-02\\eeg\\sub-06_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-06\\ses-02\\eeg\\sub-06_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-06\\ses-02\\eeg\\sub-06_ses-02_task-postMusicTherapy_eeg.edf"
        }
    },
    "sub7": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-07\\ses-01\\eeg\\sub-07_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-07\\ses-01\\eeg\\sub-07_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-07\\ses-01\\eeg\\sub-07_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-07\\ses-02\\eeg\\sub-07_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-07\\ses-02\\eeg\\sub-07_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-07\\ses-02\\eeg\\sub-07_ses-02_task-postMusicTherapy_eeg.edf"
        }
    },
    "sub8": {
        "ses01": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-08\\ses-01\\eeg\\sub-08_ses-01_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-08\\ses-01\\eeg\\sub-08_ses-01_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-08\\ses-01\\eeg\\sub-08_ses-01_task-postMusicTherapy_eeg.edf"
        },
        "ses02": {
            "Pre-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-08\\ses-02\\eeg\\sub-08_ses-02_task-preMusicTherapy_eeg.edf",
            "Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-08\\ses-02\\eeg\\sub-08_ses-02_task-musicTherapy_eeg.edf",
            "Post-Music Therapy": "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-08\\ses-02\\eeg\\sub-08_ses-02_task-postMusicTherapy_eeg.edf"
        }
    }
}

    all_participants=participants_loops(partics)
    all_participants_data_frame=pd.DataFrame(all_participants)

    print("\nAll Participants Featurs:")
    print(all_participants_data_frame)

    plot1(all_participants_data_frame,partics)
    ttest(all_participants_data_frame)
    plot2_heatmap(all_participants_data_frame)
    plot3_comparison(all_participants_data_frame, partics)

if __name__ == "__main__":
   main()