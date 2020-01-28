import common

def test_checkKeys():
    assert common.checkKeys(None) == False

    assert common.checkKeys(1) == False