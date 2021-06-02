
for i in range(1,101):
    for j in range(1,9):
        pathr = '../Data/features/'+str(i)+'_'+str(j)+'.fp'
        pathw = '../Data/cleanFeatures/'+str(i)+'_'+str(j)+'.txt'
        fr = open(pathr,'rb')
        fw = open(pathw,'w')
        byt = fr.readlines() #170 283 11 B 60
        num = int(byt[4])
        for k in range(5,num+5):
            text = str(byt[k],'utf-8').split(' ')
            fw.write(text[0]+" "+text[1]+" "+text[2]+"\n")
        fw.close()
        fr.close()