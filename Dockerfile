FROM simple-classifier-base
WORKDIR /App
COPY . /App
ENTRYPOINT ["python3","app_fasterrcnn_torchvision.py"]