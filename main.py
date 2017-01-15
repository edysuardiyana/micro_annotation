__author__ = 'ArseneLupin'

import scale_file
import microannotate_right
import activefeat
import weka_file
import source_var

def main():

     ##this is the main program to pre-processing and generating the data for WEKA classifier##
    # properties for scaling process
    for i in range(3):
        for name in names:

            sourceFile = source_var.source_path_data(name)
            destFile = source_var.source_path_scaled(name)
            initcut = source_var.init_val()
            endcut = source_var.end_val()

            # properties for micro-annotate
            source_file_micro = source_var.source_path_scaled(name)
            dest_file_micro = source_var.source_path_micro(name)

            source_file_active = source_var.source_path_micro(name)
            dest_file_active = source_var.source_path_active(name)

            source_weka = source_var.source_path_active(name)
            source_features = source_var.source_path_features(name)
            weka_dest = source_var.source_path_wekafile(name)

            count = str(i)
            run_time_name = name+"_"+count
            print run_time_name
            dest_runtime_file = source_var.source_runtime(run_time_name)


            #scale_file.scale_file(sourceFile, destFile, initcut, endcut) # scale the output from accelerometer, command this for OJ's scaled data
            microannotate_right.micro_annotate(source_file_micro, dest_file_micro) # re-annotate the raw data using micro-annotate
            activefeat.active_feat(source_file_active,dest_file_active) # check the active state
            weka_file.featCalc(source_weka,source_features,weka_dest, dest_runtime_file) # calculate features and create the weka file

def read_name():
    name_list = []
    path = source_var.listname_path()

    with open(path) as obj_name:
        for line in obj_name:
            raw = line.split()
            name = raw[0]
            name_list.append(name)

    return name_list


if __name__ == '__main__':
    main()
