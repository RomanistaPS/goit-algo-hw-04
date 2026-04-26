# from pathlib import Path

# parent_folder_path = Path(r'D:/Projects/goit-algo-hw-04')

# def parse_folder(path):
#     for element in path.iterdir():
#         if element.is_dir():
#             print(f"Parse folder: This folder's name is - {element.name}")
#             parse_folder(element)    
#         if element.is_file():
#             print(f"Parse file: This file's name is - {element.name}")

# parse_folder(parent_folder_path)

# from pathlib import Path

# file_name = Path('jokes.txt')

# try:
#     file = open(file_name, 'r', encoding='utf-8')
#     try:
#         while True:
#             line = file.readline()
#             if not line:
#                 break
#             print(line, end='')
#     except OSError:
#         print('Error while reading file')
#     finally:
#         file.close()
# except OSError:
#     print('OSError')

# from pathlib import Path

# file_name = Path('jokes.txt')

# try:
#     with open(file_name, 'r', encoding='utf-8') as file:
#         for line in file:
#             print(line, end='')
# except Exception as e:
#     print(f"{e} with file")

# from pathlib import Path

# file_name = Path('test_txt.txt')

# try:
#     file_name.unlink()
# except FileNotFoundError:
#     pass

# file_name.unlink(missing_ok=True) #for delete file this best

from pathlib import Path

file_path = Path('./some_txt_file/test_data.txt')

data = ['first line', 'second line' , 'third line', 'fourth line']
with open(file_path, 'w', encoding='utf-8') as file:
    # for line in data:
    #     file.write(f"{line}\n")
    # or short variant 
    file.write('\n'.join(data))
with open(file_path, 'a', encoding='utf-8') as file:
    file.writelines('\nfive line')

# import shutil

# archive = shutil.make_archive('backup', 'zip', 'some_txt_file')
# print(archive)

# shutil.unpack_archive(archive, 'some_txt_file_new')