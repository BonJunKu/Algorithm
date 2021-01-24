import sys
day=['MON','TUE','WED','THU','FRI','SAT','SUN']
date=[31,28,31,30,31,30,31,31,30,31,30,31]
a,b=map(int,sys.stdin.readline().split())
print(day[sum(date[:a-1],b-1)%7])