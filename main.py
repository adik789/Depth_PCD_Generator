# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from to_pc_code import dm_to_pc


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


color_test = "input/mast_0.png"
depth_test = "output/mast_0-dpt_swin2_large_384.png"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dm_to_pc(color_test, depth_test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
