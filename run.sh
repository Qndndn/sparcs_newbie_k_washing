curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
apt update
apt install python3-distutils -y
python3 get-pip.py
pip install -r requirements.txt