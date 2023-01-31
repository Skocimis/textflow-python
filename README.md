# Textflow python client

[![PyPI](https://img.shields.io/pypi/v/textflowsms.svg)](https://pypi.python.org/pypi/textflowsms)
[![PyPI](https://img.shields.io/pypi/pyversions/textflowsms.svg)](https://pypi.python.org/pypi/textflowsms)

### Supported Python Versions

This library supports the following Python implementations:

* Python 3.6
* Python 3.7
* Python 3.8
* Python 3.9
* Python 3.10
* Python 3.11

## Installation
`pip install textflowsms`

## Sample Usage

To send an SMS, you have to create an API key using the [Textflow dashboard](https://textflow.me/api). When you register an account, you automatically get an API key with one free SMS which you can send anywhere.

### Just send a message

```python
import textflowsms as tf
tf.useKey("YOUR_API_KEY");

tf.sendSMS("+381611231234", "Dummy message text...")
```

### Handle send message request result

```python
result = tf.sendSMS("+381611231234", "Dummy message text...")
if(result.ok):
  print(result.data)
else:
  print(result.message)
```

### Example result object of the successfully sent message

```json
{
    "ok": true,
    "status": 200,
    "message": "Message sent successfully",
    "data": {
        "to": "+381611231234",
        "content": "Dummy message text...",
        "country_code": "RS",
        "price": 0.05,
        "timestamp": 1674759108881
    }
}
```

### Example result object of the unsuccessfully sent message

```json
{
    "ok": false,
    "status": 404,
    "message": "API key not found"
}
```

## Getting help

If you need help installing or using the library, please check the [FAQ](https://textflow.me) first, and contact us at [support@textflow.me](mailto://support@textflow.me) if you don't find an answer to your question.

If you've found a bug in the API, package or would like new features added, you are also free to contact us!
