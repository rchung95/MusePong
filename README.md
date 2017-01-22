# MusePong


To connect to muse: muse-io --device DEVICE_NAME

And a connection will open 

Pipe output of muse to python file and pipe python file's output to unity: 
```
muse-player -l 5000 -D 1> >(python read.py) | unity_program
```

