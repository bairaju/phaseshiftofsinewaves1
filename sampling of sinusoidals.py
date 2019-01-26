import matplotlib.pyplot as plt
import numpy as np
f=input("Enter the input frequency:")
fs=input("Enter the sample frequency:")
a=np.linspace(0,10,50)
b=np.linspace(0,10,1000)
y=np.sin(2*np.pi*b*(float(f)))
x=np.sin(2*np.pi*a*(float(f)/float(fs)))
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax3=fig.add_subplot(2,1,2)
ax1.plot(b,y)
ax3.set_title("Sampled sine wave")
ax3.stem(a,x)
