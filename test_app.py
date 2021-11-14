from app import *

website_path = "https://calm-ravine-03448.herokuapp.com/"

def test_about():
    
    assert about() == "TODO by Diane and Hoang"
    
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 200 #success

'''def test_view_index():
    
    client = app.test_client()
    url = "/"
    response = client.post()
    assert response.status_code == 400 #bad request
    
    response = client.post(url, data="test")
    assert response.status_code == 400
    
    text_data = {"text": "Test"}
    response = client.post(url, data=text_data)
    assert response.status_code == 200
    assert b'Test' in response.data
    
    priority_data = {"priority": "aHIGH"}
    response = client.post(url, data=priority_data)
    assert response.status_code == 400 #why?
    
    response = client.get("/")
    assert response.status_code == 200
  '''  
def test_edit_item():
    client = app.test_client()
    url = "/edit/0"
    
    text_data = {"text": "Test"}
    client.post("/", data=text_data)
    
    response = client.get(url)
    assert response.status_code == 302 #Success defined in method
    assert b'Test' not in response.data
    
def test_delete():
    client = app.test_client()
    url = "/delete/0"
    
    text_data = {"text": "Test"}
    response = client.post("/", data=text_data)
    
    response = client.post(url)
    assert response.status_code == 303 #Success defined in method
    assert b'Test' not in response.data

'''
def test_edit_priority():
    client = app.test_client()
    
    url = "/edit/0"
    data = {"priority":"HIGH"}
    
    text_data = {"text": "Test","priority":"HIGH"}
    response = client.post("/", data=text_data)
    
    response = client.post(url) # Not working
    assert response.status_code == 304
'''

    