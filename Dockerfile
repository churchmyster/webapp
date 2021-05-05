From python:3.10.0a7-buster

#Working Directory
WORKDIR /app

#Copy contents into working directory
ADD . /app

# Install Dependencies
RUN pip3 install -r requirements.txt

#Define command to start container
CMD ["python3","app.py"]