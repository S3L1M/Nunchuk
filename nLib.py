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
    return [self.bus.read_byte(0x52) for i in range(6)]

  def getData(self):
    d = self.read()
    return {
      "accel": (d[2]+(d[5]>>2&3), d[3]+(d[5]>>2&3), d[4]+(d[5]>>6)),
      "btn":   (d[5]&2!=2, d[5]&1!=1),
      "joystk":(d[0],d[1])
    }


  
### FOR_FUTURE: ADD def AsyncDataListen()
