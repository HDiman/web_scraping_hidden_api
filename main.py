import requests
import traceback


def searchApi(query):
    endpoint = "http://prod.media.jio.com/apis/common/v3.1/search/auto"
    data = {
        "q": query
    }
    try:
        response = requests.post(endpoint, data=data)
        if(response.status_code == 200):
            for msg in response:
                print(msg)
    except Exception:
        print(traceback.format_exc())


searchApi("avengers")
