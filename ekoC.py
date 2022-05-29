import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import numpy as np
from PIL import Image
from pathlib import Path
from multiprocessing.pool import Pool
import os
import time
from multiprocessing import Process, freeze_support
import matplotlib.pyplot as plt

in_path = 'sample_dicoms/'
out_path = 'data_converted'
img_size = (256,256)
threads = 4


if os.name == 'nt':
    sep = '\\'
else:
    sep = '/'



def dicom2np(dicom):
    data = dicom.pixel_array
   
    return data

def save_img(path):
        
    dicom_scan = pydicom.read_file(path)

    np_img = dicom2np(dicom_scan)
    if len(np_img.shape) > 3:
        np_img = np_img[0]

    im = Image.fromarray(np_img)
    
    im = im.resize(img_size, Image.NEAREST)
    splitted = path.split(sep)
    splitted[0] = out_path
    path_folders = Path(sep.join(splitted[:-1]))
    path = Path(sep.join(splitted))
    
    path_folders.mkdir(parents=True, exist_ok=True)
    im.save(str(path)[:-3] + 'png') 


def main():
    thread_list = [1, 2, 3, 4]
    res = {}

    for thread_no in thread_list:
        start_time = time.time()
        paths = [str(p) for p in Path(in_path).rglob('*.dcm')]
        with Pool(thread_no) as p:
            list(p.imap(save_img, paths))
            p.close()
            p.join()
        time_taken = time.time() - start_time
        print("time taken for {} workers {:.3g}s seconds ---".format(thread_no, time_taken))

        res[thread_no] = time_taken

    fig,ax = plt.subplots(figsize=(8,8))
    plt.bar( list(res.keys()), list(res.values()))
    plt.xticks(np.arange(1,max(thread_list)+1,1))
    plt.xlabel("no. of worker processes used")
    plt.ylabel('tim taken (s)')
    plt.title('Time taken to parse Dicom images using single thread vs multiple')
    plt.savefig('results.png')
    plt.show()


if __name__ == '__main__':
    main()