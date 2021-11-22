list=[]                                                         
n=int(input("enter the number of students"))
for i in range(0,n):
    i=int(input("enter the marks of the student"))
    if (i<=50):
        list.append(i)
    else:
        print("you entered wrong marks\n re enter the marks: ")
        i=(int(input("enter the marks of the student")))
        list.append(i)

def absent(list):
    count=0
    for i in list:
        if(i==-1):
            count+=1
    return count

def max(list):
    max=list[0]
    for i in list:
        if(i>max):
           max=i
    return max
   
def min(list):
    min=list[0]
    for i in list:
        if(i<min and i!=-1):
            min=i
    return min
    
    
def sum(list):
    sum = 0
    for i in list:
        sum += i
    sum=sum + absent(list)
    return sum


def average(list):
    average=(sum(list)+absent(list))/(n-absent(list))
    return average

def frequency(list):
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    for i in list:
        if(i>=0 and i<=10):
            count1+=1
        elif(i>=11 and i<=20):
            count2+=1
        elif(i>=21 and i<=30):
            count3+=1
        elif(i>=31 and i<=40):
            count4+=1
        elif(i>=41 and i<=50):
            count5+=1
        return(count1,count2,count3,count4,count5)
 
print("Marks of student are:",list)
print("No. of absent students are:",absent(list))
print("Maximum marks are:",max(list))
print("Minimum marks are:",min(list))
print("Total marks of all students are:",sum(list))
print("Average marks of students are:",average(list))
print("Maximum frequency of marks is:",max(frequency(list)))