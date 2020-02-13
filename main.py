# This script will calculate the greatest density of points
# The script starts by calculating the greatest density of points
# in the y direction then performs a similar check for the x direction
# Where the greatest x density exists in the greatest y positions
# is the greatest overlap
# These are tuples
import random
import matplotlib.pyplot as plt
import timeit
# random.seed(3)
t1 = timeit.default_timer() # timer

# Create 2d tuple as double (to 2 digits) as x, y
pt_coord = [] # the point
intervals = [] # y intervals: lower left x,y to upper left x,y

print("Starting ...")
#print()
for i in range(100):
    x = round(random.uniform(1,20),2)
    y = round(random.uniform(1,20),2)
    pt_coord.append([x,y])
    ll_x = x - 1
    ll_y = y - 1
    ul_x = x - 1
    ul_y = y + 1
    intervals.append([ll_y,ul_y])

    plt.xlim(0, 25)
    plt.ylim(0, 25)
    plt.figure(0)
    plt.scatter(x,y,s=40)
    plt.savefig('all_points.png')

# print("All y intervals, sorted by x_coord =>", sorted(intervals))
print()
# Calculate overlap
# a = lower y-value of interval
# s = upper y-value of interval
# n = count of overlap where at least 2 is overlap
# the location of the overlap occurs when the Count is > 2 and y_high
# goes from -1 to 1 so first overlap is
# y_low => 2.11 y_high => -1 Count => 2 and overlap is y_low => 2.11
# to y_low = 2.59
count_list = []
def overlaps(intervals):
    es = []
    for a, b in intervals:
        # print(a,b)
        es.append((a, -1))
        es.append((b, 1))
    es.sort()
    # print(es)
    result = 0
    n = 0
    for a, s in es:
        if s == -1: result += n
        n -= s
        # print("y_low => ",a,"Count => ",n)
        if n >= 2 and s == -1:
            # print("Overlap: y-value start => ", a)
            count_list.append(n)
            count_list.append(a)

    return result

print ("Number of y overlaps => ", overlaps(intervals))
# print()
# print("Count_list", count_list)

# Create pairs from count_list with first value as count and second as y-value
my_pairs = list()
while(count_list):
    z = count_list.pop(0); za = count_list.pop(0)
    my_pairs.append((z,za))

#Sort by count or first number in the pair from high count to low count
def sortFirst(val):
    return val[0]

my_pairs.sort(key = sortFirst, reverse = True)
int_y_coord = max(my_pairs) # y coord in densest area of overlap

# print("List (H => L) by count, y_coord => ",my_pairs)
print()
print("Max count and y_value ", int_y_coord)
print()
# Now calculate the greatest density in the x -direction
# Start by subsetting all of the original set of points
# Constrained to the y-min and y-max centered on the y-value
# print(type(max_y_coord)) # a tuple
# Set y value max and y value min
y_interval_center = (int_y_coord[1]) # y-interval centered
y_max = y_interval_center + 1.5 # max y_value
y_min = y_interval_center - 1.5 # min y_value
print("Y-max =>", y_max)
print("Y-interval centered here => ", y_interval_center)
print("Y-min =>", y_min)
# print()
# print(sorted(pt_coord))
# Sort point coordinate list by y-coordinate
sorted_y_list = sorted(pt_coord, key=lambda y_value: y_value[1])
# print(type(sorted_y_list))
# print(sorted_y_list)
# First convert a list to a tuple 
# remove all points that are less than y_center_value + 1 and -1 and
# create a new list using list comprehension
# print()
#print("Converted coord list to tuples")
sorted_y_list = tuple(sorted_y_list)
# print(type(sorted_y_list))
# create a sorted list of coordinates using y_max and y_min
result = [j for j in pt_coord if j[1] <= y_max and j[1] >= y_min]
y_sorted_result = sorted(result, key=lambda x: x[1])
# print(y_sorted_result)
# Plot new set of truncated coordinates
x_val = [x1[0] for x1 in y_sorted_result]
y_val = [x1[1] for x1 in y_sorted_result]
# Create scatter plot
plt.xlim(0, 25)
plt.ylim(0, 25)
#plt.figure(1)
plt.scatter(x_val,y_val,s=80)
plt.savefig('y_overlap_points.png')

# Calculate x intervals
x_intervals = [] # x intervals: ll_x,y to lr_x,y
#x_val = [x1[0] for x1 in y_sorted_result]
#print(x_val)
for zz in range(len(y_sorted_result)):
  # print(zz,y_sorted_result[zz] )
  xi = y_sorted_result[zz][0]
  yi = y_sorted_result[zz][1]
  xi_left = xi - 1
  xi_right = xi + 1
  #print(xi, xi_left, xi_right)
  x_intervals.append([xi_left,xi_right])

  #plt.xlim(0, 25)
  #plt.ylim(0, 25)
  #plt.figure(2)
  #plt.scatter(xi_left,yi)
  #plt.savefig('plot3.png')

#print()
# print("All x intervals, sorted by y_coord =>", sorted(x_intervals))
print()

x_count_list = []
def x_overlaps(x_intervals):
    xes = []
    for xa, xb in x_intervals:
        # print(xa,xb)
        xes.append((xa, -1))
        xes.append((xb, 1))
    xes.sort()
    # print(xes)
    x_result = 0
    xn = 0
    for xa, xs in xes:
        if xs == -1: x_result += xn
        xn -= xs
        # print("y_low => ",xa,"Count => ",xn)
        if xn >= 2 and xs == -1:
            # print("Overlap: x-value start => ", xa)
            x_count_list.append(xn)
            x_count_list.append(xa)

    return x_result

print ("Number of x overlaps => ", x_overlaps(x_intervals))
# print()

# Create pairs from count_list with first value as count and second as y-value
x_my_pairs = list()
while(x_count_list):
    xz = x_count_list.pop(0); xza = x_count_list.pop(0)
    x_my_pairs.append((xz,xza))

#Sort by count or first number in the pair from high count to low count
def sortFirst(val):
    return val[0]

x_my_pairs.sort(key = sortFirst, reverse = True)
int_x_coord = max(x_my_pairs) # y coord in densest area of overlap
# print("List (H => L) by count, y_coord => ",x_my_pairs)
print()
print("Max count and x_value ", int_x_coord)
print()
# Highest degree of overlap based on intervals in y and x direction
print("Highest degree of overlap (x,y) => ",int_x_coord[1], int_y_coord[1])
plt.scatter(int_x_coord[1], int_y_coord[1], s=200, facecolors='none', edgecolors='r')
plt.savefig('greatest_overlap_point.png')

# testing timeit()
print("{} seconds needed for code run".format(timeit.default_timer() - t1))