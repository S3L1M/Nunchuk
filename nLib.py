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

  def extractAccelData(data):
    x = data[2]+(d[5]>>2&3)
    y = data[3]+(d[5]>>2&3)
    z = data[4]+(d[5]>>6)
    x=x-128 if x>127 else x=x*-1
    y=y-128 if x>127 else y=x*-1
    z=z-128 if x>127 else z=x*-1
    return (x, y, z)

  def getData(self):
    local = self.read()
    return {
      "accel": self.extractAccelData(local),
      "btn":   (local[5]&2!=2, local[5]&1!=1),
      "joystk":(local[0],local[1])
    }


  
### FOR_FUTURE: ADD def AsyncDataListen()
