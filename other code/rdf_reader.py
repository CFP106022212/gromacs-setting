import pandas as pd
path = 'mixture_EOH_PA/'
dir_name = ['0','0.2','0.4','0.6','0.8','1']
target_name = ['EE','EP','PP']
result = pd.DataFrame()
def read_rdf(filename,result):
    with open(filename) as f:
        l = []
        for line in f:
            cols = line.split()
            if len(cols) == 2 and cols[0][0].isnumeric():
                l.append([float(cols[0]),float(cols[1])])
    result = pd.concat([result,pd.DataFrame(l)], axis=1)
    return result

for i in range(len(dir_name)):
    if dir_name[i] == '0' or dir_name[i] == '1':
        filename = path+dir_name[i]+'/rdf.xvg'
        result = read_rdf(filename,result)
    else:
        for item in target_name:
            filename = path+dir_name[i]+'/'+item+'_rdf.xvg'
            result = read_rdf(filename,result)

result.to_excel(path[:-1]+"_rdf.xlsx",index=False,header=False)
