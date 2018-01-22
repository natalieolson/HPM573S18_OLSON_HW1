yours = ['Yale', 'MIT' , 'Berkeley']
mine = ['UC Davis', 'Yale' , 'UCLA']

ours1 = mine + yours
print(ours1)

ours2 = []
ours2.append(mine)
print(ours2)
ours2.append(yours)
print(ours2)

#ours1 adds each item to the total set (6 total items), while ours2 adds each set individually (2 total items)

yours[1] = 'Pepperdine'
print(yours)

print(ours1)
print(ours2)

#ours2 reflects the change in yours because it adds the set yours independently, while ours1 creates and stores a set and doesn't reflect the change
