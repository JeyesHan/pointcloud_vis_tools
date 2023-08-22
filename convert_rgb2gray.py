import os
import os.path as osp
import glob

import cv2

img_dir = '/home/hanj/projects/pointcloud_vis_tools/frames'
save_dir = '/home/hanj/projects/pointcloud_vis_tools/gray_frames'
os.makedirs(save_dir, exist_ok=True)
for img_name in os.listdir(img_dir):
    img = cv2.imread(osp.join(img_dir, img_name))
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    save_img_file = osp.join(save_dir, img_name)
    cv2.imwrite(save_img_file, gray_img)