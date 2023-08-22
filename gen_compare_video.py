import os
import os.path as osp
import copy

import numpy as np
import cv2


def combine_dual_imgs(img1, img2, delimer_ind, delimer_width=3, delimer_color=[0,0,0]):
    h, w, c = img1.shape
    assert w > delimer_width + 3
    left_ind = max(0, int(delimer_ind - delimer_width / 2))
    right_ind = min(w-1, int(delimer_ind + delimer_width / 2))
    if left_ind == 0:
        right_ind = left_ind + delimer_width
    if right_ind == (w-1):
        left_ind = right_ind - delimer_width
    print(left_ind, right_ind)
    # import ipdb; ipdb.set_trace()
    new_img = copy.deepcopy(img1)
    new_img[:,left_ind:right_ind] = delimer_color
    new_img[:,right_ind:] = img2[:,right_ind:]
    return new_img

if __name__ == '__main__':
    imgs_dir1 = '/home/hanj/projects/pointcloud_vis_tools/frames'
    imgs_dir2 = '/home/hanj/projects/pointcloud_vis_tools/gray_frames'
    save_dir = '/home/hanj/projects/pointcloud_vis_tools/compare_frames'
    os.makedirs(save_dir, exist_ok=True)
    ptr = None
    step = 100
    signed_step = -step
    for i, img_name in enumerate(sorted(os.listdir(imgs_dir1))):
        img1 = cv2.imread(osp.join(imgs_dir1, img_name))
        img2 = cv2.imread(osp.join(imgs_dir2, img_name))
        h, w, c = img1.shape
        if ptr is None:
            ptr = w
        ptr += signed_step
        if ptr < 0:
            ptr = 0
            signed_step = 1 * step
        elif ptr >= w:
            ptr = w - 1
            signed_step = -step
        # print(ptr)
        compare_img = combine_dual_imgs(img1, img2, delimer_ind=ptr, delimer_width=6)
        save_file = osp.join(save_dir, img_name)
        cv2.imwrite(save_file, compare_img)
    os.system(f'ffmpeg -framerate 5 -i {save_dir}/%4d.png demo.mp4')
