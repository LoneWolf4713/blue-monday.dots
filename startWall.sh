#!/bin/bash

python /home/prtyksh/Wallpapers/rofi.py

nohup python -m http.server 5670 -d /home/prtyksh/Wallpapers & 

firefox "http://localhost:5670/gallery.html" &

python /home/prtyksh/Wallpapers/server.py &

echo "HIIII"
