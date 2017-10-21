import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
import os

path = os.getcwd()

def storeInFile(n,txt):
    with open(os.path.join(path, str("data\\")) + str(n)+'.txt','a') as f:
        f.write(txt+'\n')
        f.close()

def repeats(string):
    prefix_array=[]
    for i in range(len(string)):
        prefix_array.append(string[:i])
    #see what it holds to give you a better picture
        #print (prefix_array)

    #stop at 1st element to avoid checking for the ' ' char
    for i in prefix_array[:1:-1]:
        if string.count(i) > 1 :
            #find where the next repetition starts
            offset = string[len(i):].find(i)
            return string[:len(i)+offset]
            break

    return string    

def plot(p,p_notNone):
    # data to plot
    n_groups = 8
    none = (q[1],q[2],q[3],q[4],q[5], q[6], q[7], q[8])
    not_none = (q_notNone[1],q_notNone[2],q_notNone[3],q_notNone[4],q_notNone[5], q_notNone[6], q_notNone[7], q_notNone[8])
 
    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
 
    rects1 = plt.bar(index, none, bar_width,
                     alpha=opacity,
                     color='b',
                     label='None')
 
    rects2 = plt.bar(index + bar_width, not_none, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Not None')
 
    plt.xlabel('Parameters')
    plt.ylabel('Percentage')
    plt.title('Percentage based on various parameters')
    plt.xticks(index + bar_width, ('quotes', 'alphanum', 'hash', 'num', '.com', 'card no.', 'repeat', 'city name'))
    plt.legend()
 
    plt.tight_layout()
    plt.show()


def t_plot(p,p_notNone):
    n_groups = 10
    c1,c2=0,0
    count_none=[0,0,0,0,0,0,0,0,0,0]
    count_notNone=[0,0,0,0,0,0,0,0,0,0]
    x=p[0]
    y=p_notNone[0]
    for i in x:
        c1+=1
        try:
            count_none[i]+=1
        except:
            continue
    for i in y:
        c2+=1
        try:
            count_notNone[i]+=1
        except:
            continue
    # create plot
    for j in range(0,len(count_none)):
        count_none[j]=(count_none[j]/tot)*100
    for j in range(0,len(count_notNone)):
        count_notNone[j]=(count_notNone[j]/tot)*100
    count_none=tuple(count_none)
    count_notNone=tuple(count_notNone)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
 
    rects1 = plt.bar(index, count_none, bar_width,
                     alpha=opacity,
                     color='b',
                     label='None')
 
    rects2 = plt.bar(index + bar_width, count_notNone, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Not None')
 
    plt.legend()
 
    plt.tight_layout()
    plt.show()


f1=pd.read_excel('outFile.xlsx','outFile')

factual_name=f1['factual_name']
output_name=f1['output']
score=f1['score']

f2=pd.read_csv('factual_us_city_state_zip.csv',header=None)
factual_city=f2[1]
factual_state_full=f2[2]
factual_state_short=f2[3]
a=0

#print(factual_name[:10])
factual_city=list(factual_city)
factual_state_short=list(factual_state_short)

a=0
count=0
p=[[],0,0,0,0,0,0,0,0]
p_notNone=[[],0,0,0,0,0,0,0,0,0]

q=[[],0,0,0,0,0,0,0,0]
q_notNone=[[],0,0,0,0,0,0,0,0]

master=[]

for f,o in zip(factual_name,output_name):
    count+=1
    print(count)
    tot=len(factual_name)
    o=str(o)
    o=o.strip()
    if(o=="None"):
        #print(f,o)
        temp=f
        f=f.split(' ')
        if(len(f)>=1):         
            #print ("Total number of occurances of spaces in %s is %d"% (col_val, col_val.count(' ')))
            p[0].append(len(f)-1)
        if temp[0]==("\"") and temp[-1]==("\""):
            p[1]+=1
        if '.com' in temp:
            p[2]+=1
        if re.match('.*[x]{3,}[0-9]{1,}.*',temp):
            p[3]+=1
        if re.match('.*#[0-9]{1,6}.*',temp):
            p[4]+=1
        if re.match('[0-9]',temp):
            p[5]+=1
        if re.match('.*[a-zA-Z].[0-9].*',temp):
            p[6]+=1
        if(temp!=repeats(temp)):
            p[7]+=1
        for x in f:
            if(x in factual_state_short or x in factual_city):
                #print(temp)
                p[8]+=1
                break
        n = len(temp.strip())
        storeInFile(n,str(temp.strip()))
        master.append(len(temp))
    elif(o==None):
        a+=1;
    else:     
        if(len(f)>1):         
            #print ("Total number of occurances of spaces in %s is %d"% (col_val, col_val.count(' ')))
            p_notNone[0].append(len(f)-1)
        if temp[0]==("\"") and temp[-1]==("\""):
            p_notNone[1]+=1
        if '.com' in temp:
            p_notNone[2]+=1
        if re.match('.*[x]{3,}[0-9]{1,}.*',temp):
            p_notNone[3]+=1
        if re.match('.*#[0-9]{1,6}.*',temp):
            p_notNone[4]+=1
        if re.match('[0-9]',temp):
            p_notNone[5]+=1
        if re.match('.*[a-zA-Z].[0-9].*',temp):
            p_notNone[6]+=1
        if(temp!=repeats(temp)):
            p_notNone[7]+=1
        for x in f:
            if(x in factual_state_short or x in factual_city):
                #print(temp)
                p_notNone[8]+=1
                break
        if str(f).strip()== str(o).strip():
            p_notNone[9]+=1
           
        
q[1]=(p[1]/tot)*100
q[2]=(p[2]/tot)*100
q[3]=(p[3]/tot)*100
q[4]=(p[4]/tot)*100
q[5]=(p[5]/tot)*100
q[6]=(p[6]/tot)*100
q[7]=(p[7]/tot)*100
q[8]=(p[8]/tot)*100

q_notNone[1]= (p_notNone[1]/tot)*100
q_notNone[2]= (p_notNone[2]/tot)*100
q_notNone[3]= (p_notNone[3]/tot)*100
q_notNone[4]= (p_notNone[4]/tot)*100
q_notNone[5]= (p_notNone[5]/tot)*100
q_notNone[6]= (p_notNone[6]/tot)*100
q_notNone[7]= (p_notNone[7]/tot)*100
q_notNone[8]= (p_notNone[8]/tot)*100
q_notNone[9]= (p_notNone[9]/tot)*100

print("\ntotal number of merchant descriptions is %d" %tot)
#print("\ncount whose exact match is found", p_notNone[9])
print("\npercentage whose exact match is found", q_notNone[9])
print("\npercentage where no value is found", (a/tot)*100)
print("\nwhen the output is None")

for i in range(0,(max(master))+1):
    if(master.count(i)>0):
        length=master.count(i)
        print ("percentage of occurances of %d characters in merchant names is %.2f %%"% (i, (length/tot)*100))
        #print ("Total number of occurances of %d is %d"% (i, master.count(i)))


for s in range(0,(max(p[0]))+1):
    if(p[0].count(s)>0):
        sp=p[0].count(s)
        print("percentage of occurances of %d spaces is %.2f %%"%(s, (sp/tot)*100))
        #print ("Total number of occurances of %d spaces is %d"% (s, p[0].count(s)))
print("percentage of quotes ",q[1])
print("percentage of .com ",q[2])
print("percentage of credit card ",q[3])
print("percentage of hash ",q[4])
print("percentage of numeric ",q[5])
print("percentage of alphanumeric ",q[6])
print("percentage of repeats ",q[7])
print("percentage of city in merchant name ",q[8])

print("\nwhen the output is Not None")
for s in range(0,(max(p_notNone[0]))+1):
    if(p_notNone[0].count(s)>0):
        sporig=p_notNone[0].count(s)
        print("percentage of occurances of %d spaces is %.2f %%"%(s, (sporig/tot)*100))
        #print ("Total number of occurances of %d spaces is %d"% (s, p[0]_notNone.count(s)))
print("percentage of quotes ",q_notNone[1])
print("percentage of .com ",q_notNone[2])
print("percentage of credit card ",q_notNone[3])
print("percentage of hash ",q_notNone[4])
print("percentage of numeric ",q_notNone[5])
print("percentage of alphanumeric ",q_notNone[6])
print("percentage of repeats ",q_notNone[7])
print("percentage of city in merchant name ",q_notNone[8])

t_plot(p,p_notNone)            
plot(p,p_notNone)
