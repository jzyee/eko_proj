import matplotlib.pyplot as plt
from pathlib import Path
import os
import pydicom
#
import io.tensorflow_io as tfio # no support for M1

pathname = "sample_dicoms"


def check_isFile(filepath):

    if Path(filepath).is_file():
        return True
    else:
        return False

print('start')

file_exts_ignore = [".DS_Store", ".zip"]

dcm_files = []

for path in Path(pathname).rglob('*'):
    fullpath = path.resolve()
    #print(path.name)
    if check_isFile(fullpath):
        filename, file_ext = os.path.splitext(path.name)
        if not path.name.startswith('.'):
            if file_ext not in file_exts_ignore:
                #print("{} | {}".format(filename, file_ext))
                if file_ext == ".dcm":
                    dcm_files.append(fullpath)
        else:
            pass

dcm_filename = dcm_files[0]

# ds = pydicom.read_file(dcm_filename)

# plt.imshow(ds.pixel_array, cmap=plt.cm.bone)

image_bytes = tfio.read_file(dcm_filename)