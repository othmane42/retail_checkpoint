# retail-checkout-detection

## requirements 
Python 3.7 or later with all requirements.txt dependencies installed.
```
pip install -r requirements.txt 
pip install visdom
pip install cython
pip install git+https://github.com/lucasb-eyer/pydensecrf.git


```

## weights to download 

link to download salient detector model : https://drive.google.com/file/d/1-bTMzWzq5m512OtDm6GN8iGWyPHdTg0C/view?usp=sharing 

there's no need to download yolo weights they are already in the weights folder

## how to use

```
python main.py --source 0 #webcam --weight_salient PATH_TO_SALIENT_DETECTOR_WEIGHTS 
```
