# FROM python:3.7

# COPY . /web
# WORKDIR /web
# RUN pip install -r ./requirements.txt
# WORKDIR /web
# ENTRYPOINT ["python"]
# WORKDIR /web
# CMD ["/web/Database/sqlalchemy_test.py"]


##From web
# https://forums.docker.com/t/issue-with-installing-pip-packages-inside-a-docker-container-with-ubuntu/35107/3
# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
WORKDIR /web

# Copy the current directory contents into the container at /app
ADD . /web

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "/web/Database/sqlalchemy_test.py"]