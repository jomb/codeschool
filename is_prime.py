def is_prime(x):
    if  x < 2:
        #print "Prostoe"
        return False
    elif x==2:
        return True
    else:
        for i in range(2,x):
            if x%i ==0:
                #print x, "%", i, "=", x%i
                #print "sostavnoe"
                return False
        return True
print is_prime(6)