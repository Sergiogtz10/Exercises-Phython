#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(dollar,cent,n_cupcakes):
    cost = (n_cupcakes *dollar * 100) + (n_cupcakes * cent)
# La variable total cost se pasa a centavos 
    return int(cost/100), cost%100
# Devolvemos a dolares cost y establecemos los centavos con el resto


#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(10,15,2))
