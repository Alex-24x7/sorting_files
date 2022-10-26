import os, sys
targetFile = open('List.txt', 'w')
maskFile = open('mask.txt', 'r')
mask = maskFile.read().split(',')
list_communis = []
list_communis_number = []
list = []

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        list_communis.append(os.path.join(root, name))


def name_bypass(i_mask):
    i = 0
    j = len(list_communis) - 1
    while i <= j:
        filed_name = (list_communis[i].split(sep='/'))
        if mask[i_mask] in filed_name[(len(filed_name)-1)]:
            if i not in list_communis_number:
                list.append(list_communis[i])
                list_communis_number.append(i)
                i +=1
            else:
                i += 1
        else:
            i +=1

def other_name(list_other):
    i = 0
    j = len(list_communis) - 1
    while i <= j:
        if i not in list_other:
            list.append(list_communis[i])
            i +=1
        else:
            i +=1


i_mask = 0
j_mask = len(mask) - 1

while i_mask <= j_mask:
    name_bypass(i_mask)
    i_mask += 1

other_name(list_communis_number)

for element in list:
     targetFile.write(element)
     targetFile.write('\n')
targetFile.close()
maskFile.close()
