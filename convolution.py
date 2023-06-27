import numpy as np



# this is a convolution example



# lets get two random lists 
a= np.random.randint(0,100,50)
b = np.random.randint(0,100,50)

# a variable that hold what is the maximum sum for both of the indexes of the lists to be able to run through the numbers
# from 0 to that number

max = len(a)+len(b)-2

# a list which will save the results
result=[]
# run throught each number possible as indicated above
for goal in range(max+1):
    # a variable to sum all of the possible values and add them to the result
    temp=0
    # run though the list and find whether there is a fitting sum 

    for i in range(len(a)):
        for j in range(len(b)):
            if i+j==goal:
                temp+=a[i]*b[j]
    result.append(temp)

    
# for more on the maths behind this visit https://www.youtube.com/watch?v=KuXjwB4LzSA&t




