from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import serial

#ser = serial.Serial('COM3', 9600)

# Открытие конфигурационного файла
f = open("config.json", "r")
config = json.load(f)
num_lamps = config["num_lamps"]

# Начальные значения
n = 100  # Уровень батареи
m = 25   # Температура

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global n, m
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        if self.path == "/bat":
            self.wfile.write((str(n) + " ").encode())  # Отправка уровня батареи
            n -= 1
            print(f"Батарея: {n}")
        #   ser.write(b'e')

        #             #temp = ser.readline()
        #             # print(temp)
        #             # s = "bat:" + str(n) + ";temp:" + str(temp) + ";"
        #             # self.wfile.write(str.encode(str(s)))
        #         elif self.path == "/temp":
        #             global m
        #             self.wfile.write(str.encode(str(m)))  # Ответ для запроса уровня батареи
        #             print(str.encode(str(m)))
        #             m -= 1
        #             print(m)
        #             #ser.write(b'e')
        #
        #             #temp = ser.readline()
        #             # print(temp)
        #             # s = "bat:" + str(n) + ";temp:" + str(temp) + ";"
        #             # self.wfile.write(str.encode(str(s)))
        #
        elif self.path == "/temp":
            self.wfile.write((str(m) + " ").encode())       # Отправка текущей температуры
            print(f"Температура: {m}")

        elif self.path.startswith("/temp_update"):
            # Извлекаем новое значение температуры из URL
            try:
                new_temp = int(self.path.split("=")[1])
                m = new_temp
                print(f"Температура обновлена: {m}")
                self.wfile.write(b"OK")  # Подтверждение обновления
            except (IndexError, ValueError):
                self.wfile.write(b"ERROR")  # Ошибка при обработке

        elif self.path == "/config":
            self.wfile.write(str(num_lamps).encode())  # Отправка количества ламп

        elif self.path == "/lamp1_on":
            print("Лампа 1: Включена")
            self.wfile.write(b"OK")  # Ответ на включение лампы 1
            # ser.write(b'a')
        elif self.path == "/lamp1_off":
            print("Лампа 1: Выключена")
            self.wfile.write(b"OK")  # Ответ на выключение лампы 1
            # ser.write(b'c')

        elif self.path == "/lamp2_on":
            print("Лампа 2: Включена")
            self.wfile.write(b"OK")
            # ser.write(b'b')
        elif self.path == "/lamp2_off":
            print("Лампа 2: Выключена")
            self.wfile.write(b"OK")
            # ser.write(b'd')

        elif self.path == "/lamp3_on":
            print("Лампа 3: Включена")
            self.wfile.write(b"OK")
        elif self.path == "/lamp3_off":
            print("Лампа 3: Выключена")
            self.wfile.write(b"OK")

server_address = ('172.20.10.3', 8000)
httpd = HTTPServer(server_address, MyHandler)

print("Starting server on port 8000...")
httpd.serve_forever()



# class MyHandler(SimpleHTTPRequestHandler):
#   def do_GET(self):
#     print(self.path)
#
#     self.send_response(200)
#     self.send_header('Content-type', 'text/html')
#     self.end_headers()
#
#     # if self.path == "/config":
#     #     with open("config.json", "r") as f:
#     #         config = json.load(f)
#     #         num_lamps = config["num_lamps"]
#     #         self.wfile.write(str(num_lamps).encode())
#     #     return
#
#     if self.path == "/bat":
#         self.wfile.write(b"56")
#
#         if self.path == "/lamp1_on":
#             print("ВКЛ 1 лампу")
#         elif self.path == "/lamp1_off":
#             print("ОТКЛ 1 лампу")
#         elif self.path == "/lamp2_on":
#             print("ВКЛ 2 лампу")
#         elif self.path == "/lamp2_off":
#             print("ОТКЛ 2 лампу")
#         elif self.path == "/lamp3_on":
#             print("ВКЛ 3 лампу")
#         elif self.path == "/lamp2_off":
#             print("ОТКЛ 3 лампу")
#
#     # for i in range(1, num_lamps):
#     #     if self.path == "/lamp" + str(i) + "_on":
#     #         print("LAMP " + str(i) + " ON")
#     #         ser.write(b'a')
#     #     if self.path == "/lamp" + str(i) + "_off":
#     #         print("LAMP " + str(i) + " OFF")
#     #         ser.write(b'b')
