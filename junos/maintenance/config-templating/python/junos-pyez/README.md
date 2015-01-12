The easiest way to load configuration templates
===============================================

The best way to automate Junos utilizing Python is the Junos-PyEZ library. It handles the complex tasks for you, such as netconf connectivity and RPC creation. In the long term this libary is your best option for interacting with Junos outside of configuring the device directly from the CLI.

Example
-------

For this example we are going to take a configuration template and load it onto the device. The template is written in [Jinja](http://jinja.pocoo.org) a simple template language.

### Configuration Template

This example is found within this directory as "jnpr-config.conf".

```
system {
    host-name {{ hostname }};
    root-authentication {
        encrypted-password "{{ enc_password }}";
    }
    services {
        ssh {
            root-login {{ ssh_root_login }};
        }
        netconf {
            ssh;
        }
        web-management {
            http {
                interface ge-0/0/0.0;
            }
        }
    }
}
```

The configuration template is setting up a few management options for us. This would be typical of most organizations and their need to bootstrap devices. In this template we have three defined variables: hostname, enc_password, and ssh_root_login. These variables are contained within a set of special brackets "{{ }}". These brackets tell the Jinja engine that the string within the brackets are the variable names. Once you apply the template to render it replaces the brackets and the name with the data you have chosen. In this case render isn't a complex process that includes 3D textures it simple means to replace these values with the ones I provide.

### Python script

Now that we have taken a look at a basic template, let's look at the program that will be using it. In the below example is the script or program that will be reading in the template.

This example is found within this directory as "jnpr-config.py".

```
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

#template variables are added to a dict or dictionary. A dict is simply a key/value store data structure
my_variables = {"hostname":"JNPRConfig-ez","enc_password":"$1$MwLiep8p$l5g17Euco.AqvBH5Kd/VC/","ssh_root_login":"allow"}

#now lets connect to the device, load the template, and commit the changes
#first we instantiate an instance of the device
junos_dev = Device(host='172.16.237.128', user='root', password='Juniper' )
#We must bind an empty configuration to the device
junos_dev.bind(cu=Config)
#now we can connect to the device
junos_dev.open()
#lets go ahead and load the configuration. We are reading fromt he local directory and specifying the jnpr-config.conf file
#the file exension specifies the config type of config stored in the file
junos_dev.cu.load(template_path="./jnpr-config.conf",merge=True,template_vars=my_variables)
#commit and close the config
commit_result = junos_dev.cu.commit()
#Show that the commit worked True means it worked, false means it failed
print commit_result
#lastly we close the connection to the device
junos_dev.close()
```

#### Alternate configuration templates

Junos supports many different configuration loading types. Previously we showed the standard Junos configuration format. However some users prefer to use the "set" style of commands. Here is an example of loading the set style commands. It is almost identidal to the previous example. There are two differences which are specified below.

This example is found within this directory as "set-config.set".

```
set system host-name {{ hostname }}
set system root-authentication encrypted-password "{{ enc_password }}"
set system services ssh root-login {{ ssh_root_login }}
set system services netconf ssh
set system services web-management http interface ge-0/0/0.0
```

This template varies greatly from the previous example of a Junos config. In this example we use the Junos set commands that are used if you were to manually configure the device. There isn't a specific benefit to either configuration type. Each organization may prefer a different type of configuration to load. Junos gives you the option to load a text config (standard Junos), set config (set/delete commands), or an XML configuration.

This example is found within this directory as "set-config.py".

```
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

```

This example is almost identical. The difference we have here is that when loading the configuration we must specify the type. As we are using the set commands we specify the type as "set". In the previous example we didn't specify the type as the "text" type is the default.
