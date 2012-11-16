import sys
seqargs = []
for key,value in enumerate(sys.argv):
    seqargs.append(value)
print(len(seqargs))
