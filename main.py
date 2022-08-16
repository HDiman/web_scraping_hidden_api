import requests
import traceback
import json

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
print(text_msg)
for msg in text_msg:
    print(msg)

#
# your_json = f"{searchApi('avengers')}"
# parsed = json.loads(your_json)
# print(json.dumps(parsed, indent=4, sort_keys=True))

