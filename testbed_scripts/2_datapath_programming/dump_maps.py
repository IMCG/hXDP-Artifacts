#!/usr/bin/python3

import os
import sys
import subprocess

FNULL = open(os.devnull, "w")

if len(sys.argv) < 2:

	MAX_LINES = 256
else:
	MAX_LINES = int(sys.argv[1])

map_select = "1"

print("Reaing from", map_select, "PER_CPU Map")

print (map_select)


# Test presence of NetFPGA
retcode = subprocess.call(["./rwaxi"], stdout=FNULL, stderr=subprocess.STDOUT)

if retcode == 1:
    print ("ERROR: NetFPGA-SUME not available on this system")
    exit(-1)

else:
    print("NetFPGA-SUME Detected")

############ READ FROM AXI ADDRESS FUNCTION ###############
def read_axi_addr(addr):
	result = subprocess.Popen(["./rwaxi", "-a", addr], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	readed_value = result.communicate()
	#print (readed_value[0].decode('utf-8').rstrip())
	return readed_value[0][2:].decode('utf-8').rstrip()
###########################################################

line_selector = 0

for i in range (0, MAX_LINES):
	if (i < 10):
		print(str(hex(i)),":\t", read_axi_addr("0x800"+map_select+"0"+str(hex(i)[2:])+"1c") + read_axi_addr("0x800"+map_select+"0"+str(hex(i)[2:])+"18"),"|",
			read_axi_addr("0x800"+map_select+"0"+str(hex(i)[2:])+"14") + read_axi_addr("0x800"+map_select+"0"+str(hex(i)[2:])+"10"), "|")
	else:
		print(str(hex(i)),":\t", read_axi_addr("0x80"+map_select+"0"+str(hex(i)[2:])+"1c") + read_axi_addr("0x80"+map_select+"0"+str(hex(i)[2:])+"18"),"|",
			read_axi_addr("0x80"+map_select+"0"+str(hex(i)[2:])+"14") + read_axi_addr("0x80"+map_select+"0"+str(hex(i)[2:])+"10"), "|")
		
