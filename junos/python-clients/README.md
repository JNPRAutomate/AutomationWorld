Junos command-line abstractions
===============================

While Junos offers many different APIs, programming language drivers, these all require a way to interact with these APIs. Customers could write a tool to interact with the APIs, or use one of the drivers this may be out of the scope of their capabilities. Or they may simply not want to maintain these tools. The Junos CLI toolkit helps solve some common problems that users face with managing Junos devices. These tools are not designed to run every possible command or configure every element.

Common Uses
-----------

### Configuration

-	Create a firewall policy
-	Add an IP on an interface
-	Add a VLAN to a device
-	Apply a VLAN to an interface
-	Enable a routing protocol on an interface

### Operations

-	Fetch a request support information (RSI) from a device
-	Validate if your BGP connection is running

### Maintenance

-	Upgrade a device
-	Clean up log files
-	Restart a service
-	Reboot a device
-	Clear counters
