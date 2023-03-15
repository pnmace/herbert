import requests
import json

bearer_token = "I'm too lazy to do this the correct way for a personal project :^)"

def create_url(post_id):
    fields = "tweet.fields=lang,author_id,attachments"
    url = "https://api.twitter.com/2/tweets?ids={}&{}".format(post_id, fields)
    return url

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def check_twitter(post_id):
    url = create_url(post_id)
    json_response = connect_to_endpoint(url)
    # print(json.dumps(json_response, indent=4, sort_keys=True))

    media_key = ""
    try:
        media_key = json_response['data'][0]['attachments']['media_keys'][0]
    except:
        return False

    print(media_key)

    if media_key[0] == "7":
        return True
    return False
