![](https://www.xda-developers.com/files/2019/01/es-explorer-skull-1900x700_c.png)
(https://www.xda-developers.com/files/2019/01/es-explorer-skull-1900x700_c.png)

## Introduction
As I was fiddling around on the HackTheBox machine "Explore" lately, I came across this vulnerability. It is not particularly complicated or interesting, merely a bug that was actually a feature. 

CVE-2019-6447 is a high impact vulnerability targeting the ES File Explorer application on Android devices. This file explorer used to have the added functionality of providing an interface for commands to the entire network, without authentication whatsoever.

This vulnerability scored an 8.1 for CVSS 3.x and was initially reported and disclosed by Baptiste Robert two days before a patch was ready. 

## The workings
Basically, ES File Explorer used to open up a backdoor listening on port 59777, providing a set of commands to interact with the device, as well as the option to directly access a file by appending the absolute path to the request url. A list of the commands available:
- listFiles
- listPics
- listVideos
- listAudios
- listApps
- listAppsSystem
- listAppsPhone
- listAppsSdcard
- listAppsAll
- getDeviceInfo

## Usage
Inspired by the name of the box, "Explore", I wanted this POC to be easy to use with exploration in mind. Staying interactive and typing command after command to search through the device was my goal. 

`python3 poc.py`

The exploit will require you to enter a target and ask if you'd like to change the default port. Then, you are pretty much ready to explore the device you are "connected" to, but of course, it will still send separate requests each time. The interactiveness is just for the looks and funsies:D

## Contributions
Shout-out to Baptiste Robert (@fs0c131y) for finding and reporting the vulnerability, as well as Nehal Zaman (packetstorm contributor, didn't find Twitter handle) for creating the exploit this is inspired by.
