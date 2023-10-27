import grpc
import sensorservice_pb2
import sensorservice_pb2_grpc
import pytest

def test_sensor_service():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = sensorservice_pb2_grpc.SensorServiceStub(channel)
        sensor_id = "Sensor001"
        request = sensorservice_pb2.GetSensorDataRequest(sensor_id=sensor_id)
        response = client.GetData(request)
        assert response.data == f"Sensor data for sensor {sensor_id}"

if __name__ == "__main__":
    pytest.main(["-s", "test_sensor_service.py"])
