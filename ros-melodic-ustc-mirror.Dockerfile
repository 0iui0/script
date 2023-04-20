# Use the official ROS Melodic image as a parent image

FROM osrf/ros:melodic-desktop-full

# Set environment variables for nvidia-container-runtime

ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}

ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# Copy the original sources.list file to sources.list.ori

RUN cp /etc/apt/sources.list /etc/apt/sources.list.ori

# Replace the default sources.list with the USTC mirror

RUN sed -i 's@//.*archive.ubuntu.com@//mirrors.ustc.edu.cn@g' /etc/apt/sources.list

RUN sed -i 's/security.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

RUN sed -i 's/packages.ros.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list

RUN sed -i 's/packages.ros.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/ros1-latest.list

RUN echo "deb https://mirrors.aliyun.com/nvidia-cuda/ubuntu1804/x86_64/ /" >> /etc/apt/sources.list

# Import the ROS GPG key

RUN gpg --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

RUN gpg --export C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654 | sudo tee /usr/share/keyrings/ros.gpg > /dev/null

RUN apt-key adv --fetch-keys https://mirrors.aliyun.com/nvidia-cuda/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-key adv --fetch-keys https://mirrors.aliyun.com/nvidia-cuda/ubuntu1804/x86_64/3bf863cc.pub

# Clean up the apt cache

RUN apt clean && apt -y update
