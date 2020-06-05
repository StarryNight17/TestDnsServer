# TestDnsServer
Select best DNS servers. Giving a list of domains and a list of DNS servers. The process will test dns server sequentially. When Testing a dns server, the process acquire the server address of the domain with this dns at first, and then test the latency between client and server. For every domain, the process will output the maximum, minimum and average latency. If one DNS server can not resolve all the domains or have any latency that is greater than 300ms, it will not be appear on the final top rank. At the end of the process will output the Top DNS servers sorted by average latency.


## Requirements
- [nslookup](https://pypi.org/project/nslookup/)
```
pip install nslookup
```
- [pythonping](https://pypi.org/project/pythonping/)
```
pip install pythonping
```
- [eventlet](https://pypi.org/project/eventlet/)
```
pip install eventlet
```

## Run
Please make sure to run with root access.
```
sudo python ./testDnsServer.py
```