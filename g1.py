import matplotlib.pyplot as plt
 
# x axis values
ss=[]
s = [('h1'),('h2'),('h3')]
s1=[('Infosys',), ('Amazon',), ('Flipcart',), ('Reliance',), ('Wipro',)]
for i in s1:
    for n in i:
        ss +=n.split(",")
print(ss)
# corresponding y axis values
import matplotlib.pyplot as plt
 
# x axis values
x = [2016,2017,2018,2019,2020,2021,2022]
# corresponding y axis values
y = [24,49,77,54,13,33,99]
 
# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
 
# setting x and y axis range
plt.ylim(0,100)
plt.xlim(2016,2022)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Amazon')
 
# function to show the plot
plt.show()
