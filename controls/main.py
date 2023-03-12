def mean(data,r):
    sum=0
    for i in range(0,len(data)):
        sum+=data[i]
    mean_val=sum/len(data)
    return round(mean_val,r)

def var(data,r):
    var=0
    for i in range(0,len(data)):
         var+=(data[i]-mean(data,r))**2
    var_val=var/len(data)
    return round(var_val,r)

def sv(data,r):
    sv_val=var(data,r)**0.5
    return round(sv_val,r)
