# pyUDPpunch

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

pyUDPpunch is a lightweight udp hole punching tool made solely in python, it uses a series of connection steps to build and establish connection.. (note: doesnt support relays)

  - Easy and lightweight module
  - Import, run and build connection
  - Join two clients p2p without hassles!

# New Features!

  - Support direction connection and double full nat connections!
  - Can optionally define timestamp to coordinate connection time and hence ensure more chances of connection establishment (timestamp is seconds elapsed after 1970/1/1)


pyUDPpunch works and tries to implement several methods of nat traversal and udp hole punching algorithms  as stated on this [Wikipedia site][df1]

> The overriding design goal for pyUDPPunch
> is to make a tool for pythonian users to have
> better network controls and tools that make
> networking and p2p connections more feasible
> without the hassle of diving deeper into more
> OOP high level languages like c. This ensures
> user to be present with high readability and 
> a community which works exclusively to make
> direct connections possible with ease :)


### Tech

pyUDPPunch uses a these source projects to work properly:

* [pystun3](https://github.com/talkiq/pystun3) - STUN for python users!

And of course pyUDPPunch itself is open source with a [public repository][dill] on GitHub.

### Installation

pyUDPPunch requires [python 3+](https://www.python.org/download/) to run.
```py
pip install pyUDPpunch
```
##### For Latest/Beta Releases: Install Using Git Link (GIT PROGRAM REQUIRED)
```py
pip install git+https://github.com/hari01584/pyUDPpunch.git#egg=pyUDPpunch
```

### How To Use / Implement

Using pyudppunch is tad easy, its like buttering your breads! just after installing the module do (in top of your script):
```py
from pyUDPpunch.nat_punch import Connector
```
then whenever you want to make a connection write these lines :P
```py
x = Connector(<targetip>,<targetport>,<optional:connection_port>,<optional:timestamp>)
x.start_connection()
print(x.load())
```
Or you could initilize with empty instructor and fill values later!
```py
x = Connector()
info = x.local_info() #Gives client localip and port, pass this data to second clien.
x.setOn(<targetip>,<targetport>,<optional:connection_port>,<optional:timestamp>)
print(x.load())
```

###### Here's How To Implement This Nicely!
* In Start Of Program Call Empty Constructor Connector And Set It To A Variable Say **x**.
* Call **x.local_info()** and pass this data (in tuple) to your other client/peer.
* This data contains ip and port of your peer and use this to initialize constructor on your peer's pc.
* Optionally you can define a timestamp to coordinate start of connection attempt.
* Wait for connection to succeed! And call **x.load()** to fetch your connection data.
* You can bind to the ip and port described in your connection data and open udp socket to start exchange!
* NOTE: If connection fails then first parameter of connection data is set to 0!! (Read Descriptor Table For More Information Regarding Each Function Call Returns!)


### Descriptor/Class Function Returns
| Function Name | Return Data |
| ------ | ------ |
| setOn | Returns Nothing |
| local_info | Returns tuple (nat_type, localip, localport) |
| load | Returns tuple (status, connection_ip, connection_port, lport)|


### Development

Want to contribute? Great!

We are in dire need for developers which can extend and improve the codes as well as add new functions and methods, you are always welcome to pull and edit the code, for more active development you can directly contact me at my discord IGN: Agent_Orange#9852
### Todos

 - Add Full Cone To Symmetric Connector
 - Add Support And Better Output Of Codes/Result And Data
 - Support Symmetric-Symmetric Connection Using Relays

License
----

GPLv3

    Copyright (C) 2020 Harishankar Kumar
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/hari01584/r>
   [git-repo-url]: <https://github.com/hari01584/pyUDPpunch.git>
   [df1]: <https://en.wikipedia.org/wiki/UDP_hole_punching>
 
   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
