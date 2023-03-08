import os
import fire
import subprocess


def run_dyna_model(index):
    index = int(index)
    input_file_name = "run_" + str(index) + ".k"
    input_file_path = "InputFiles"
    working_dir = os.getcwd()

    # call LS-DYNA
    run_dir = os.path.join(working_dir, input_file_path)
    os.chdir(run_dir)
    subprocess.call(
        "C:/LSDYNA/program/ls-dyna_smp_s_R11_1_0_winx64_ifort160.exe i={}".format(
            input_file_name
        )
    )
    fileObject = open("messag", "r")
    data = fileObject.read()
    if "N o r m a l    t e r m i n a t i o n" in data:
        pass
    elif "E r r o r   t e r m i n a t i o n" in data:
        print("Error in simulation n:{}".format(index))
    else:
        print("Error -{}".format(index))

    return


if __name__ == "__main__":
    fire.Fire(run_dyna_model)
