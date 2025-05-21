#username is not more 12 char
#username is not include space
#username is not include digits

name = input("masukkan nama anda = ")

if len(name)> 12:
    print("nama tidak boleh lebih dari 12 huruf")
elif not name.find(" ") == -1:
    print("nama tidak boleh ada spasi")
elif not name.isalpha():
    print("nama harus huruf")
else:
    print(name)
