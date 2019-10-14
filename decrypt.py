# coding=utf-8
from __future__ import print_function
import os
import argparse
import glob
import fnmatch


def valid(input_path):
    file = open(input_path, 'rb')
    magic = file.read(12)
    return magic == b'bogehcollege'


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
    if not valid(input_path):
        print('[x] Not an encrypted file: {}'.format(input_path))
        return
    if os.name == 'posix':  # Unix system need prefix
        os.system('./decrypt {} {}'.format(input_path, output_path))
    else:
        os.system('decrypt {} {}'.format(input_path, output_path))


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file', help='Path of file or directory to be decrypted', type=str)
    p = parser.parse_args()
    path = p.file
    if os.path.isfile(path):
        decrypt(p.file)
    else:
        if not path.endswith(os.path.sep):
            path += os.path.sep
        flist = find_files(path, '*.png')
        for f in flist:
            decrypt(f)


if __name__ == '__main__':
    main()
