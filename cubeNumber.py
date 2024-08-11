import sys
num_args = len(sys.argv)
if num_args < 3:
    print (f"number of argument supplied is less than expected , please provide at least 2 agrument")
elif num_args > 3:
    print (f"number of argument supplied is more  than expected , please provide at least 2 agrument")
elif num_args == 3 :
    print ("yess all good , i will now proceed with the calc")
    data1,data2 =  int(sys.argv[1]),int(sys.argv[2])
    print (data1 % data2)
else:
        print ("something wrong with the argument supplied")
