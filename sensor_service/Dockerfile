FROM python:3.8
WORKDIR /app
COPY sensor_service.proto .
COPY sensor_service.py .
RUN pip install grpcio
RUN python -m grpc_tools.protoc --python_out=. --grpc_python_out=. sensor_service.proto
EXPOSE 50051
CMD ["python", "sensor_service.py"]
