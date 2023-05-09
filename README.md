## Code to generate a depth image and point cloud file from a normal, single image

This repository uses an already developed model that converts from single images to depth images by René Ranftl, Alexey Bochkovskiy, Vladlen Koltun.  This repository can be found here: https://github.com/isl-org/MiDaS

Make sure that you get an understanding of the model setup using the linked repository's readme!  This is very important to make sure that you have the right dependencies in your enivronment.

DO NOT forget to use a virtual enviornment like Anaconda to set up dependencies -- your computer WILL have problems otherwise and you might lose many other files and work if you have to revert back to a previous backup of your OS.

### Setup 
 
Install open3D:
```
pip install --trusted-host www.open3d.org -f http://www.open3d.org/docs/latest/getting_started.html open3d
```

Install other needed libraries:
All of the needed libraries shoud already be installed if you followed the setup in the linked repository above.  However, if there are any libaries that still need to be installed, you will be prompted to do so by PyCharm when you try to run the depth map generation, and you can just install these either through pip or through PyCharm itself.

### Running

1) Place your normal images in the "input" folder
2) Run the depth map generation using the following code:

```
python run.py --model_type dpt_swin_large_384 --input_path input --output_path output
```
3) The depth map will be output to the "output" folder
4) In ```main.py```, change the variable named ```color_test``` to ```"input/<your_filename>"```
5) In ```main.py```, change the variable named ```depth_test``` to ```"output/<name_of_corresponding_depth_img>"```
6) In ```to_pc_code.py``` change the filename variable on line 14 to correspond to the name of the file you are using as your normal image (file nameing is not automated yet, so this needs to be done manually for every new point cloud generated)
7) Run ```main.py``` to generate the point cloud file and bring up the point cloud viewer

