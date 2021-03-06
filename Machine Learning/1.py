import numpy as np
def gradient_descent(x,y): 
    m_curr=0
    b_curr=0
    iterations=100
    n=len(x)
    learning_rate=0.008
    for i in range(iterations):
        y_predicted = m_curr*x + b_curr
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted) 
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd 
        print('m {},b{}, iterations{}'.format(m_curr,b_curr,i))

x=np.array([1,2,3,4,6,5])
y=np.array([99,87,65,43,22,65])

gradient_descent(x,y)

