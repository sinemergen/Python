import scipy.integrate

result = scipy.integrate.quad(lambda x: x+1, 0, 4.5)
print (result)