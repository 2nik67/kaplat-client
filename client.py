import requests
import datetime

if __name__ == '__main__':
    current_hour = datetime.datetime.now().hour
    current_minute = datetime.datetime.now().minute
    # GET
    get_response = requests.get('http://localhost:8989/test_get_method', params={'hour': current_hour,
                                                                                 'minute': current_minute})
    # POST
    post_body = {
        "hour": current_hour,
        "minute": current_minute,
        "requestId": get_response.text
    }
    post_response = requests.post('http://localhost:8989/test_post_method', data=post_body)
    post_message = post_response.json()['message']

    current_hour = (current_hour + 21) % 24
    current_minute = (current_minute + 13) % 60

    # PUT
    put_body = {
        "hour": current_hour,
        "minute": current_minute
    }
    put_response = requests.put("http://localhost:8989/test_put_method", params={"id": post_message}, data=put_body)
    put_message = put_response.json()['message']

    # DELETE
    requests.delete("http://localhost:8989/test_put_method", params={"id": put_message})
