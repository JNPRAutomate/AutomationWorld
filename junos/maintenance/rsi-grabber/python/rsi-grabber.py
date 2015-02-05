from jnpr.junos import Device
import xml.etree.ElementTree as ET

#now lets connect to the device, load the template, and commit the changes
#first we instantiate an instance of the device
junos_dev = Device(host='172.16.237.128', user='root', password='Juniper' )
#now we can connect to the device
junos_dev.open()
#run the RPC to get the support information
rsi_output = junos_dev.rpc.get_support_information()
#output to a sting
print ET.tostring(rsi_output,encoding="utf8", method="text")
#lastly we close the connection to the device
junos_dev.close()
