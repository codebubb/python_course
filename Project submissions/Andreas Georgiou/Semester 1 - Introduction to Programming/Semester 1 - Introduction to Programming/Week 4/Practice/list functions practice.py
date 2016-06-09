phones = ["Samsung", "Apple", "HTC", "Sony", "Microsoft Lumia",
          "LG", "Blackberry"]

phones.append("Nokia")

phones.sort()

topoflist = phones.pop(1)


show_place = phones.index("Apple")

for i in phones:
    print i

print phones
print show_place

print len(phones)

print topoflist
