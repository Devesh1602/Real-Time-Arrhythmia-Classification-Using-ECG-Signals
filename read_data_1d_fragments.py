import glob
import random
import numpy as np
import wfdb
from preprocessing import preprocess

count = {'N': 0,
             'A': 0,
             '(AFL': 0,
             '(AFIB': 0,
             '(SVTA': 0,
             '(PREX': 0,
             'V': 0,
             '(B': 0,
             '(T': 0,
             '(VT': 0,
             '(IVR': 0,
             '(VFL': 0,
             'F': 0,
             'L': 0,
             'R': 0,
             '(BII': 0,
             '/': 0}
beats_data = {}

def full_check(c):
    check = {'N': 283,
                 'A': 66,
                 '(AFL': 20,
                 '(AFIB': 135,
                 '(SVTA': 13,
                 '(PREX': 21,
                 'V': 133,
                 '(B': 55,
                 '(T': 13,
                 '(VT': 10,
                 '(IVR': 10,
                 '(VFL': 10,
                 'F': 11,
                 'L': 103,
                 'R': 62,
                 '(BII': 10,
                 '/': 45}
    while True:
        symb = max(c, key=c.get)
        if c[symb] == 0:
            return None
        val = count[symb]
        if val == check[symb]:
            c[symb] = 0
        else:
            count[symb] += 1
            return symb

default = {'N': 0,
                 'A': 0,
                 '(AFL': 0,
                 '(AFIB': 0,
                 '(SVTA': 0,
                 '(PREX': 0,
                 'V': 0,
                 '(B': 0,
                 '(T': 0,
                 '(VT': 0,
                 '(IVR': 0,
                 '(VFL': 0,
                 'F': 0,
                 'L': 0,
                 'R': 0,
                 '(BII': 0,
                 '/': 0}
X = []
y = []
def read_data():
    # read all files in data dir
    files = glob.glob('data/*.dat')

    for record in files:
        print(record)
        record = record[:-4]
        signals, fields = wfdb.rdsamp(record, channels = [0])
        annotation = wfdb.rdann(record, 'atr')
        j = 0
        i = 1
        c = {'N': 0,
                 'A': 0,
                 '(AFL': 0,
                 '(AFIB': 0,
                 '(SVTA': 0,
                 '(PREX': 0,
                 'V': 0,
                 '(B': 0,
                 '(T': 0,
                 '(VT': 0,
                 '(IVR': 0,
                 '(VFL': 0,
                 'F': 0,
                 'L': 0,
                 'R': 0,
                 '(BII': 0,
                 '/': 0}
        data = {}
        while j < len(annotation.sample):
            if annotation.sample[j] < 3600*i:
                if annotation.symbol[j] in count:
                    c[annotation.symbol[j]] += 1
                elif annotation.symbol[j] == '+' and annotation.aux_note[j].strip('\x00') in count:
                    c[annotation.aux_note[j].strip('\x00')] += 1
                j += 1
            else:
                sig = signals[3600*(i-1):3600*i]
                symb = full_check(c)
                if symb:
                    data[i] = {'signal': sig,
                               'symbol': symb}
                    if symb in beats_data:
                        beats_data[symb].append(sig)
                    else:
                        beats_data[symb] = [sig]
                    X.append(sig)
                    y.append(symb)
                c = default
                i += 1

    print('Hello')
    sum = 0
    X_train = []
    y_train = []
    X_validation = []
    y_validation = []
    X_test = []
    y_test = []
    for key, pair in beats_data.items():
        print(key+' -count is: '+str(len(pair)))
        sum += len(pair)
        random.shuffle(pair)
        train_idx = int(0.7*len(pair))
        valid_idx = train_idx + int(0.15*len(pair))
        train = pair[ : train_idx]
        validation = pair[train_idx : valid_idx]
        test = pair[valid_idx : ]
        X_train.extend(train)
        X_validation.extend(validation)
        X_test.extend(test)
        y_train.extend([key]*len(train))
        y_validation.extend([key] * len(validation))
        y_test.extend([key] * len(test))
    print('Total: '+ str(sum))
    X_train = preprocess(signals = X_train, type = 2)
    X_validation = preprocess(signals=X_validation, type=2)
    X_test = preprocess(signals=X_test, type=2)
    return np.array(X_train), np.array(y_train), np.array(X_validation), np.array(y_validation), np.array(X_test), np.array(y_test)

if __name__ == "__main__":
    X, y = read_data()