import serial
import time
import arena

def scene_callback(msg):
    print("scene_callback: ", msg)

def arena_init(temp_hum_readings):
    arena.init("arena.andrew.cmu.edu", "realm", "patrick_scene", scene_callback)
    deg = "0"
    hum = "0"
    text = arena.Object(
        objName = "text_1",
        objType = arena.Shape.text,
        color = (255, 0, 0),
        location = (-1, 2, -3),
        text = "Hello world! It's currently " + deg + " degrees with a humidity of: " + hum
    )
    time.sleep(5)
    for pair in temp_hum_readings:
        text.update(text = "Hello world! It's currently " + pair[0] + " degrees with a humidity of: " + pair[1])
        time.sleep(1)
    # text.update(text = "Based")

    arena.handle_events()


def start_serial():
    # set up the serial line
    ser = serial.Serial('COM6', 9600)
    time.sleep(2)

    # Read and record the data
    temperature_readings = []
    humidity_readings = []
    for i in range(15):
        b = ser.readline()  # read a byte string
        string_n = b.decode()  # decode byte string into Unicode
        string = string_n.rstrip()  # remove \n and \r

        if (string):
            # print(string)
            if (string[0] == "T"):
                temperature_readings.append(string)
            elif (string[0] == "H"):
                humidity_readings.append(string)

        time.sleep(0.1)  # wait (sleep) 0.1 seconds

    ser.close()

    return zip(temperature_readings, humidity_readings)

if __name__ == '__main__':
    readings = start_serial()
    arena_init(readings)

