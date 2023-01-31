import requests
import json

class SendMessageData:
    def __init__(self, obj):
        self.to:str = obj["to"]
        self.content:str = obj["content"]
        self.country_code:str = obj["country_code"]
        self.price:float = obj["price"]
        self.timestamp:int = obj["timestamp"]
    def __str__(self) -> str:
        return json.dumps(self.__dict__)

class SendMessageResult:
    def __init__(self, obj):
        self.ok:bool = obj["ok"]
        self.status:str = obj["status"]
        self.message:str = obj["message"]
        if(self.ok):
            self.data:SendMessageData = SendMessageData(obj["data"])
    def __str__(self) -> str:
        return json.dumps(self.__dict__, default=vars)


apiKey:str = ""

def useKey(key:str):
    """
    Set the API key, so that the service knows that you are authorized to use it.

    Parameters:
    key (string): Unique key created using the [API Console](https://textflow.me/api)

    Examples:
    >>> import textflow as tf
    >>> tf.useKey("YOUR_API_KEY")
    """
    global apiKey
    apiKey = key


def sendSMS(recipient:str, text:str)->SendMessageResult:
    """
    Function that is used to send an SMS. 

    Parameters:
    recipient (string): Recipient phone number, formatted like `+381617581234`
    text (string): Message body

    Returns:
    SendMessageResult: Result status of the TextFlow Send SMS API call

    Examples:
    >>> import textflow as tf
    >>> tf.useKey("YOUR_API_KEY")
    >>> tf.sendSMS(recipient="+3811231234", text="Message text...")
    """
    global apiKey
    if(len(recipient) == 0):
        return dict(ok=False, status=400, message="You have not specified the recipient. ")
    if(len(text) == 0):
        return dict(ok=False, status=400, message="You have not specified the message body. ")
    if(len(apiKey) == 0):
        return dict(ok=False, status=400, message="You have not specified the API key. ")
    data = json.dumps(dict(recipient=recipient, text=text, apiKey=apiKey))
    r = requests.post(
        url="https://textflow.me/messages/send",
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Content-Length': str(len(data))
        })
    return SendMessageResult(json.loads(r.text)) 