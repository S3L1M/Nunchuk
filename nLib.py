from smbus import SMBus
import RPi.GPIO as rpi
import time

class nunchuk:

  def __init__(self,delay = 0.05):
    self.delay = delay
    self.bus = SMBus(1)
    self.bus.write_byte_data(0x52,0xF0,0x55)
    time.sleep(0.1)
    self.bus.write_byte_data(0x52,0xFB,0x00)
    time.sleep(0.1)

  def read(self):
    self.bus.write_byte(0x52,0x00)
    time.sleep(self.delay)
    temp = [self.bus.read_byte(0x52) for i in range(6)]
    return temp

  def getData(self):
    data = self.read()
    return { 
      "accel": (data[2], data[3], data[4]),
      "btn":   ((data[5]&0x02)!=2, (data[5]&0x01)!=1),
      "joystk": (data[0],data[1])
    }


### FOR_FUTURE: ADD def AsyncDataListen()

