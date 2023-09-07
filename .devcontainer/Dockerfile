# ubuntu base image
FROM ubuntu:20.04

# install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    libgl1-mesa-glx 

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y libglib2.0-0

# clean cache 
RUN apt-get clean

# point "python3" to "python"
RUN ln -s /usr/bin/python3 /usr/bin/python

# add a a new user "guest"
RUN useradd -ms /bin/bash guest
ENV PATH="/home/guest/.local/bin:$PATH"
USER guest

