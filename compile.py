# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import re

def replace_snp(name, trans_list):
    with open(name, 'r') as f:
        file_string = f.readlines()

    for trans in trans_list:
        snp, ch, en, abbr = trans
        if snp:
            if abbr:
                ch_en_abbr = "%s（%s，%s）" % (ch, en, abbr)
            else:
                ch_en_abbr = "%s（%s）" % (ch, en)
            snp = "'%s'" % snp
            file_string = [re.sub(snp, ch_en_abbr, line) for line in file_string]
        else:
           continue
    ext_pos = -4
    with open(name[:ext_pos] + '_compiled' + name[ext_pos:], 'w') as f:
        f.writelines(file_string)

if __name__ == "__main__":# org file path
    file_names = ['./ch1_ml_m_trans.org', './prefix_ml_m_trans.org']
    trans_list = pd.read_csv('./dict.csv').fillna(0).as_matrix()
    # print(trans_list)
    # isn(trans_list[0, -1])

    for name in file_names:
        # name = file_names[0]
        replace_snp(name, trans_list)
