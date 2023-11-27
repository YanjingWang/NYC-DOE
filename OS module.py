import os
print(dir(os))
print(os.getcwd())
#os.chdir('C:\Users\Ywang36\Desktop')
print(os.getcwd())

print(os.listdir())
#os.mkdir('OS-Demo')
#os.makedirs('OS-Demo-1/Sub-Dir-1')

# os.rmdir('OS-Demo')
# os.removedirs('OS-Demo-1/Sub-Dir-1')

# os.rename('OOP.py', 'OOP_ALL.py')
print(os.stat('OOP_01.py'))
#print(os.stat('OOP_01.py).st_size) #1844

from datetime import datetime
#os.chdir('////////////')
mod_time = os.stat('OOP_01.py').st_mtime
print(datetime.fromtimestamp(mod_time))

# os.walk()  # yield the directory path the direct within that path and the files within
"""
go through the entire tree to find the file location
"""
# for dirpath, dirnames, filenames in os.walk('////////////////////////'):
#     print('current path : ', dirpath)
#     print('Directories : ', dirnames)
#     print('Files : ', filenames)
#     print()

print(os.environ.get('HOME'))
file_path = os.environ.get('HOME') + 'test.txt'  # don't double slashes or no slash
file_path2= os.environ.join(os.environ.get('home'), 'test.txt')
print(file_path2)

# with open(file_path,'w')

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))
