import struct
from datetime import datetime

class VendingMachineParser:
    CMD_TEMP = 100
    CMD_DOOR = 101
    CMD_DISP = 102

    def __init__(self):
        self.last_temperature = None
        self.door_open_time = None
        self.packet_started = False
        self.packet = bytearray()

    def read_byte(self, byte):
        if self.packet_started:
            self.packet.append(byte)
            if byte == 0xC0:  # Final Flag
                self._parse_packet(self.packet)
                self.packet = bytearray()
                self.packet_started = False
        else:
            if byte == 0xC0:  # First Flag
                self.packet.append(byte)
                self.packet_started = True

    def _parse_packet(self, packet):
        # print(f">> DBG: packet: {packet}")
        initial_flag, timestamp_bytes, data, error_check, final_flag = (
            packet[0],
            packet[1:5],
            packet[5:-2],
            packet[-2],
            packet[-1],
        )

        if not (initial_flag == final_flag == 0xC0):
            self._log_packet_error(packet)
            return

        timestamp = struct.unpack('>I', timestamp_bytes)[0]
        data = data.replace(b'\xDB\xDC', b'\xC0').replace(b'\xDB\xDD', b'\xDB')
        # print(f">>DBG: error_check {error_check}")
        if self._calc_checksum(packet) != error_check:
            self._log_packet_error(packet)
            return

        command_code, *payload = data.split(b',')
        command_code = int(command_code)
        payload = [part.decode() for part in payload]

        if command_code == self.CMD_TEMP:
            self._handle_temperature(payload)
        elif command_code == self.CMD_DOOR:
            self._handle_door_sensor(timestamp)
        elif command_code == self.CMD_DISP:
            self._handle_product_dispense(payload, timestamp)
    
    @staticmethod
    def _calc_checksum(packet):
        # print(f">> DBG: error check: {sum(packet[:-2]) % 256}")
        return sum(packet[:-2]) % 256
    
    def _handle_temperature(self, payload):
        temperature = float(payload[0])
        if self.last_temperature is None or abs(temperature - self.last_temperature) >= 2.5:
            self.last_temperature = temperature
            timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            print(f"TEMPERATURE: {temperature} ({timestamp})")

    def _handle_door_sensor(self, timestamp):
        if self.door_open_time is None:
            self.door_open_time = timestamp
        else:
            door_open_duration = timestamp - self.door_open_time
            timestamp_str = datetime.fromtimestamp(self.door_open_time).strftime('%d/%m/%Y %H:%M:%S')
            print(f"MAINTENANCE_SESSION: {door_open_duration} seconds ({timestamp_str})")
            self.door_open_time = None

    def _handle_product_dispense(self, payload, timestamp):
        shelf = payload[0]
        channel = payload[1]
        timestamp_str = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')
        print(f"PRODUCT_VEND: shelf {shelf}, channel {channel} ({timestamp_str})")

    def _log_packet_error(self, packet):
        print(f"PACKET_ERROR: {packet.hex()}")