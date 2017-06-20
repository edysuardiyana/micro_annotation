__author__ = 'edy'

import ConfigParser

def configParser(section):

    Config = ConfigParser.ConfigParser()
    Config.read('prop.ini')
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def listname_path():
    path = configParser("SectionOne")['listname_path']
    return path

def sampling_rate():
    samp_rate = int(configParser("SectionOne")['sampling_rate'])
    return samp_rate

def init_val():
    in_val = int(configParser("SectionOne")['initval'])
    return in_val

def end_val():
    en_val = int(configParser("SectionOne")['endval'])
    return en_val

def source_path_data(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_data']
    source_path= path+name+'.txt'
    return source_path

def source_path_scaled(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_scaled']
    scaled_path = path+name+'.csv'
    return scaled_path

def source_path_micro(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_micro']
    micro_path = path+name+'.csv'
    return micro_path

def source_path_active(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_active']
    active_path = path + name +'.csv'
    return active_path

def source_path_features(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_features']
    features_path = path + name + '.csv'
    return features_path

def source_runtime(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_runtime']
    runtime = path + name + '.csv'
    return runtime

def class_result():
    path = configParser("SectionOne")['result']
    return path
