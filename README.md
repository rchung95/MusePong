# MusePong

First, install Muse's Research Tools

To connect to muse: 
```muse-io --device DEVICE_NAME```

And a connection will open 

Redirect output dump of muse to python's stdin: 
```
muse-player -l 5000 -D 1> >(python game2.py)
```
This would open a game of Pong on your computer, which is be controlled by the muse headband's inputs
