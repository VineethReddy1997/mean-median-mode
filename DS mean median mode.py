# mean-median-mode
##FUNCTION TO CALCULTE THE MEAN VALUES

def Mean(M):
    total = 0
    for i in M:
        total+= i
    Mean = total / len(M)  #sum of average values in data
    return Mean



##FUNCTION TO CALCULTE THE MEDIAN VALUES
def Median(M):
    M.sort()
    if len(M)%2 !=0:
        Median = M [int(len(M)/2)]
    else:
        Median = M [(int(len(M)/2)) -1] + M[int(len(M)/2)]
        Median = Median/2  #midle of the values in data
    return  Median

##FUNCTION TO CALCULTE THE MODE VALUES
def Mode(M):
    counter=0
    num = [0]

    for k in M:
        frequency=M.count(k)   
        if(frequency > counter):
            counter = frequency  ## more repeated values in data 
            num = 1
        if len(set(M))==len(M):
            return 'there is no mode'
    return num

number_list = []     #declaration of values by calculated numbers
while(True):
    tell = input("enter a number and say 'stop' to end:  ")
    if tell == 'stop':
        break
    number_list.append(int(tell))

Mean=str(Mean(number_list))
Median=str(Median(number_list))
Mode=str(Mode(number_list))

##printing the mean median and mode value
print('Mean: '+ Mean +'\n' + 'Median: '+ Median + '\n'+ 'Mode: '+ Mode + '\n')  
print('Thank You')