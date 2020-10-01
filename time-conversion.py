#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hour,minute,second_AMPM=s.split(':')

    if second_AMPM[2:]=="PM" and hour!='12':
        hour=str(int(hour)+12)
    if second_AMPM[2:]=="AM" and hour=='12':
        hour="00"
    if second_AMPM[2:]=="'PM" and hour=='12':
        hour="12"
    
    conversion_time=hour+':'+minute+':'+second_AMPM[0:2]

    return conversion_time
    


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
