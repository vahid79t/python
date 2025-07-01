from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Request
import requests
import json


app = FastAPI()
@app.post("/")
async def root(request: Request):
    try:
        raw_data = await request.body()
        data_str = raw_data.decode("utf-8")
        with open("/root/python/testlog", "w") as file:
            file.write(data_str)
        cleantext(data_str)
        return {"message": "Data received and saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def webhookzoho(data):
    url = 'https://cliq.zoho.com/<>'
    headers = {"Content-Type": "application/json"}
    payload = json.dumps(data,ensure_ascii=False)
    response = requests.post(url, data=payload.encode("utf-8"), headers=headers)
    

def cleantext(rawdata):
    list=[]
    emoji="🚩🚩"
    datatest=json.loads(rawdata)
    for question_id, question_data in datatest["quiz"]["sport"].items():
        list.append(f"{emoji}    {question_data['question']}")
    #json_string = json.dumps(list ,ensure_ascii=False)
    json_string = "\n".join(list)
    webhookzoho(json_string)
