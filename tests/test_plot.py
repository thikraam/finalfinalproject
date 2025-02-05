import pytest
import pandas as pd
from working_code_f import plot1

def test_plot1_runs_without_error():
    data = pd.DataFrame({
        "Participant": ["sub1", "sub1", "sub1"],
        "Session": ["ses01", "ses01", "ses01"],
        "Phase": ["Pre-Music Therapy", "Music Therapy", "Post-Music Therapy"],
        "AlphaPowerMean": [10.5, 12.3, 11.0]
    })
    
    try:
        plot1(data, {"sub1": {"ses01": {}}})
    except Exception as e:
        pytest.fail(f"Plot function failed with error: {e}")
