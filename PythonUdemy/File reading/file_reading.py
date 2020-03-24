def cast_name_file(filename):
    Cast_name = []
    with open("file_curcus_cast_.txt") as f:
        for line in f:
            name = line.split(",")[0]
            Cast_name.append(name)
            print(Cast_name)

    return Cast_name


Cast_name = cast_name_file("file_curcus_cast_.txt")
for cast in Cast_name:
    print(cast)
