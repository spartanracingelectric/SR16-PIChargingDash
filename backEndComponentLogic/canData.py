#This file should receive CAN data and then be allowed to pass it to graphing components.
#Use python-can to receive live CAN data and cantools to decode/encode CAN data.
import can
import cantools


#Below is a series of statements that can be formatted for a single method.

# Load DBC file (optional for decoding)
db = cantools.database.load_file("./backEndComponentLogic/all_SRE.dbc")

# Initialize CAN bus (Raspberry Pi using SocketCAN)
#Use "with" keyword
    #Interface: The hardware or software that connects to the CAN bus. 
    #Channel: A specific CAN connection managed by an interface. 
    #Bitrate: The data transmission speed (bits per second) on the CAN bus. 
    #can_filters: set filters based on array given.

#Apply can filter for selected information. 
bus = can.interface.Bus(channel="can0", bustype="socketcan")



print("Listening for CAN messages...")

#How the bus works here: sends many messages throughout time, and one message at one time. 
#to identify message being sent, query their IDS using a switch statement etc.

# If the software reads messages slowly, the buffer may overflow, causing packet loss.
# You can use asynchronous reception (threaded approach) to prevent message loss:

#Use can.Notifier as it's async and non-blocking


try:
    while True:

        #recv is synchronous: so message maybe missed.
        msg = bus.recv()  # Receive CAN message, check notes of what msg has.
        print(f"Raw Message: {msg}")

        try:
            decoded = db.decode_message(msg.arbitration_id, msg.data)
            print(f"Decoded: {decoded}")
        except KeyError:
            print(f"Unknown CAN ID: {msg.arbitration_id}")

except KeyboardInterrupt:
    print("Stopped.")

bus.shutdown()