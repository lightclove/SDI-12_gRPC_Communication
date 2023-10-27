FROM python:3.8
WORKDIR /app
COPY client_service.py .
RUN pip install grpcio
EXPOSE 8080
CMD ["python", "client_service.py"]
