names =["sachin","sourav","Goutam","Rahul", "SAMIT"]

constant=[char for name in names if name.islower() for char in name if char not in 'aeiou']
print(constant)