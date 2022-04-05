import os

rootDirectory = str((os.path.dirname(os.path.dirname(os.path.abspath(__file__))))).replace('\\', '/')

print(rootDirectory)