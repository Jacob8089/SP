a=[5,10,6,4,2,7,3,4,1]

def mean(data=[],int r,*args):
    sum=0
    for i in range(0,len(data)):
        sum+=data[i]
    mean_val=sum/len(data)
    return round(mean_val,r)

def variance(data=[],*args):
    var=0
    for i in range(0,len(data)):
         var+=(data[i]-mean(data))**2
    var_val=var/len(data)
    return round(var_val,4)

def sv(data=[],*args):
    sv_val=variance(data)**0.5
    return round(sv_val,4)

print(mean(a,4))
print(variance(a))
print(sv(a))