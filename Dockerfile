#Create a ubuntu base image with python 3 installed.
FROM python:3

#Set the working directory
WORKDIR /usr/src/app

#copy all the files
COPY . .

#Install the dependencies
RUN apt-get -y update
RUN pip3 --disable-pip-version-check install -r requirements.txt

#Expose the required port
EXPOSE 5058

#Run the command
CMD ["python3", "./app.py"]
