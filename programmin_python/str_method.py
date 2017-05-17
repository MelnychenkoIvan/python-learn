s1, s2 = "        str\n\r\v\t", "sttsrstrstrokstrstrstr"
print("{} - {}".format(s1.strip(), s2.strip('str')))

s3 = 'world1, world2, world3, world4'
print(s3.split())
print(s3.split(', '))

print(s3[4:5])
