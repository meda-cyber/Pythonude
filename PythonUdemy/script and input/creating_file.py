f = open(r"C:\Users\User\Desktop\My_projects\Python_@Edx_Udemy\PythonUdemy\script and input\my_file.txt", "r")
file_data = f.read()
f.close()
f = open(r"C:\Users\User\Desktop\My_projects\Python_@Edx_Udemy\PythonUdemy\script and input\my_file.txt", "w")
f.write("Hello there")
f.close()


# Using python for auto closing
with open(r"C:\Users\User\Desktop\My_projects\Python_@Edx_Udemy\PythonUdemy\script and input\my_file.txt", "r") as f:
    file_data = f.read()
# another example
with open(r"C:\Users\User\Desktop\My_projects\Python_@Edx_Udemy\PythonUdemy\script and input\camelot.txt.txt", "r") as song:
    print(song.read(8))
    print(song.read(20))
    print(song.read())
