# for more details check out https://www.youtube.com/watch?v=gMlf1ELvRzc
from math import factorial,sqrt

digit_count=int(input('digit count : '))
result = 0
n=1/2

x_power=1


for term in range(digit_count):

    temp = 1

    # get the coofecient of the term 
    for multiple in range(term):
        temp*=n-multiple



    temp*=1/factorial(term)

    # since we integrated the binomial theorem from 0 to 1/2 in a circle we have to divide by the new power of x
    temp*=1/x_power
    temp*=(1/2)**x_power
    # in the binomial theorem when we substitue x with -x^2 the powers that were odd will have and x added to them which is why all of the
    # odd terms are multiplied by -1
    if term%2==1:
        temp*=-1

    # now we actually multiply this term with the x since we have integrated in terms of x from 0 to 1/2
    # but instead of integrating x we are integrating -x^2 so x in this case is  to whatever power
    x_power+=2

    result+=temp



# since we are calculating the are from 0 1/2 in a circle we divided the section into a triangle with are root of 3 / 8 and a slice of the cirlce
# that has a 30 degrees center angle which has the are of pi/12
result-=sqrt(3)/8
result*=12


print(result)



# note that we are integrating from 0 to 1/2 for a more rapidly converging series which will give us a more precise answer more quickly
# this is the isaac newton way of doing it

