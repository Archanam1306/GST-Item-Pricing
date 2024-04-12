import csv
#gst file {category,gst]
n=int(input('Enter the no.of categories:'))
g1=open('GST.csv','w',newline='')
w1=csv.writer(g1)
gst={}
for i in range(n):
    l=[]
    na=input('Enter the category:')
    pe=float(input('Enter the GST in %:'))
    gst[na]=pe
    l=[na,pe]
    w1.writerow(l) 
g1.close()
#items file [item id, item name, category, unit price]
m=int(input('Enter the no.of elements:'))
t1=open('Items.csv','w',newline='')
r1=csv.writer(t1)
#final file [item id, item name, unit price, gst,total price]
f1=open('Final.csv','w',newline='')
fr=csv.writer(f1)
for j in range(m):
    k=[]
    it=int(input('Enter item id:'))
    itn=input('Enter item name:')
    ct=input('Enter the category:')
    up=int(input('Enter the unit price:'))
    k=[it,itn,ct,up]
    r1.writerow(k)
    y=[]
    for i in gst:
        if ct==i:
            tp=up+up*(gst[i]/100)
            y=[it,itn,up,gst[i],tp]
            fr.writerow(y)
f1.close()
t1.close()

#display
print('\t\t\tGST')
print('\t\t\t***')
g2=open('GST.csv','r',newline='')
w2=csv.reader(g2)
print('\t','Category\t\tGST')
for i in w2:
    for j in range(len(i)):
        print('\t',i[j],'\t\t',i[j+1],end='\n')
        break

print('\n\t\t\tItems')
print('\t\t\t*****')
t2=open('Items.csv','r',newline='')
x=csv.reader(t2)
print('\tItem id\t\tItem name\tCategory\t\tUnit Price')
for i in x:
    for j in range(len(i)):
        print('\t',i[j],'\t\t',i[j+1],'\t\t',i[j+2],'\t\t',i[j+3],end='\n')
        break

print('\n\t\t\tFINAL')
print('\t\t\t*****')
f2=open('Final.csv','r',newline='')
fr2=csv.reader(f2)
print('\tItem id\t\tItem name\tUnit Price\tGST\t\tTotal price')
for i in fr2:
    for j in range(len(i)):
        print('\t',i[j],'\t\t',i[j+1],'\t\t',i[j+2],'\t\t',i[j+3],'\t\t',i[j+4],end='\n')
        break
