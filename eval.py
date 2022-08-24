import SimpleITK as sitk
import matplotlib.pyplot as plt
import pandas as pd
import os
from tqdm import tqdm
import shutil
import metrics

label_folder = './data/labelsTr_NonContrast/'
seg_folder = './data/labelsTr_NonContrast_pred/'

label_ls = sorted(os.listdir(label_folder))
seg_ls = sorted(os.listdir(seg_folder))

file_name = []
DSC_val = []
IoU_val = []
VOE_val = []
RVD_val = []
FNR_val = []
FPR_val = []
ASSD_val = []
RMSD_val = []
MSD_val = []

for i in tqdm(range(len(label_ls))):
# for i in range (2,5):
#     # if len(os.listdir(BASE_DIR + df_folder + df_ls[i])) > 3:
#     #     continue
    ct_sitk = sitk.ReadImage(seg_folder + seg_ls[i])
    pred = sitk.GetArrayFromImage(ct_sitk)

    label_sitk = sitk.ReadImage(label_folder + label_ls[i])
    label = sitk.GetArrayFromImage(label_sitk)

    Loss = metrics.Metric(label, pred, label_sitk.GetSpacing())
    print(label_ls[i][:5] + ': ' + str(Loss.get_dice_coefficient()))

    DSC = Loss.get_dice_coefficient()
    IoU = Loss.get_jaccard_index()
    VOE = Loss.get_VOE()
    FNR = Loss.get_FNR()
    FPR = Loss.get_FPR()
    ASSD = Loss.get_ASSD()
    RMSD = Loss.get_RMSD()
    MSD = Loss.get_MSD()

    file_name.append(label_ls[i][:5])
    DSC_val.append(DSC)
    IoU_val.append(IoU)
    VOE_val.append(VOE)
    FNR_val.append(FNR)
    FPR_val.append(FPR)
    ASSD_val.append(ASSD)
    RMSD_val.append(RMSD)
    MSD_val.append(MSD)

    df = pd.DataFrame({'File name': file_name,
                        'DSC': DSC_val,
                        'IoU': IoU_val,
                        'VOE': VOE_val,
                        'FNR': FNR_val,
                        'FPR': FPR_val,
                        'ASSD': ASSD_val,
                        'RMSD': RMSD_val,
                        'MSD': MSD_val})

    df.to_csv(path_or_buf = './niftyReg_report_1.csv')
