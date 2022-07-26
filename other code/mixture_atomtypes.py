# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 01:16:23 2022

@author: Administrator
"""
files = ['oleic.itp','ETH.itp']
atomtypes = [[] for _ in range(len(files))]
atoms     = [[] for _ in range(len(files))]
index     = [[] for _ in range(len(files))]
for count in range(len(files)):
    with open(files[count]) as f:
        lines = f.readlines()
    for j in range(len(lines)):
        if 'atomtypes' in lines[j]: break
    index[count].append(j)
    for i in range(j+1,len(lines)):
        if 'moleculetype' in lines[i]: break
        atomtypes[count].append(lines[i])
    index[count].append(i)
    index[count].append(i+5)
    for j in range(i+5,len(lines)):
        if 'bonds' in lines[j]: break
        atoms[count].append(lines[j])
    index[count].append(j)
pre = 0

for i in range(len(atomtypes)):
    atomtypes[i] = sorted(atomtypes[i])
    for j in range(len(atomtypes[i])):
        atoms[i][j]     = atoms[i][j].replace(atoms[i][j][9:17],'atms_'+str(j+pre).zfill(3))
        atomtypes[i][j] = atomtypes[i][j].replace(atomtypes[i][j][ 2:10],'atms_'+str(j+pre).zfill(3))
        atomtypes[i][j] = atomtypes[i][j].replace(atomtypes[i][j][12:16],atomtypes[i][j][12]+str(j+pre).zfill(3))
    pre += j+1

for count in range(len(files)):
    with open(files[count]) as f:
        lines = f.readlines()
    lines[index[count][2]:index[count][3]] = atoms[count]
    del lines[index[count][0]:index[count][1]]
    with open(files[count][:-4]+'_1.itp','w') as f:
        f.writelines(lines)

atomtypes_output = ['[ atomtypes ]\n']
for item in atomtypes:
    atomtypes_output += item

with open('atomtypes.txt','w') as f:
    f.writelines(atomtypes_output)