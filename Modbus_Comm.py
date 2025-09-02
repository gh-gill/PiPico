import time
from machine import Pin, UART
from umodbus.serial import Serial as ModbusRTUMaster

# Define the pins for Modbus communication
rtu_pins = (Pin(0), Pin(1))

# Define the starting address to read from
starting_address = 0

# Define the quantity of registers to read
qty = 8

# Initialize Modbus RTU Master
host = ModbusRTUMaster(baudrate=9600, data_bits=8, stop_bits=1, parity=None, pins=rtu_pins, ctrl_pin=None, uart_id=0)

# Continuous reading loop
while True:
    try:
        print('INPUT REGISTER request test.')
        print('Reading qty={} from starting address {}:'.format(qty, starting_address))
        
        # Read inputs from the slave device
        mB_slave1_In = host.read_discrete_inputs(slave_addr=1, starting_addr=0, input_qty=8)
        mB_slave1_Out = host.read_coils(slave_addr=1, starting_addr=0, coil_qty=8)
        #values = host.read_coils(slave_addr=1, starting_addr=10007, coil_qty=1)
        #values = host.read_input_registers(slave_addr=1, starting_addr=starting_address, register_qty=qty, signed=False)
        # Print the result
        print('mB_slave1_In Result: {}'.format(mB_slave1_In))
        print('mB_slave1_Out Result: {}'.format(mB_slave1_Out))
        
        print("mB_slave1_Out0 Status:", mB_slave1_Out[7]) 
        if mB_slave1_Out[7] == True:
            mB_slave1_Out0 = 0
        else:
            mB_slave1_Out0 = 1
            
        Set_mB_slave1_Out0 = host.write_single_coil(slave_addr=1, output_address=0, output_value=mB_slave1_Out0)

    except Exception as e:
        print('An error occurred:', e)

    # Wait for 5 seconds before the next reading
    time.sleep(5)

