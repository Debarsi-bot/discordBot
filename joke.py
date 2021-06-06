import requests
import json

link="https://v2.jokeapi.dev/joke/"
def get(a):
    response=requests.get(link+a)
    if(response.status_code!=200):
        return "No jokes found"
    data=json.loads(response.text)
    error=data["error"]
    if(error):
        return "No jokes found"
    else:
        type=data["type"]
        if(type=="twopart"):
            return data["setup"]+"\n\n"+data["delivery"]
        else:
            return data["joke"]

