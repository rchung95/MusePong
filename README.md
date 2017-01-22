# MusePong


To connect to muse: 
```muse-io --device DEVICE_NAME```

And a connection will open 

Redirect output dump of muse to python's stdin: 
```
muse-player -l 5000 -D 1> >(python new_server.py)
```

