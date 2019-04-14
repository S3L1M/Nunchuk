# nLib
A Python library for reading nunchuk accelerometer data on RaspberryPi 3

## Hello World example
``` 
from nLib import nunchuck

x = nunchuck()
while True:
  print x.getData()
```

** You can specify the delay between readings in nunchuk constructor `x = nunchuk(delay)`
