The easiest way to load configuration templates
===============================================

The best way to automate Junos utilizing Python is the Junos-PyEZ library. However if you have little experience with Python these first steps can be very daunting. To make Junos-PyEZ even easier we have the pyJunosManager library. This abstracts some of the common use cases of Junos-PyEZ into a simpler format. Typically this library is used by beginners or folks who don't want to get deeper into Python. Since this module uses Junos-PyEZ it will also install that as well.

pyJunosManager
--------------

The [pyJunosManager](https://pypi.python.org/pypi/pyJunosManager) is a simple abstraction library for Junos-PyEZ. As an abstraction library simply takes a task, or series of steps, and makes it easier to accomplish. In this case we want to simply connect to a Junos device and load a configuration template. You can check out the [source code](https://github.com/JNPRAutomate/pyJunosManager) of the module and see how it utilizes Junos-PyEZ. Or you can look at the [documentation](http://pyjunosmanager.readthedocs.org/en/latest/).

Example
-------

For this example we are going to take a configuration template and load it onto the device. The template is written in [Jinja](http://jinja.pocoo.org) a simple template language.

### Configuration Template

This example is found within this directory as "jnpr-config.tmpl".

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

This example is found within this directory as "set-config.tmpl".

The configuration template is setting up a few management options for us. This would be typical of most organizations and their need to bootstrap devices. In this template we have three defined variables: hostname, enc_password, and ssh_root_login. These variables are contained within a set of special brackets "{{ }}". These brackets tell the Jinja engine that the string within the brackets are the variable names. Once you apply the template to render it replaces the brackets and the name with the data you have chosen. In this case render isn't a complex process that includes 3D textures it simple means to replace these values with the ones I provide.

### Python script

Now that we have taken a look at a basic template, let's look at the program that will be using it. In the below example is the script or program that will be reading in the template.

This example is found within this directory as "jnpr-config.py".

```
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
junos_dev = JunosDevice(host="1.2.3.4",username="root",password="Juniper")
#now we can connect to the device
dev.open()
#we then open the configuration
dev.open_config()
#lets go ahead and load the configuration.
dev.load_config_template(tmpl_data,my_variables)
#commit and close the config
dev.commit_and_quit()
#lastly we close the connection to the device
dev.close()
```

This example is found within this directory as "set-config.tmpl".

```
set system host-name {{ hostname }}
set system root-authentication encrypted-password "{{ enc_password }}"
set system services ssh root-login {{ ssh_root_login }}
set system services netconf ssh
set system services web-management http interface ge-0/0/0.0
```

This example is found within this directory as "set-config.py".

```
```
