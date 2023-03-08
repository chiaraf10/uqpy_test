import fire
import os
import numpy as np
from lasso.dyna import D3plot, ArrayType
import shutil


def read_output(index):
    index = int(index)
    try:
        d3plot = D3plot(state_array_filter=[ArrayType.node_displacement])
        path_to_d3plot = os.path.join(os.getcwd(), "d3plot")
        d3plot = D3plot(path_to_d3plot)
        node_disp = d3plot.arrays[ArrayType.node_displacement][1, :, :]
        # os.chdir("..")
        # run_dir = os.getcwd()
        # print(run_dir)
        # os.chdir("..")
        # print(os.listdir())
        # # print(os.getcwd())
        # del_dir = "run_" + str(index)
        # shutil.rmtree(del_dir)

        return node_disp
    except OSError as err:
        print(err)
        return np.array([100, 100, 10000])


if __name__ == "__main__":
    fire.Fire(read_output)
