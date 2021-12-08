import threading
import time
import queue
import Infrared_camera
import Lux_Humidity_Pressure_temper_Altitude

def multipro():
    Infrared_thread = threading.Thread(target = Infrared_camera.data_Infrared_camera)
    Lux_thread = threading.Thread(target = Lux_Humidity_Pressure_temper_Altitude.data_Lux)
    
    Lux_thread.start()
    Infrared_thread.start()
    
    Lux_thread.join()
    Infrared_thread.join()
    

multipro()
    