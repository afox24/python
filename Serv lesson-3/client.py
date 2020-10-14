# Программа - клиент
import sys
import json
import socket
import time

from helper.variables import (
    ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR,
    DEFAULT_IP_ADDRESS, DEFAULT_PORT, MAX_PACKAGE_LENGTH, ENCODING
)


class ClientSocket:
    def __init__(self, af_inet, sock_stream, account_name='Guest'):
        self.inet = af_inet
        self.stream = sock_stream
        self.account_name = account_name

    def create_socket(self):
        return socket.socket(self.inet, self.stream)

    def create_presence(self):
        # Функция генерирует запрос о присутствии клиента
        # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
        out = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: self.account_name
            }
        }
        return out

    def get_message(self, client):
        """
         Утилита приёма и декодирования сообщения
        принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
        """
        encoded_response = client.recv(MAX_PACKAGE_LENGTH)
        if isinstance(encoded_response, bytes):
            json_response = encoded_response.decode(ENCODING)
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError

    def send_message(self, sock, message):
        # Утилита кодирования и отправки сообщения принимает словарь и отправляет его
        js_message = json.dumps(message)
        encoded_message = js_message.encode(ENCODING)
        sock.send(encoded_message)

    def process_ans(self, message):
        # Функция разбирает ответ сервера
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200 : OK'
            return f'400 : {message[ERROR]}'
        raise ValueError


def main():
    # Загружаем параметы коммандной строки
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен
    cs = ClientSocket(socket.AF_INET, socket.SOCK_STREAM)
    sock = cs.create_socket()
    sock.connect((server_address, server_port))
    message_to_server = cs.create_presence()
    cs.send_message(sock, message_to_server)
    try:
        answer = cs.process_ans(cs.get_message(sock))
        print(f'Server response: {answer}')
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()