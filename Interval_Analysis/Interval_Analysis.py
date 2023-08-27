import numpy as np
import matplotlib.pyplot as plt

class Interval:
    def __init__(self, left, right=None):
        if right is None:
            self.left, self.right = left, left
        else:
            self.left, self.right = left, right
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = Interval(other, other)
            
        a, b = self.left, self.right
        c, d = other.left, other.right
        return Interval(a+c, b+d)
    
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            other = Interval(other, other)
            
        a, b = self.left, self.right
        c, d = other.left, other.right
        return Interval(a+c, b+d)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = Interval(other, other)
            
        a, b = self.left, self.right
        c, d = other.left, other.right
        return Interval(a-d, b-c)
    
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = Interval(other, other)
            
        a, b = self.left, self.right
        c, d = other.left, other.right
        return Interval(min(c-a, c-b), max(d-a, d-b))
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = Interval(other, other)
        
        a, b = self.left, self.right
        c, d = other.left, other.right
        return Interval(min(a*c, a*d, b*c, b*d), max(a*c, a*d, b*c, b*d))
    
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            other = Interval(other, other)
            
        a, b = self.left, self.right
        c, d = other.left, other.right
        return Interval(min(a*c, a*d, b*c, b*d), max(a*c, a*d, b*c, b*d))

    def __truediv__(self, other):
        a, b = self.left, self.right
        c, d = other.left, other.right
        if c == 0 or d == 0:
            raise Exception(f"Error dividing by zero! The second interval that is used to divide the first interval contains a zero value.")
        
        return Interval(min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d))

    def __repr__(self):
        return f'[{self.left},{self.right}]'
    
    def __contains__(self, number):
        if number >= self.left and number <= self.right:
            return True
        else:
            return False
        
    def __pow__(self, power):
        if self.left<0 and self.right>0:
            return Interval(min(0, self.left**power, self.right**power), max(self.left**power, self.right**power))
        else:
            return Interval(min(self.left**power, self.right**power), max(self.left**power, self.right**power))


I4 = Interval(1)
print(I4)

# Task 8
print(Interval(2,3) + 1)
print(1 + Interval(2,3))
print(Interval(2,3) + 1.0)
print(1.0 + Interval(2,3))

print(Interval(2,3) - 1)
print(1 - Interval(2,3))
print(Interval(2,3) - 1.0)
print(1.0 - Interval(2,3))

print(Interval(2,3) * 1)
print(1 * Interval(2,3))
print(Interval(2,3) * 1.0)
print(1.0 * Interval(2,3))

# Task 4
I0 = Interval(1, 2)
print(I0)

I1 = Interval(1, 4)
I2 = Interval(-2, -1)

I1_plus_I2 = I1 + I2
print(I1_plus_I2)

I1_minus_I2 = I1 - I2
print(I1_minus_I2)

I1_multiply_I2 = I1*I2
print(I1_multiply_I2)

I1_divide_I2 = I1/I2
print(I1_divide_I2)

# Task 5 (Additional)        
I3 = Interval(1, 4)
print(1 in I3)
print(7 in I3)

# Task 9
x = Interval(-2,2)
x_power_2 = x**2
print(f'[{x_power_2.left},{x_power_2.right}]')
x_power_3 = x**3
print(f'[{x_power_3.left},{x_power_3.right}]')


#%% Task 10 (Prep)
b = []

for n in np.linspace(0., 1, 1000):
    b.append(3*(Interval(n, n+0.5)**3) - 2*(Interval(n, n+0.5)**2) - 5*(Interval(n, n+0.5)) - 1)
    
print(b)

#%% Task 10
yl = []
yu = []

for n in np.linspace(0., 1, 1000):
    a = 3*(Interval(n, n+0.5)**3) - 2*(Interval(n, n+0.5)**2) - 5*(Interval(n, n+0.5)) - 1
    yl.append(a.left)
    yu.append(a.right)
    
print(yu)

x_axis = [x for x in np.linspace(0., 1, 1000)]
y1 = yl
y2 = yu

plt.plot(x_axis, y1, color='b')
plt.plot(x_axis, y2, color='g')

plt.xlim(0.0, 1.0)
plt.ylim(-10, 4)

plt.title('$p(I) = 3I^{3} - 2I^{2} - 5I - 1$, I = Interval (x, x + 0.5)')
plt.ylabel('p(I)')
plt.xlabel('x')

plt.show()

        

