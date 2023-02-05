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

class VerifyPhoneData:
    def __init__(self, obj):
        self.verification_code:str = obj["verification_code"]
        self.expires:int = obj["expires"]
        self.message_text:str = obj["message_text"]
    def __str__(self) -> str:
        return json.dumps(self.__dict__)

class SendMessageResult:
    def __init__(self, obj):
        self.ok:bool = obj["ok"]
        self.status:int = obj["status"]
        self.message:str = obj["message"]
        if(self.ok):
            self.data:SendMessageData = SendMessageData(obj["data"])
    def __str__(self) -> str:
        return json.dumps(self.__dict__, default=vars)

class VerifyPhoneResult:
    def __init__(self, obj):
        self.ok:bool = obj["ok"]
        self.status:int = obj["status"]
        self.message:str = obj["message"]
        if(self.ok):
            self.data:VerifyPhoneData = VerifyPhoneData(obj["data"])
    def __str__(self) -> str:
        return json.dumps(self.__dict__, default=vars)


class VerifyCodeResult:
    def __init__(self, obj):
        self.ok:bool = obj["ok"]
        self.status:int = obj["status"]
        self.message:str = obj["message"]
        self.valid:bool = obj["valid"]
        if("valid_code" in obj):
            self.valid_code:str = obj["valid_code"]
        if("expires" in obj):
            self.expires:int = obj["expires"]
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


def sendSMS(phone_number:str, text:str)->SendMessageResult:
    """
    Function that is used to send an SMS. 

    Parameters:

    phone_number (string): Recipient phone number, formatted like `+381617581234`

    text (string): Message body

    Returns:
    SendMessageResult: Result status of the TextFlow Send SMS API call

    Examples:

    >>> import textflow as tf
    >>> tf.useKey("YOUR_API_KEY")
    >>> tf.sendSMS("+11234567890", text="Message text...")
    """
    global apiKey
    if(len(phone_number) == 0):
        return dict(ok=False, status=400, message="You have not specified the recipient phone number. ")
    if(len(text) == 0):
        return dict(ok=False, status=400, message="You have not specified the message body. ")
    if(len(apiKey) == 0):
        return dict(ok=False, status=400, message="You have not specified the API key. ")
    data = dict(phone_number=phone_number, text=text)
    
    r = requests.post(
        url="https://textflow.me/api/send-sms",
        json=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ apiKey
        })
    return SendMessageResult(json.loads(r.text)) 


def sendVerificationSMS(phone_number:str, service_name:str = "", seconds:int = 600)->VerifyPhoneResult:
    """
    Function that is used to send a phone number verification SMS to your customer. 

    Parameters:

    phone_number (string): Phone number to verify, including country calling code, like `+11234567890`

    service_name (string): What the user will see in the verification message. If the `service_name` is `"Guest"`, they would get the message `"Your verification code for Guest is: CODE"`. Default is none

    seconds (int): How many seconds is the code valid for. Default is 10 minutes. Maximum is one day.

    Returns:
    VerifyPhoneResult: Result status of the TextFlow Verify phone number API call

    Example: 

    ```python
    #User has sent his phone number for verification
    tf.sendVerificationSMS(phone_number)

    #Show him the code submission form
    #The user has submitted the code

    res = tf.verifyCode(phone_number, code)
    if res.valid:
        print("Real user")
    
    ```
    

    """
    global apiKey
    if(len(phone_number) == 0):
        return dict(ok=False, status=400, message="You have not specified the recipient phone number. ")
    if(len(apiKey) == 0):
        return dict(ok=False, status=400, message="You have not specified the API key. ")
    data = dict(phone_number=phone_number, service_name=service_name, seconds = seconds)
    
    r = requests.post(
        url="https://textflow.me/api/send-code",
        json=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ apiKey
        })
    return VerifyPhoneResult(json.loads(r.text)) 

def verifyCode(phone_number:str, code:str)->VerifyCodeResult:
    """
    Function that is used to verify the code that the customer has submitted. 

    Parameters:

    phone_number (string): Phone number to verify, including country calling code, like `+11234567890`

    code (string): Verification code that the user has submitted.

    Returns:
    VerifyCodeResult: Result status of the TextFlow Verify phone number API call

    Example: 

    ```python
    # prior to the call of this function,
    # you have called the sendVerificationSMS
    # and the user has submitted the code
    # that now needs to be verified

    res = tf.verifyCode(phone_number, code)
    if res.valid:
        print("Real user")
    
    ```
    

    """
    global apiKey
    if(len(phone_number) == 0):
        return dict(ok=False, status=400, message="You have not specified the recipient phone number. ", valid=False)
    if(len(code) == 0):
        return dict(ok=False, status=400, message="You have not specified the recipient phone number. ", valid=False)
    if(len(apiKey) == 0):
        return dict(ok=False, status=400, message="You have not specified the API key. ", valid=False)
    data = dict(phone_number=phone_number, code=code)
    
    r = requests.post(
        url="https://textflow.me/api/verify-code",
        json=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ apiKey
        })
    return VerifyCodeResult(json.loads(r.text)) 