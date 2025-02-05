import pytest
from working_code_f import create_participants

def test_create_participants():
    partics = create_participants()
    
    assert isinstance(partics, dict), "Participants should be a dictionary"
    assert "sub1" in partics, "First subject missing"
    assert "ses01" in partics["sub1"], "Session structure incorrect"
    assert "Pre-Music Therapy" in partics["sub1"]["ses01"], "Phase structure incorrect"
