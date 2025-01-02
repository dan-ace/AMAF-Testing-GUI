import tkinter
import customtkinter as ctk # <- import the CustomTkinter module                                                                                                                      
from tkinter import filedialog
import socket
import multiprocessing
import numpy as np
import os
import os.path
import subprocess
import json
from datetime import datetime
import time

def process_messages(queue):
    while True:
        client_socket, message = queue.get()
        print(f"Processing message: {message}")
        response = f"Echo: {message}"
        client_socket.send(response.encode())


def handle_client_connections(client_socket, client_address, queue):
    print(f"Connected by {client_address}")
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        queue.put((client_socket, message))
    client_socket.close()


if __name__=="__main__":

    # Server setup
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening on port 12345")

    # Create a message queue
    message_queue = multiprocessing.Queue()

    # Create and start the message processing process
    message_processor = multiprocessing.Process(target=process_messages, args=(message_queue,))
    message_processor.start()

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = multiprocessing.Process(target=handle_client_connection, args=(client_socket, client_address, message_queue))
        client_handler.start()

