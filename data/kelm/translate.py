import os
import sys

filename = sys.argv[1]
try:
    device = sys.argv[2]
except:
    device = ''

os.environ['CUDA_VISIBLE_DEVICES'] = device

from tqdm import tqdm
import pandas as pd
import malaya
import pickle
from unidecode import unidecode
import ujson as json


class Pointer:
    def __init__(self, filename):
        self.filename = filename
        self.index = 0

    def _save(self):
        with open(self.filename, 'wb') as fopen:
            pickle.dump(self.index, fopen)

    def increment(self):
        self.index += 1
        self._save()

    def load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'rb') as fopen:
            self.index = pickle.load(fopen)


def split(string):
    return len(string.split())


maxlen = 150
batch_size = 8

transformer = malaya.translation.en_ms.transformer(check_gpu = False)

pointer = Pointer(f'{filename}.pickle')
pointer.load()
index = 0
file = open(f'{filename}.translated', 'a')
with open(filename) as fopen:
    data = json.load(fopen)

for i in tqdm(range(0, len(data), batch_size)):
    if index >= pointer.index:
        batch = data[i : i + batch_size]
        L, R = [], []
        for k in range(len(batch)):
            if len(batch[k]['candidate'].split()) <= maxlen:
                L.append(batch[k])
                R.append(unidecode(batch[k]['candidate']))
        t = transformer.greedy_decoder(R)
        for k in range(len(L)):
            d = json.dumps({'en': L[k], 'candidate-ms': t[k]})
            file.write(f'{d}\n')

        file.flush()
        pointer.increment()

    index += 1

file.close()
