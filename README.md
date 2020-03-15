# SimplePiScanner
Simple Raspberry Pi 3D Scanner

## Setup hardware
Coming soon

## Install Requirements
```
pip install -r requirements.txt
````

## Run Scanner

```
python scan.py
```

## Turn into 3D model

I use meshroom, Google Drive, and a Google Colab notebook to do the photogrammetry model processing for me.

Upload your folder to Google Drive.

Copy the jupyter notebook from this repo to Google Colab (https://colab.research.google.com/)

Change the input and output folders to match your Drive folder.

Press the play button on Step 1 to authorize Drive access, then press play on Step 2 and wait.  After a while you should have 3 files in your Output file.
