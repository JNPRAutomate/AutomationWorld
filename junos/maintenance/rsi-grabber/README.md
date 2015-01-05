RSI Grabber
===========

Gathering the "request support information" from a Junos Device

Background
----------

One of the first steps to do when trying to troubleshoot an issue on a Junos device is to gather the request support information or RSI. This is an on-box script that is included on every Junos device. It provides a majority of the current state on a device. This includes but is not limited to: configuration, counters, the presence of core dumps, and logs. Often you want to gather this information at the point at which an event occurs to provide the most current state of device. However you are often not sitting at the console of a device when this occurs.

Demo Examples
-------------

This directory contains two examples of gathering the RSI from a host.

#### Python Version

The first is an off-device script that pulls the RSI data off the device and places it in a specified directory. The filename is automatically named based upon the timestamp of the data acquisition and the IP or hostname provided.

#### SLAX Version

Secondly an on-device version is also provided. This will allow you to either issue a command to trigger the script to place the RSI off-box or secondly let an event on the device trigger the collection.
