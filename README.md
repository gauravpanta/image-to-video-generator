Simple script to create video from images in a folder.
Concatenates all images in the folder into a video file

Install Dependencies:

```
pip install av opencv-python
```

RUN
```
python app.py -p ./NORMAL -f 30 -o normal.mp4
```

HELP:
python app.py --help
usage: app.py [-h] -p PATH [-f FPS] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit  
  -p PATH, --path PATH  
  -f FPS, --fps FPS  
  -o OUTPUT, --output OUTPUT  
