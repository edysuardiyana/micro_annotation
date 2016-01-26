__author__ = 'ArseneLupin'

import scale_file
import microannotate_right
import activefeat
import weka_file
import source_var

def main():

     ##this is the main program to pre-processing and generating the data for WEKA classifier##

    # properties for scaling process
    names = ["subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9",
             "subject_10","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17",
             "subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28",
             "subject_29","subject_31"]

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

if __name__ == '__main__':
    main()
