from pyJunosManager import JunosDevice

#template variables are added to a dict or dictionary. A dict is simply a key/value store data structure
my_variables = {"hostname":"CoreDev","enc_password":"$1$MwLiep8p$l5g17Euco.AqvBH5Kd/VC/","ssh_root_login":"allow"}

#lets read in the file
#first we open in in read only mode
tmpl_file = open("jnpr-config.tmpl","r")
#next we read all the data into a variable
tmpl_data = tmpl_file.read()
#lastly we close the file since we are done reading it
tmpl_file.close()

#now lets connect to the device, load the template, and commit the changes
#first we instantiate an instance of the device
junos_dev = JunosDevice(host="172.16.237.12",username="root",password="Juniper")
#now we can connect to the device
junos_dev.open()
#we then open the configuration
junos_dev.open_config()
#lets go ahead and load the configuration.
junos_dev.load_config_template(tmpl_data,my_variables)
#commit and close the config
junos_dev.commit_and_quit()
#lastly we close the connection to the device
junos_dev.close()
