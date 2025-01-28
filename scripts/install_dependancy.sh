curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
yum install git -y
cd /home/ssm-user
git clone https://github.com/puru-aws/sample-app-e2e-testing.git
cd sample-app-e2e-testing
python3 -m pip install -r requirements.txt