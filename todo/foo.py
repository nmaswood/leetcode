bag1 = [1,2,3,4,5,1,111,2,2,3,4]

# Remove all duplicates

no_dups_1 = set(bag1)


#print (no_dups)
bag2 =  [1,2,3,4,11,2,3,41,1]

no_dups_2 = set(bag2)



print (no_dups_1)
print (no_dups_2)

bag_3 = set()

#bag_3.add()


for  i in no_dups_1:

	if i in no_dups_2:

		bag_3.add(i)

#print (bag_3)


print (no_dups_1.intersection(no_dups_2))




