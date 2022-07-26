# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:47:48 2022

@author: HFLAB
"""
file = 'ETH.car'
moles = []
with open(file,encoding='utf-8') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split()
    if lines[i][0] == 'PBC': system_size = [float(item) for item in lines[i][1:4]]
for i in range(len(lines)):
    if lines[i][0] == 'PBC': break

temp = []
for j in range(i+1,len(lines)):
    if lines[j][0] != 'end':
        temp.append([lines[j][5]]+lines[j][:5])
    else:
        moles.append(temp)
        temp = []
moles = sorted(moles[:-1])
total_atom = sum([len(x) for x in moles])

output = []
mole_count, atom_count = 1, 1
for mole in moles:
    for atom in mole:
        output.append([mole_count,atom[5][:-1],atom[1],atom_count,float(atom[2])/10,float(atom[3])/10,float(atom[4])/10])
        atom_count += 1
    mole_count += 1

with open('conf.gro',"w",encoding='utf-8') as f:
    f.write('System\n')
    f.write(' '+str(total_atom)+'\n')
    for i in range(len(output)):
        f.write("%5d%-5s%5s%5d%8.3f%8.3f%8.3f\n" %(output[i][0],output[i][1],output[i][2],output[i][3],output[i][4],output[i][5],output[i][6]))
    f.write("%10.5f%10.5f%10.5f"%(system_size[0]/10,system_size[1]/10,system_size[2]/10))
    f.write('\n')