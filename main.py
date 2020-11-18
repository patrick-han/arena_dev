import serial
import time
import arena

def scene_callback(msg):
    print("scene_callback: ", msg)

def arena_init():
    arena.init("arena.andrew.cmu.edu", "realm", "patrick_scene", scene_callback)

    temperature_text = arena.Object(
        objName = "temperature_text",
        objType = arena.Shape.text,
        color = (255, 0, 0),
        location = (-1, 2, -3),
        text = "Hello world! The temperature is: 0"
    )
    humidity_text = arena.Object(
        objName="humidity_text",
        objType=arena.Shape.text,
        color=(255, 0, 0),
        location=(-1, 1, -3),
        text="Hello world! The humidity is: 0"
    )
    start_serial(temperature_text, humidity_text)
    arena.handle_events()


def start_serial(temperature_text_obj, humidity_text_obj):
    # set up the serial line
    ser = serial.Serial('COM6', 9600)
    time.sleep(2)

    while (True):
        b = ser.readline()
        string_n = b.decode()
        string = string_n.rstrip()
        if (string):
            if (string[0] == "T"):
                temperature_text_obj.update(text = "The temperature is: " + string)
            elif (string[0] == "H"):
                humidity_text_obj.update(text = "The humidity is: " + string)
            print(string)

        time.sleep(0.1)

    ser.close()

if __name__ == '__main__':
    arena_init()
