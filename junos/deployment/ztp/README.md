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


# Advanced Notes

## ZTP DHCP Options codes
```
Required ZTP Options: | Purpose | Description
--------------------- | ------- | -----------
DHCP Option 66:       | 	| This is for TFTP/HTTP/FTP server name. Operator should be aware that this option usage comes with certain conditions till DNS resolving capability is supported. Till DNS resolving support is implemented, option 66 should send IP address in string format.
-or- | |
DHCP Option 150       | 	| To specify the IP address of the FTP, HTTP, or TFTP server.
		
ZTP Specific Sub option codes: | |
------------------------------ | - | - 
00	| Image File | This is the image file name, which is used by DHCP client for requesting HTTP/FTP/TFTP server.
01	| Configuration file. | This is the configuration file name, which is used by DHCP client for requesting HTTP/FTP/TFTP server.
02	| Symbolic link to the software image file to install | If this option is not set, ZTP handles the software image as a filename, not a symbolic link.
03	| Transfer Mode | Transfer mode (TFTP/FTP/HTTP) that the switch uses to access the TFTP/FTP/HTTP server for retrieving file(s).
04	| Alternate Image | When the DHCP server cannot use vendor sub option 00, configure image file using sub option 04. If both sub option 00 and sub option 4 are defined, sub option 04 is ignored.
		
Additional options to be processed:
-----------------|---------------|-----------------------------------------------------------------------------|
DHCP Option 42:  | NTP Server 	 | NTP server is to perform time synchronization on the network.
DHCP Option 07:  | Syslog Server | System log (syslog) server to manage system log messages and alerts.
DHCP Option 12:  | Hostname 	 | To specify the hostname of the switch.
```
