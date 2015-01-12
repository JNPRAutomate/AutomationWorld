from jnpr.junos import Device
from jnpr.junos.utils.config import Config

#template variables are added to a dict or dictionary. A dict is simply a key/value store data structure
my_variables = {"hostname":"JNPRConfig-ez-set","enc_password":"$1$MwLiep8p$l5g17Euco.AqvBH5Kd/VC/","ssh_root_login":"allow"}

#now lets connect to the device, load the template, and commit the changes
#first we instantiate an instance of the device
junos_dev = Device(host='172.16.237.128', user='root', password='Juniper' )
#We must bind an empty configuration to the device
junos_dev.bind(cu=Config)
#now we can connect to the device
junos_dev.open()
#lets go ahead and load the configuration. We are reading fromt he local directory and specifying the jnpr-config.conf file
#the file exension specifies the config type of config stored in the file
junos_dev.cu.load(template_path="./set-config.set",merge=True,template_vars=my_variables)
#commit and close the config
commit_result = junos_dev.cu.commit()
#Show that the commit worked True means it worked, false means it failed
print commit_result
#lastly we close the connection to the device
junos_dev.close()
