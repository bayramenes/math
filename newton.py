from polynomial import polynomial

# create a new instance
main_poly=polynomial()


# set the polynomial 
degree=main_poly.set_the_poly()


print(f'The degree of the polynomail is : {degree}')
derivative=polynomial()
derivative.replace_poly(main_poly.differentiate())


iterationCount=int(input('How many steps do you want: '))
firstGuess=float(input('What is your fist guess: '))

# keep count of how many iterations
i=0

# just to compare some cool sensitivity properties of this method and its convergence
list_of_guesses=[]

# the real deal
def newton_raphson(guess):
    global i
    initialGuess=guess
    list_of_guesses.append(initialGuess)
    # stop if have gotten to the desired iteration count
    if i==iterationCount:
        print(initialGuess)
        print(list_of_guesses)
        exit()
    # add one more iteration record
    i = i+1
    # recall the function inside of it but after evaluating the new guess
    # if is the formula for the newton raphson method of finding roots
    newGuess=initialGuess-((main_poly.evaluate_for(initialGuess))/(derivative.evaluate_for(initialGuess)))
    newton_raphson(newGuess)


newton_raphson(firstGuess)
