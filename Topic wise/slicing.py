# slicing -> creating a substring by extracting elements from existing string
#           indexing[] or slice()
#           [start:stop:step]

name = "Pradeep Singh"

first_letter = name[0]
print(first_letter)

first_name = name[0:8:1]
print(first_name)

last_name = name[8::1]
print(last_name)

step = name[::2]
print(step)

reverse_name = name[::-1]
print(reverse_name)


# SLICE

URL1 = "http://shaktimaan.in/gangadhar.com"
URL2 = "http://ironman.com/tonystark.com"

slice = slice(7,-4)

print(URL1[slice])
print(URL2[slice])