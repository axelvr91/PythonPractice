temps=[221, 234, 340, 230, 210, 300, 299]

new_temps=[ temp/10 if temp!=-9999 else 0 for temp in temps]
print(new_temps)