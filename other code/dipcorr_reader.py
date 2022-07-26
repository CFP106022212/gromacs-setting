import pandas as pd
path = 'mixture_EOH_PA/'
dir_name = ['0','0.2','0.4','0.6','0.8','1']
result = []
for i in range(len(dir_name)):
    filename = path+dir_name[i]+'/dipcorr.xvg'
    with open(filename) as f:
        index = 0
        for line in f:
            cols = line.split()
            if len(cols) == 2 and cols[0][0].isnumeric():
                if i == 0:
                    result.append([abs(float(cols[0])),abs(float(cols[1]))])
                elif index < len(result):
                    result[index].append(abs(float(cols[1])))
                    index += 1
                else:
                    break
df = pd.DataFrame(result)
df.columns = ['time(ps)']+dir_name
df.to_excel(path[:-1]+"_dipcorr.xlsx",index=False)
