FROM python:3.8

RUN apt update
RUN apt install python3

# set the working directory in the container
WORKDIR C:\Users\anisi\OneDrive\Documents\M1-EFREI\Devops\TP1devops

COPY TP1.py ./

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python3", "./TP1.py" ]