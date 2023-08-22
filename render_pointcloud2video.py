import os
import os.path as osp
import time

import numpy as np
import open3d as o3d

def transform_view(vis):
    angle_deg = 30
    angle_rad = np.radians(angle_deg)
    rot = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad), 0],
        [np.sin(angle_rad), np.cos(angle_rad), 0],
        [0, 0, 1]
    ])
    pcd.rotate(rot, center=(0,0,0))

pcd = o3d.io.read_point_cloud('/home/hanj/projects/pointcloud_vis_tools/chair.ply')
mean_val, _ = pcd.compute_mean_and_covariance()
pcd.translate(-mean_val, relative=True)

vis = o3d.visualization.Visualizer()
vis.create_window()

# vis.add_geometry(pcd)
# vis.register_animation_callback(transform_view)
# vis.run()

def predfine_move(index):
    if True: #index < 10:
        angle_deg = 5
        angle_rad = np.radians(angle_deg)
        rot = np.array([
            [np.cos(angle_rad), -np.sin(angle_rad), 0],
            [np.sin(angle_rad), np.cos(angle_rad), 0],
            [0, 0, 1]
        ])
        pcd.rotate(rot, center=(0,0,0))
    else:
        pcd.translate((0,-1,0), relative=True)

image_folder = 'frames'

for i in range(60):
    vis.clear_geometries()
    vis.add_geometry(pcd)
    predfine_move(i)
    vis.poll_events()
    vis.update_renderer()

    image_path = os.path.join(image_folder, f'{i:04d}.png')
    os.makedirs(osp.dirname(image_path), exist_ok=True)
    vis.capture_screen_image(image_path)
    time.sleep(0.3)