import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    (True, (9.93570222, 0.000023))
    """
    col_handedness = "handedness"
    col_avg = "avg"
    bf = pandas.read_csv(filename)
    # print(bf)
    rhands = bf[bf.loc[:, col_handedness] == 'R']
    lhands = bf[bf.loc[:, col_handedness] == 'L']
    # print(rhands)
    ttest = scipy.stats.ttest_ind(rhands[col_avg], lhands[col_avg], equal_var=False)
    # print(ttest)
    return ttest[1] > .05, ttest

result = compare_averages('baseball_stats.csv')
print "result: ", result
