# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requeriments.txt .

# install dependencies
RUN pip install -r requeriments.txt

# copy the content of the local src directory to the working directory
COPY . .


EXPOSE 80
CMD ["sh", "start.sh"]