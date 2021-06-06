import requests

link="https://artii.herokuapp.com/make?text="
def get(a):
    text= ' '.join(map(str, a))
    response=requests.get(link+text)
    if(response.status_code!=200):
        return "😔"
    return response.text