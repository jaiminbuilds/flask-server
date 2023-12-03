import requests

def get_hello():
    url = 'https://limitless-oasis-36594-df4aab0d8c6c.herokuapp.com/'  # URL for the hello_world endpoint
    response = requests.get(url)
    print('Response from /:', response.text)

def get_custom_message():
    url = 'https://limitless-oasis-36594-df4aab0d8c6c.herokuapp.com/message'  # URL for the send_message endpoint
    response = requests.get(url)
    print('Response from /message:', response.text)

if __name__ == "__main__":
    get_hello()
    get_custom_message()

