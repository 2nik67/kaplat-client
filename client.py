import requests
import datetime

if __name__ == '__main__':
    get_response = requests.get('http://localhost:8989/test_get_method', params={'hour': datetime.datetime.now().hour,
                                                                      'minute': datetime.datetime.now().minute})
    print(get_response.text)
    post_body = {
        "hour": datetime.datetime.now().hour,
        "minute": datetime.datetime.now().minute,
        "requestId": get_response.text
    }
    x = requests.post('http://localhost:8989/test_post_method', data=post_body)
    message = x.json()['message']
    print(message)
