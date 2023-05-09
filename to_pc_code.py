import open3d as o3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def dm_to_pc(color_image, depth_image):
    color_raw = o3d.io.read_image(color_image)
    depth_raw = o3d.io.read_image(depth_image)
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, o3d.camera.PinholeCameraIntrinsic(
        o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault))
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    o3d.io.write_point_cloud(filename="mast_0_pc_1.pcd", pointcloud=pcd)
    o3d.visualization.draw_geometries(geometry_list=[pcd])
