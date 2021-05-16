

import argparse
import sys
import os


checkpoint_path="weights/best_yolov5s.pt"
checkpoint_path_second="weights/best_salient.pth"

if __name__ == '__main__':
    


    
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default=checkpoint_path, help='model.pt path(s)')
    parser.add_argument('--weights_bg_removal', nargs='+', type=str, default=checkpoint_path_second, help='model.pt path(s)')

    parser.add_argument('--source', type=str, default="0", help='source')

    opt = parser.parse_args()
    command = f"python3 ./yolov5_repo/detect.py --source {opt.source} --weights {opt.weights} --weight_salient {opt.weights_bg_removal} --conf 0.5"
    try:
        os.system(command)
    except:
        command=command.replace("python3","python",1)
        os.system(command)
    

    