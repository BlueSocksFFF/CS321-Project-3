from app import *
import requests

website_path = "https://calm-ravine-03448.herokuapp.com/"

def test_about():
    
    assert about() == "TODO by Diane and Hoang"
    
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200 #success