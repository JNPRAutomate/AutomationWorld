Zero Touch Provisioning
========================

What is Zero Touch Provisioning
--------------------------------

# Examples
## Simple ISC DHCP Example

In this example we will use the contents of the file:
	https://github.com/JNPRAutomate/AutomationWorld/blob/master/junos/deployment/ztp/ztp-dhcpd-simple.conf.

This example shows the minimal configuration required to configure 

### Define ZTP Options
The first step is to map the required DHCP Option codes to friendly names we can reference in our dhcpd.conf file. These codes are common to all examples shown here.

```
option ztp-file-server code 150 = { ip-address };

option space ztp-ops;
option ztp-ops.image-file-name code 0 = text;
option ztp-ops.config-file-name code 1 = text;
option ztp-ops.image-file-type code 2 = text;
option ztp-ops.transfer-mode code 3 = text;
option ztp-ops-encap code 43 = encapsulate ztp-ops;
```

Next we use standard ISC DHCP ranges to define details such as subnet, gateways as well as our ZTP options defined above

```
subnet 172.32.32.0 netmask 255.255.255.0 {
  range 172.32.32.20 172.32.32.200;
  option domain-name "ztp.provisioning.local";
  option routers 172.32.32.254;
  option broadcast-address 172.32.32.255;
  default-lease-time 600;
  max-lease-time 7200;
  option ztp-file-server 172.32.32.254;
  option host-name "netboot";
  option ztp-ops.image-file-name "/jinstall-qfx-5-flex-13.2X51-D20.2-domestic-signed.tgz";
  option ztp-ops.transfer-mode "http";
  }
}
```