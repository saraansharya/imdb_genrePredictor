#python 3.8 lambda base image
#FROM amazon/aws-lambda-python:3.8
FROM public.ecr.aws/lambda/python:3.8.2021.12.18.01-x86_64
COPY . .

#copying to container
COPY requirements.txt ./

#installing dependencies
RUN pip3 install -r requirements.txt

#copying function code
COPY app1.py ./

#copying model code
COPY runModel1.py ./

#copying models
COPY . /models_BOW ./models_BOW

#setting CMD to handler file_name.function_name
CMD [ "app1.handler" ]
