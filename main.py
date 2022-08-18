import requests
import traceback

def searchApi(query):
    endpoint = "http://prod.media.jio.com/apis/common/v3.1/search/auto"
    data = {
        "q": query
    }
    try:
        list_msg = []
        response = requests.post(endpoint, data=data)
        if(response.status_code == 200):
            # for msg in response:
            #     print(msg)
            return response
    except Exception:
        print(traceback.format_exc())


text_msg = searchApi('avengers')
print(text_msg.json())


