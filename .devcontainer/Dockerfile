# ubuntu base image
FROM ubuntu:20.04

ARG USER=guest

# install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    libgl1-mesa-glx

# clean cache 
RUN apt-get clean

# point "python3" to "python"
RUN ln -s /usr/bin/python3 /usr/bin/python

# add a a new user
RUN useradd -ms /bin/bash $USER
# ENV PATH="/home/$USER/.local/bin"
USER $USER

