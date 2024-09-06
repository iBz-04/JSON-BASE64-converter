## Overview

Because some older systems think that data consists of 7-bit chunks (bytes), whereas modern ones use 8-bit bytes. This may lead to misunderstandings between systems. And **base64** presumably can help with this

### Stack

- Python3

## How It Works

The code first transforms the JSON object into a JSON-formatted string. 
This string is then encoded to bytes using UTF-8 encoding. Next, the byte-encoded JSON string is converted into a Base64 byte string.
This Base64 byte string is decoded back into a regular string.


## Installation

1. Clone the repository

```bash
git clone https://github.com/iBz-04/JSON-BASE64-converter.git
```

## Feedback

If you have any feedback, please reach out to me ibz.04dev@gmail.com


## Author

- [@iBz-04](https://github.com/iBz-04)
