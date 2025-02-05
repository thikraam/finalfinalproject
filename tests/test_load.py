import pytest
import mne
from working_code_f import load_eeg

def test_load_valid_eeg():
    path = "C:\\Users\\user\\Desktop\\finalfinalproject\\sub-01\\ses-01\\eeg\\sub-01_ses-01_task-PreMusicTherapy_eeg.edf"

    raw = load_eeg(path)
    assert raw is not None, "Failed to load valid EEG file"

def test_load_invalid_eeg():
    path = "./non_existent_file.edf"
    raw = load_eeg(path)
    assert raw is None, "Function should return None for missing files"
