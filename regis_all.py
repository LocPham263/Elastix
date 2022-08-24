import subprocess
import os
import time
import shutil
from tqdm import tqdm
# import SimpleITK as sitk
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from time import time

moving_folder = './data/images_Contrast_bbox/'
fixed_folder = './data/images_NonContrast_bbox/'
moving_label_folder = './data/mask_Contrast/'
fixed_label_folder = './data/mask_NonContrast/'

# moving_folder = './data/imageTr_Contrast/'
# fixed_folder = './data/image_NonContrast/'
# moving_label_folder = './data/mask_Contrast/'
# fixed_label_folder = './data/mask_NonContrast/'

rigid_pred_folder = './data/rigid_pred/'
nonrigid_pred_folder = './data/nonrigid_pred/'
pred_folder = './data/prediction/'

moving_ls = sorted(os.listdir(moving_folder))
fixed_ls = sorted(os.listdir(fixed_folder))
moving_label_ls = sorted(os.listdir(moving_label_folder))
fixed_label_ls = sorted(os.listdir(fixed_label_folder))

rigid_params = './script/RigidparaPI.txt'
# rigid_params = './elastix_example_v4.8/exampleinput/parameters_Rigid.txt'
nonrigid_param = './script/NonrigidparaPI.txt'

for i in tqdm(range(len(moving_ls))):
# for i in range (1):
    os.mkdir(pred_folder + moving_ls[i][:5])
    
    subprocess.run('elastix -f ' + fixed_folder + fixed_ls[i] +
            ' -m ' + moving_folder + moving_ls[i] +
            ' -fMask ' + fixed_label_folder + fixed_label_ls[i] +
            ' -mMask ' + moving_label_folder + moving_label_ls[i] +
            ' -p ' + rigid_params +
            ' -p ' + nonrigid_param +
            ' -out ' + pred_folder + moving_ls[i][:5], shell=True)
#     print(moving_ls[i][2:5], fixed_ls[i][2:5], moving_label_ls[i][2:5], fixed_label_ls[i][2:5])
