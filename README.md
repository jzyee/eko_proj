# eko_proj


script loads all dicom files and saves the first frame of the image/video


Place your dicom(.dcm) files in the sample_dicoms/ folder

## how to run the file

create a virtual environment to install the requirements for file
```
    conda create -n eko_proj python=3.9
    source activate eko_proj
    pip install -r requirements.txt
```

Once the environemnt has all the required packages and activated, simple run the following
```
    python ekoC.py
```
## single worker vs mutliple worker results

![res](results.png)



