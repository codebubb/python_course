import os
import _winreg
print "-" * 34
print "|", " " * 30, "|"
print "| Operating System Information   |"
print "|", " " * 30, "|"
print "| Find data about this machine   |"
print "|", " " * 30, "|"
print "-" * 34

print "Computer name        :\t", os.environ["COMPUTERNAME"]
print "Operating system     :\t", os.environ["OS"]
print "Processor type       :\t", os.environ["PROCESSOR_IDENTIFIER"]
print "Number of processors :\t", os.environ["NUMBER_OF_PROCESSORS"]

print "-" * 34
print "| BIOS Information               |"
print "-" * 34
local_machine_reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "HARDWARE\\DESCRIPTION\\System\\BIOS")
key_info = _winreg.QueryInfoKey(local_machine_reg)
for i in range(key_info[1]):
    print _winreg.EnumValue(local_machine_reg, i)
