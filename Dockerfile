FROM python:3.9.11-alpine3.14

# set a directory for the app
WORKDIR /home/stackfaq

# copy requirement files
COPY requirements.txt /home/stackfaq/requirements.txt

# install dependencies
RUN pip3 install -r requirements.txt

# copy all the files to the container
COPY . /home/stackfaq

# tell the port number the container should expose
EXPOSE 8088

# run the command
CMD ["./gunicorn.sh" ]
