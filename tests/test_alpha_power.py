import pytest
import mne
import numpy as np
from working_code_f import alpha_power

def test_alpha_power_valid():
    
    info = mne.create_info(ch_names=["Fp1", "Fp2"], sfreq=256, ch_types="eeg")
    data = np.random.rand(2, 256*5)  # Simulated 5-second EEG data
    raw = mne.io.RawArray(data, info)
    
    result = alpha_power(raw)
    assert result is not None, "Alpha power computation failed"
    assert isinstance(result, float), "Alpha power should return a float"

