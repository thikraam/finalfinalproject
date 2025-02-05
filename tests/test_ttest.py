import pytest
import pandas as pd
from working_code_f import ttest


def test_ttest_not_enough_data():
    data = pd.DataFrame({
        "Phase": ["Pre-Music Therapy"],
        "AlphaPowerMean": [10]
    })
    
    result = ttest(data)
    assert result is None, "T-test should not run if there is insufficient data"
