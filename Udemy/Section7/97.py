import os
import pathlib
import glob
import shutil

print(os.path.exists('test.csv'))
print(os.path.isfile('test.csv'))
print(os.path.isdir('Text'))

os.symlink('renamed.txt', 'symlink.txt')

os.mkdir('test_dir')
os.rmdir('test_dir')

shutil.copy('test_dir/test_dir/empty.txt',
            'test_dir/test_dir2/empty2.txt')

os.mkdir('test_dir')
os.mkdir('test_dir/test_dir2')
print(os.getcwd())