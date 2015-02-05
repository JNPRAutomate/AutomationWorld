Junos Space APIs
================

Currently it seems that Space 13.1 is the most deployed. So all APIs below are part of that. Newer documentation is available for the new platforms. Generally the APIs do not regress, but are always subject to change.

Platform APIs
-------------

Space is a platform and it has many applications that can run on top of it. However there are core APIs that are used to access platform logging, device management, and other core areas.

-	[General API Information](http://www.juniper.net/techpubs/en_US/junos-space-sdk/13.1/apiref/index.html)
-	[API Behaviors](http://www.juniper.net/techpubs/en_US/junos-space-sdk/13.1/apiref/com.juniper.junos_space.sdk.help/html/reference/Commonbehav.html)
-	[Auth Model](http://www.juniper.net/techpubs/en_US/junos-space-sdk/13.1/apiref/com.juniper.junos_space.sdk.help/html/reference/Commonbehav.html#step3)
	-	The auth model is HTTP/S Basic auth
-	[Junos Device Management](http://www.juniper.net/techpubs/en_US/junos-space-sdk/13.1/apiref/com.juniper.junos_space.sdk.help/JSDeviceManagerSvc/Docs/index.html)
	-	Covers listing devices and understanding the properties of devices
-	[Auditlogging](http://www.juniper.net/techpubs/en_US/junos-space-sdk/13.1/apiref/com.juniper.junos_space.sdk.help/JSAuditlogManagerSvc/Docs/index.html)

Security Director APIs
----------------------

Security director is a space application that allows you to manage SRX devices and specifically their security aspects.

-	[SD APIs](http://www.juniper.net/techpubs/en_US/junos-space13.1/information-products/topic-collections/junos-space-security-designer/security-director-api.pdf)
	-	Policy management areas:
		-	Firewall Policy Management RESTful Web Services (Adding/removing policies)
		-	Address Management RESTful Web Services (Address objects for policies)
