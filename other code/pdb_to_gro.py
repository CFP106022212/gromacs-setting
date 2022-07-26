# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 22:52:30 2022

@author: Administrator
"""
file = 'mix.pdb'
output = []
with open(file,encoding='utf-8') as f:
    lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split()
    if lines[i][0] == 'CRYST1': system_size = [float(item) for item in lines[i][1:4]]
for i in range(len(lines)):
    if lines[i][0] == 'CRYST1': break
mole_class = 'A'
preclass_num = 0
for j in range(i+1,len(lines)-1):
    if lines[j][0] == 'CONECT': break
    if lines[j][4] != mole_class:
        preclass_num = output[-1][0]
        mole_class = lines[j][4]
    output.append([int(lines[j][5])+preclass_num,lines[j][3],lines[j][2],int(lines[j][1]),float(lines[j][6])/10,float(lines[j][7])/10,float(lines[j][8])/10])

total_atom = output[-1][3]
with open('conf.gro',"w",encoding='utf-8') as f:
    f.write('System\n')
    f.write(' '+str(total_atom)+'\n')
    for i in range(len(output)):
        f.write("%5d%-5s%5s%5d%8.3f%8.3f%8.3f\n" %(output[i][0],output[i][1],output[i][2],output[i][3],output[i][4],output[i][5],output[i][6]))
    f.write("%10.5f%10.5f%10.5f"%(system_size[0]/10,system_size[1]/10,system_size[2]/10))
    f.write('\n')