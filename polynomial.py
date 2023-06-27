class polynomial:
    def __init__(self):
        self.degree=0
        self.term_count=0

        # 2d array that has the first value as the coefficient and the second as the x power
        self.terms=[]
    def set_the_poly(self):
        while True:
            temp=[]
            temp.append(int(input('what is the coefficient(0 to stop): ')))
            if temp[0]==0:
                break
            temp.append(int(input('what is the power of x: ')))
            self.terms.append(temp)
        
        for term in self.terms:
            if term[1]>self.degree:
                self.degree=term[1]
        return self.degree


    # get the polynomial
    def get_the_poly(self):
        return self.terms


    # evaluate the polynomial for a given x value
    def evaluate_for(self,x_value):
        sum=0
        for term in self.terms:
            temp=x_value**term[1]
            temp*=term[0]
            sum+=temp
        return sum


    def evaluate_poly(x_value,poly):
        sum=0
        for term in poly:
            temp=x_value**term[1]
            temp*=term[0]
            sum+=temp
        return sum



# differentiate using the power rule
    def differentiate(self):
        temp=[]
        for term in self.terms:
            temp2=[]
            temp2.append(term[0]*term[1])
            if temp2[0]==0:
                break
            temp2.append(term[1]-1)
            temp.append(temp2)
        return temp

    def replace_poly(self,newPoly):
        self.terms=newPoly
        return self.terms

            






