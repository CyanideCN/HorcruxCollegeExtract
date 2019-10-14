import os
import argparse
import glob

def decrypt(input_path):
    path, file = os.path.split(input_path)
    file_split = file.split('.')
    if len(file_split) == 1:
        fname = file_split[0]
        ext = ''
    else:
        fname = file_split[0]
        ext = '.' + file_split[1]
    output_path = os.path.join(path, fname + '_decrypt' + ext)
    os.system('decrypt {} {}'.format(input_path, output_path))

parser = argparse.ArgumentParser()
parser.add_argument('file', help='Path of file or directory to be decrypted', type=str)
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