__author__ = 'bijan'
#!/bin/python
t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = map(int,raw_input().strip().split(' '))
    a = map(int,raw_input().strip().split(' '))
    if len(filter(lambda x:x<=0,a)) >=k:
        print 'NO'
    else:
        print 'YES'
