import socket
import numpy as np
import sys
import config
import os
from config import PATH
from spcy import *
from transcript import *

HOST = socket.gethostname()

def send_data(loss):
    
    data = loss.encode()

    conn.sendall(data)
    return True


node_word = str(sys.argv[1])
if node_word is not None:
    track_word = node_word

else:
    track_word = "kabul"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), config.PORT))
print("connected")
losses = []
full_msg = b''


while s:
    try:
        encoded_data = track_word.encode()
        s.sendall(encoded_data)
        print("track word sent")
        while True:
            data = s.recv(21)

            decoded_data = float(data.decode())
            full_msg = b''
            losses.append(decoded_data)

            array_losses = np.asarray(losses)
            mod_array = array_losses.copy()

            mod_array[mod_array >= 5] = -1
            anomalies = np.count_nonzero(mod_array == -1)
            std = np.std(array_losses)
            mean = np.mean(array_losses)
            anomaly_percentage = (anomalies/len(losses)) * 100

           
            if anomaly_percentage < 20:
                
                sys.stdout.write("0")
            elif 20 <= anomaly_percentage < 40:
                
                sys.stdout.write("1")
            else:
                sys.stdout.write("2")
            sys.stdout.flush()

    except KeyboardInterrupt:
        if s:
            s.close()
            print("connection closed")
            break