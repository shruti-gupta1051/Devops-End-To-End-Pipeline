#start from the base image 
FROM python:3.10-slim

#setup the working directory in container
WORKDIR /app

#copy requiremnets to container
COPY requirements.txt .

#install dependecies 
RUN pip install --no-cache-dir -r requirements.txt

#copy code to conatiner
COPY . .

#eport mapping
EXPOSE 5000

#set env
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# run the app 
CMD ["flask","run"]
