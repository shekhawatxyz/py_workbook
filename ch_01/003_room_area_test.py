import pytest
room_area =__import__("003_room_area", fromlist=["room_area"]).room_area 

def test_room_area():
    assert room_area(5,3) == 15
    #assert room_area(5,4) == 20
    #assert room_area(2,1) == 2
