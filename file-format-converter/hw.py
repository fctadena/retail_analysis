
import sys
import os


args = sys.argv
arg = args[1]
file_name = args[0]

print(f'This is the passed argument: {arg}, from {file_name}')

host = os.environ.get('HOST')

print(f'Connecting to {host}')