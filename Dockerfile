#  base image 
FROM python:3.10-slim 

# working directory inside container 
WORKDIR /app 

# copy files 
COPY requirements.txt .        

#  install dependincy 
RUN pip install --no-cache-dir -r requirements.txt 

# copy all files.. 
COPY . .   

# expose port 
EXPOSE 8000 

# run application 
CMD ["python","app.py"]