import wlan
import urequests as requests
import time
import ujson as json
import mysensor.config as config

wlan.connect()

now_time = 141200

while True:
    data = {
        "date" : 20241014,
        "time" : now_time,
        "temperature" : 25.0,
        "humidity" : 50.0,
        "pressure" : 1013
    }
    header = {
        'Content-Type' : 'application/json'
    }
    res = requests.post(
        url = config.URL,
        data = json.dumps(data).encode("utf-8"),
        headers = header
    )
    
    res.close()

    time.sleep(10)
    now_time += 10
