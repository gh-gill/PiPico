from umodbus.serial import Serial as ModbusRTUMaster

# RTU Host/Master setup

# the following definition is for a RP2
rtu_pins = (Pin(0), Pin(1))     # (TX, RX)
uart_id = 0
#
# rtu_pins = (Pin(4), Pin(5))     # (TX, RX)
# uart_id = 1

host = ModbusRTUMaster(
    pins=rtu_pins,          # given as tuple (TX, RX)
    # baudrate=9600,        # optional, default 9600
    # data_bits=8,          # optional, default 8
    # stop_bits=1,          # optional, default 1
    # parity=None,          # optional, default None
    # ctrl_pin=12,          # optional, control DE/RE
    uart_id=uart_id         # optional, default 1, see port specific documentation
)

#Supported Modbus functions
# ID    Description
# 1     Read coils 
# 2     Read discrete inputs
# 3     Read holding registers
# 4     Read input registers
# 5     Write single coil
# 6     Write single register
# 15    Write multiple coils
# 16    Write multiple registers

# 0x01 read_coils
# 0x02 read_discrete_inputs
# 0x03 read_holding_registers
# 0x04 read_input_registers
# 0x05 write_single_coil
# 0x06 write_single_register
# 0x0F write_multiple_coils
# 0x10 write_multiple_registers

# reading one coil returns a list of 1 boolean element
# host.read_coils(slave_addr=10, starting_addr=123, coil_qty=1)
# [True]
# reading 3 coils returns a list of 3 boolean elements
# host.read_coils(slave_addr=10, starting_addr=126, coil_qty=3)
# [False, True, False]

coil_status = host.read_coils(slave_addr=10, starting_addr=123, coil_qty=1)
print('Status of coil 123: {}'.format(coil_status))
time.sleep(1)
# WRITE COILS
new_coil_val = 0
coil_status = host.write_single_coil(slave_addr=10, output_address=123, output_value=new_coil_val)
print('Result of setting COIL 123: {}'.format(coil_address, operation_status))
time.sleep(1)

