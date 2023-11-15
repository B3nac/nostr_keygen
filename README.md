### Why

I was looking for the easiest way to generate `npub` and `nsec` keys myself locally without a ton of dependencies. There wasn't a solution out there for Python so here we are. Currently planning on building upon this example and adding various features. 

### Dependencies to run nostr_keygen.py

1. On Debian/Ubuntu you might need to install 

`sudo apt install build-essential automake pkg-config libtool libffi-dev`

to compile libsecp256k1.

2. Python3 and what's in the requirements.txt file.

If you have multiple Python versions or are worried about dependency conflicts I recommend using a virtual environment.

`python3 -m venv envname`

`source path/to/env/bin/activate`

else:

`pip install -r requirements.txt`

`python3 nostr_keygen.py`

### Build from source into a binary

`pyinstaller --add-data bech32:bech32 --add-binary _cffi_backend.cpython-310-x86_64-linux-gnu.so:. --onefile nostr_keygen.py`

### What nostr_keygen does currently

The script will print out the `npub` and `nsec` address that is randomly generated as well as ascii qrcodes for mobile clients.

#### In the works

- Add import private key function 
- Add CLI params for specific output
- Add a way to generate a specific number of key pairs
- Add support for NIP-05 via output of nostr.json via CLI param

### Support

Please send Satoshis so I can feed my plants

https://getalby.com/p/proudforest149266
