import can
import cantools
import unittest


#NOTE: ChatGPT uses outdate information sometimes.

#Could Create two virtual bus instances on the same channel to communicate or one loop back:
    #bus1 = can.interface.Bus(interface='virtual', channel='vcan0')

#Loads the dbc file.
    #db = cantools.database.load_file("all_SRE.dbc")


class CanTests(unittest.TestCase):

    #NOTE: all tests should be prefaced with "test" in method name. Tests are ALSO ran synchronously.

    #Essentially calls at the beginning of every method.
    def setUp(self):
        self.bus = can.interface.Bus(interface='virtual', receive_own_messages=True)
        self.db = cantools.database.load_file("./backEndComponentLogic/canTest/all_SRETest.dbc")

    #Will only be called at the end of each method IF setup method succeeds to be called at beginning.
    def tearDown(self):
        #Shuts down bus.
        self.bus.shutdown()

    def test_receive_simpleMessage(self):
        print("Test 1:")

        # Send a test message
        msg = can.Message(arbitration_id=0x123, data=[0x01, 0x01, 0x01], is_extended_id=False)
        self.bus.send(msg)
        print(f"Sent message: {msg}")

        # Receive the same message (loopback mode)
        received_msg = self.bus.recv(timeout=1.0)  # Wait for a message for a max 1 second, if deson't receive, output None.

        print(f"Received message: {received_msg}")


        # Check if the message was received correctly
        assert received_msg is not None
        assert received_msg.arbitration_id == msg.arbitration_id
        assert received_msg.data == msg.data

        print("Message sent and received successfully! \n")

    def test_EMeter_Measurement_Message(self):
        print("Test 2:")

        #sends message relating to EMeter_Measurement values.
        msg = can.Message(arbitration_id=256, data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        
        self.bus.send(msg)
        print(f"Sent message: {msg}")

        # Receive the same message (loopback mode)
        received_msg = self.bus.recv(timeout=1.0)  # Wait for a message for a max 1 second, if deson't receive, output None.

        print(f"Received message: {received_msg}")

        #Verifies the information has been received.
        assert received_msg is not None
        assert received_msg.arbitration_id == msg.arbitration_id
        assert received_msg.data == msg.data

        decoded = self.db.decode_message(msg.arbitration_id, msg.data)

        print(f"Decoded message: {decoded}")

        #Asserts that the received information is 0 current and 0 voltage.
        self.assertEqual(decoded["EMeter_Current"], 0) 
        self.assertEqual(decoded["EMeter_Voltage"], 0)

#should create a test that can verify if bus can take and process all of the CAN data.
if __name__ == '__main__':
    unittest.main()