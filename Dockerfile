FROM python:3.9-slim
RUN pip install fastapi uvicorn 
COPY ./ /
CMD [ "uvicorn", "index:app", "--host", "0.0.0.0", "--port", "15400" ]


