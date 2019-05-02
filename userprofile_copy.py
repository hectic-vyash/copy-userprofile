import os
import shutil

#script functies:
# - kopieer laatst bijgewerkte versie van profiel.
# - profiel kan .devoogt.local bevatten of juist niks.

# user = input("Enter username: ")
# user_path = "C:\\Users\\" + user

# files = []

# for root, directories, files in os.walk(user_path):
#     for file in files:
#         files.append(os.path.join(root, file))
#
# for f in files:
#     print (f)

source = os.listdir("D:\\testfiles\\")

# def copyProfile():
#     # source = "C:/Users/" + username
#     source = "D:/testfiles/"
#     destination = "E:/testfiles/"
#     for file in source:
#         print ("Copying " + file)
#         shutil.copy(os.path.join('D:/testfiles/', file), destination)

# source = "D:/testfiles/"

destination = "E:/testfiles/"
for file in source:
    print("Copying " + file)
    shutil.copy(os.path.join('D:/testfiles/', file), destination)

# if __name__ == "__main__":
#     copyProfile()