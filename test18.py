# 文件读取，整个读取
r"""
当文件位于所处程序文件夹的子文件夹中,使用相对路径,如:with open('text_files\filename.txt') as file_object:
当文件不在程序文件夹中,使用绝对路径,如:file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
"""
with open('test_file.txt') as file_object:
    contents = file_object.read()
    print(contents)


# 文件读取，单行读取
filename = 'test_file.txt'
with open(filename) as file_object_1:
    for line in file_object_1:
        print(line)

# 创建一个包含文件各行的列表
filename = 'test_file.txt'
with open(filename) as file_object_2:
    lines = file_object_2.readlines() #创建了一个列表

for line in lines: # 文件关闭后，文件内容仍存在于列表中
    print(line.rstrip())

# 打印文件内容, line.strip()删除所有空字符串
pi_string = ''
for line in lines:
    pi_string += line.strip() 
print(pi_string)
print(len(pi_string))

# 字符串切片
print(pi_string[:20]+'...')
