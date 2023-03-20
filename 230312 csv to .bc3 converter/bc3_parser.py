"""
Author : Jin Choi
GitHub : https://github.com/JinCoreana
Date : 12th March 2023
Description: This python project converts csv data in text file to .bc3 binary data.
"""

import time
import sys

if len(sys.argv) < 2:
    print("Please specify a filename to import.")
    sys.exit()

filename = sys.argv[1]

print(f"Coverting {filename} to .bc3 format")

start_time = time.time()
today_date = time.strftime("%d%m%y")
with open(filename, 'r', encoding='utf-16le') as f:
    data = f.readlines()

codes = ''
output = ''
# Header record
output += '~V|SOFT S.A.|FIEBDC-3/2002|Presto 8.8||ANSI|\n'
output += '~K|\\2\\2\\3\\2\\2\\2\\2\\EUR\\|0|\n'
output += f'~C|PROYECTO##|||0|{today_date}|0|\n'
output += '~D|PROYECTO##|01\\1\\1\\|\n'
output +=f'~C|01#||{filename.rstrip(".txt")}|0|{today_date}|0|\n'

# Data records
for i, line in enumerate(data):
    if i <3:
        continue  # skip first two lines
    fields = line.strip().split(',')
    print(f"Line {i}: {fields}")
    output += f'~C|{fields[2]}||{fields[6]}|{fields[10].rstrip(" m²")}|{today_date}|0|\n'
    codes += f'{fields[2]}\\1\\0\\'
    # output += f'~D|{fields[0]}|{"|".join(fields[2:5])}|\n'
  
code = "".join(str(i) for i in codes)
# # Footer record
# output += '~C|PROYECTO##|||0|120323|0|\n'
# output += '~D|PROYECTO##|01\\1\\1\\|\n'
output += f'~D|01#|{code}|\n'
formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
with open(f'{filename.rstrip(".txt")}_converted_{formatted_time}.bc3', 'w') as f:
    f.write(output.replace('\n', '\r\n'))
end_time = time.time()
print(f".bc3 file is now generated")
