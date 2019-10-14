import os
import argparse
import glob

def decrypt(input_path):
    os.system('decrypt {} {}'.format(input_path, input_path[:-4] + '_decrypt.png'))

parser = argparse.ArgumentParser()
parser.add_argument('file', help='Path of file or directory to de decrypted', type=str)
p = parser.parse_args()
path = p.file
if os.path.isfile(path):
    decrypt(p.file)
else:
    if not path.endswith(os.path.sep):
        path += os.path.sep
    flist = glob.glob(path + '*.png')
    for f in flist:
        decrypt(f)