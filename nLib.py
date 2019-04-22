from smbus import SMBus
import RPi.GPIO as rpi
import time
from openpyxl import load_workbook

class nunchuk:
  def __init__(self,delay = 0.001):
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

  def extractAccelData(self, data):
    x = data[2]+(data[5]>>2&3)-128
    y = data[3]+(data[5]>>2&3)-128
    z = data[4]+(data[5]>>6)-128
    return (x, y, z)

  def getAccelData(self):
    local = self.read()
    return self.extractAccelData(local)

  def getData(self):
    local = self.read()
    return {
      "accel": self.extractAccelData(local),
      "btn":   (local[5]&2!=2, local[5]&1!=1),
      "joystk":(local[0],local[1])
    }

  def selectSheet(path, sheetname):
    self.path = path
    self.ws = load_workbook(path)[sheetname]

  def appendToExcl(row):
    self.ws.append(row)

  def saveExcl():
    self.ws.save(self.path)


### FOR_FUTURE: ADD def AsyncDataListen()
