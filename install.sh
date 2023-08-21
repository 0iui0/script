#librealsense2
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0AD9A3000D97B6C9
sudo sh -c 'echo "deb [arch=amd64] http://packages.usenko.eu/ubuntu $(lsb_release -sc) $(lsb_release -sc)/main" > /etc/apt/sources.list.d/basalt.list'
sudo apt-get update
sudo apt install librealsense2-dev

#cuda+tensorrt
wget https://mirrors.aliyun.com/nvidia-cuda/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://mirrors.aliyun.com/nvidia-cuda/ubuntu1804/x86_64/7fa2af80.pub
sudo add-apt-repository "deb https://mirrors.aliyun.com/nvidia-cuda/ubuntu1804/x86_64/ /"
sudo apt-get update
sudo apt-get -y install cuda

#Err:3 https://mirrors.aliyun.com/nvidia-cuda/ubuntu1804/x86_64  InRelease                          
#  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY A4B469963BF863CC

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
