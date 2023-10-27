# Микросервисы на базе gRPC с использованием Poetry

Этот проект содержит два микросервиса: SensorService и ClientService, которые используют gRPC для обмена данными.

## Инструкции по установке зависимостей, генерации gRPC кода, выполнению тестов и развертыванию контейнеров с микросервисами.

Развертывание и Запуск:

1. Установите Poetry, если его у вас нет:

   ```bash
   pip install poetry

    Для каждого микросервиса выполните следующие команды:

        Войдите в каталог микросервиса (например, sensor_service):

        bash

cd sensor_service

2. Установите зависимости с помощью Poetry:

    ```bash
    poetry install

3. Сгенерируйте gRPC код:

    ```bash
    poetry run python -m grpc_tools.protoc --python_out=. --grpc_python_out=. proto/sensor_service.proto

4. Выполните тесты:

    ```bash
    poetry run pytest -s tests/

5. Запустите микросервис:

    ```bash
    poetry run python sensor_service.py

6. В новой консоли, выполните тесты клиентского микросервиса:
   ```bash
    cd ../client_service
    poetry install
    poetry run pytest -s tests/

7. Запустите клиентский микросервис:
   ```bash
    poetry run python client_service.py

8. Для развертывания микросервисов в Docker, используйте команду:
   ```bash
    docker-compose up

Теперь можно обращаться к ClientService через порт 8080 и получать данные с помощью gRPC от SensorService.
