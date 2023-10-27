import serial
import time

class SDI12Sensor:
    def __init__(self, serial_port, address):
        self.serial_port = serial_port
        self.address = address
        self.ser = None

    def connect(self):
        self.ser = serial.Serial(self.serial_port, 1200, timeout=1)

    def send_command(self, command):
        self.ser.write(f'{self.address}{command}\r'.encode())
        self.ser.flush()

    def read_response(self):
        response = ''
        while True:
            char = self.ser.read().decode()
            if char == '\r':
                break
            response += char
        return response

    def close(self):
        self.ser.close()

if __name__ == "__main__":
    sensor = SDI12Sensor('/dev/ttyUSB0', '0')
    sensor.connect()

    try:
        sensor.send_command('M!')
        time.sleep(1)
        response = sensor.read_response()
        print("Sensor response:", response)

    except Exception as e:
        print("Error:", str(e))

    finally:
        sensor.close()
