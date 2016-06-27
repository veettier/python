fname = input("Enter input name: ")
print()

try:
    fobj = open(fname,'r')
except IOError,e:
    print ("*** file open error",e)
else:
    for eachLine in fobj:
        eachLine = eachLine.strip('\n')
        print (eachLine)
    fobj.close()