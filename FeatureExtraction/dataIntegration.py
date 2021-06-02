
# pathw = '5-gon-translation.txt'
pathw = '../Data/feature443.txt'
fw = open(pathw,'w')
for i in range(1,101):
    for j in range(1,9):
        # pathr = '5-gon-translation/'+str(i)+'_'+str(j)+'.txt'
        pathr = '../Data/feature443/'+str(i)+'_'+str(j)+'.txt'
        fr = open(pathr,'r')
        fw.write(fr.read())
        fr.close()
fw.close()
            