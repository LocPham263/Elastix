import os
import numpy as np
import SimpleITK as sitk
from tqdm import tqdm
import matplotlib.pyplot as plt

BASE_DIR = './data/'

# ct_folder = 'images_NonContrast/'
# seg_folder = 'labels_NonContrast/'
# saved_ct_folder = 'images_NonContrast_bbox/'
# saved_seg_folder = 'labels_NonContrast_bbox/'

# ct_folder = 'images_Contrast/'
# seg_folder = 'labels_Contrast/'
# saved_ct_folder = 'images_Contrast_bbox/'
# saved_seg_folder = 'labels_Contrast_bbox/'

seg_folder = 'labels_NonContrast_bbox/'
saved_seg_folder = 'mask_NonContrast/'

# ct_ls = sorted(os.listdir(BASE_DIR + ct_folder))
seg_ls = sorted(os.listdir(BASE_DIR + seg_folder))

for i in tqdm(range(19,len(seg_ls))):
# for i in range (18,19):
    # print(seg_ls[i], ct_ls[i])
    # ct_sitk = sitk.ReadImage(BASE_DIR + ct_folder + ct_ls[i])
    # ct = sitk.GetArrayFromImage(ct_sitk)
    seg_sitk = sitk.ReadImage(BASE_DIR + seg_folder + seg_ls[i], outputPixelType=sitk.sitkUInt8)
    seg = sitk.GetArrayFromImage(seg_sitk)
    
    # start_z = 0
    # stop_z = 0
    # for slice in range (seg.shape[0]):
    #     if start_z == 0 and np.sum(seg[slice]) != 0:
    #         start_z = slice
    #     elif start_z != 0 and np.sum(seg[slice]) == 0:
    #         stop_z = slice
    #         # print(seg_ls[i], start, stop, stop - start)
    #         break

    # start_x = 0
    # stop_x = 0
    # for slice in range (seg.shape[1]):
    #     if start_x == 0 and np.sum(seg[:,slice,:]) != 0:
    #         start_x = slice
    #     elif start_x != 0 and np.sum(seg[:,slice,:]) == 0:
    #         stop_x = slice
    #         # print(seg_ls[i], start, stop, stop - start)
    #         break
    
    # start_y = 0
    # stop_y = 0
    # for slice in range (seg.shape[2]):
    #     if start_y == 0 and np.sum(seg[:,:,slice]) != 0:
    #         start_y = slice
    #     elif start_y != 0 and np.sum(seg[:,:,slice]) == 0:
    #         stop_y = slice
    #         # print(seg_ls[i], start, stop, stop - start)
    #         break

    # labelimfilter = sitk.LabelShapeStatisticsImageFilter()
    # labelimfilter.Execute(seg_sitk)
    # (y, x, z, y_len, x_len, z_len) = labelimfilter.GetBoundingBox(1)

    # # print(labelimfilter.GetBoundingBox(1))
    # # print(y, y+y_len, x, x+x_len, z, z+z_len)
    # # print(start_y, stop_y, start_x, stop_x, start_z, stop_z)
    
    
    # # new_ct_sitk = sitk.GetImageFromArray(ct[z:z_len, x-30:x+x_len+100, y-30:y+y_len+130])
    # new_ct_sitk = sitk.GetImageFromArray(ct[z:z_len, x-15:x+x_len+30, y-15:y+y_len+30])
    # new_ct_sitk.SetSpacing(ct_sitk.GetSpacing())
    # new_ct_sitk.SetDirection(ct_sitk.GetDirection())
    # # new_ct_sitk.SetOrigin(ct_sitk.TransformIndexToPhysicalPoint((y-30,x-30,z)))
    # new_ct_sitk.SetOrigin(ct_sitk.TransformIndexToPhysicalPoint((y-15,x-15,z)))
    # # new_ct_sitk.SetOrigin(ct_sitk.TransformIndexToPhysicalPoint((0,0,start)))
    
    # # new_seg_sitk = sitk.GetImageFromArray(seg[z:z_len, x-30:x+x_len+100, y-30:y+y_len+130])
    # new_seg_sitk = sitk.GetImageFromArray(seg[z:z_len, x-15:x+x_len+30, y-15:y+y_len+30])
    # new_seg_sitk.SetSpacing(seg_sitk.GetSpacing())
    # new_seg_sitk.SetDirection(seg_sitk.GetDirection())
    # # new_seg_sitk.SetOrigin(seg_sitk.TransformIndexToPhysicalPoint((y-30,x-30,z)))
    # new_seg_sitk.SetOrigin(seg_sitk.TransformIndexToPhysicalPoint((y-15,x-15,z)))
    # # new_seg_sitk.SetOrigin(seg_sitk.TransformIndexToPhysicalPoint((0,0,start)))

    dilate_itk = sitk.BinaryDilate(seg_sitk, (2,2,2))
    sitk.WriteImage(dilate_itk, BASE_DIR + saved_seg_folder + seg_ls[i])

    # sitk.WriteImage(new_ct_sitk, BASE_DIR + saved_ct_folder + seg_ls[i])
    # sitk.WriteImage(new_seg_sitk, BASE_DIR + saved_seg_folder + seg_ls[i])

   