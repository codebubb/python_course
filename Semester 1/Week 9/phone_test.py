from phone import Phone
from iphone import iPhone

simple_phone = Phone(80, 60, 32, 3.8)

print simple_phone.battery_life
print simple_phone.signal_strength
print simple_phone.memory_size
print simple_phone.screen_size

print "*"*20

iphone = iPhone(90, 60, 16)
print iphone.battery_life
print iphone.signal_strength
print iphone.memory_size
print iphone.screen_size
iphone.switch_on()
iphone.updateiTunes()
