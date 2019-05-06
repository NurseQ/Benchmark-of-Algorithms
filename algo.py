# import packages to be used for this program
from random import randint
from statistics import mean
import time


# Selection sort algorithm, adapted from https://www.pythoncentral.io/selection-sort-implementation-guide/

def selectionSort(arr):

   for i in range(len(arr)):

      # Find the element with lowest value 
       minPosition = i

       for j in range(i+1, len(arr)):
           if arr[minPosition] > arr[j]:
               minPosition = j
                
       # Swap the element with lowest value at the beginning       
       temp = arr[i]
       arr[i] = arr[minPosition]
       arr[minPosition] = temp

   return arr

# Quick Sort Algorithm
# adapted from https://stackoverflow.com/questions/18262306/quicksort-with-python/27461889#27461889

def qsort(arr):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[0]
        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # join the lists together
        return qsort(less)+equal+qsort(greater)  
    # Note that you want equal ^^^^^ not pivot
    else:  # when you only have one element in your array, just return the array.
        return arr

def bucket_sort(arr):
    largest = max(arr)
    length = len(arr)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(arr[i]/size)
        if j != length:
            buckets[j].append(arr[i])
        else:
            buckets[length - 1].append(arr[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = temp

# Merge Sort Algorithm
# Adapted from https://www.simplifiedpython.net/merge-sort-python/
def merge(left, right):
    result = []  # final result array, that is an empty array
 
#create two indices and initialize with 0
    i,j = 0,0
 
# Till this condition is true, keep on appending elements into resultant array
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            result.append(left[i]) #append ith element of left into resultant array
            i+=1
        else:
            result.append(right[j])  #append jth element of right into resultant array
            j+=1
 
# it is basically specifies that if any element is remaining in the left array from -
# ith to the last index so that it should appended into the resultant array. And similar -
# to the right array.
    result += left[i:]
    result += right[j:]
    return result
 
# Definition for merge sort
# this takes an input list
def mergesort(lst):
    if(len(lst)<= 1): # this means that the list is already sorted.
        return lst
    mid = int(len(lst)/2)
 
# left array will be mergesort applied over the list from starting index 
# till the mid index
    left = mergesort(lst[:mid])
 
# right array will be mergesort applied recursively over the list from mid index
# till the last index 
    right = mergesort(lst[mid:])
 
    return merge(left,right)  # finally return merge over left and right


# Shell Sort Algoritm
# Adapted from https://interactivepython.org/runestone/static/pythonds/SortSearch/TheShellSort.html

def shellSort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(arr,startposition,sublistcount)

     

      sublistcount = sublistcount // 2

# this uses the insertion sort algorithm to sort the gap sequence
def gapInsertionSort(arr,start,gap):
    for i in range(start+gap,len(arr),gap):

        currentvalue = arr[i]
        position = i

        while position>=gap and arr[position-gap]>currentvalue:
            arr[position]=arr[position-gap]
            position = position-gap

        arr[position]=currentvalue


# this function takes one parameter to produce an array of n amount of random numbers 
def random_array(n):
    aray = []
    for i in range(0, n, 1):
        aray.append(randint(0, 10000))
    return aray

num_runs = 10
elements = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]

# this function takes the first element of array elements and passess it to the next for loop where it calculates
# the mean of 10 runs of the function selectionSort. 
def selrunTime():    
    
    times = []    
    for i in elements:
        arr = random_array(i)
        selresults = []
        for r in range(num_runs):
            
            start_time = time.time()

            selectionSort(arr)
            
            end_time = time.time()

            time_elapsed = end_time - start_time
            selresults.append(time_elapsed)
        s = round(mean(selresults),3)
        times.append(s)
    return times

# this function takes the first element of array elements and passess it to the next for loop where it calculates
# the mean of 10 runs of the function qruntime.
def qrunTime():    
    
    qtimes = []    
    for i in elements:
        arr = random_array(i)
        qresults = []
        for r in range(num_runs):
            
            start_time = time.time()

            qsort(arr)
            
            end_time = time.time()

            time_elapsed = end_time - start_time
            qresults.append(time_elapsed)
        q = round(mean(qresults),3)
        qtimes.append(q)
    return qtimes

# this function takes the first element of array elements and passess it to the next for loop where it calculates
# the mean of 10 runs of the function bucketrunTime.
def bucketrunTime():    
    
    btimes = []    
    for i in elements:
        arr = random_array(i)
        bucketresults = []
        for r in range(num_runs):
            
            start_time = time.time()

            qsort(arr)
            
            end_time = time.time()

            time_elapsed = end_time - start_time
            bucketresults.append(time_elapsed)
        b = round(mean(bucketresults),3)
        btimes.append(b)
    return btimes

# this function takes the first element of array elements and passess it to the next for loop where it calculates
# the mean of 10 runs of the function mergerunTime.
def mergerunTime():    
    
    mtimes = []    
    for i in elements:
        arr = random_array(i)
        mergeresults = []
        for r in range(num_runs):
            
            start_time = time.time()

            qsort(arr)
            
            end_time = time.time()

            time_elapsed = end_time - start_time
            mergeresults.append(time_elapsed)
        m = round(mean(mergeresults),3)
        mtimes.append(m)
    return mtimes

# this function takes the first element of array elements and passess it to the next for loop where it calculates
# the mean of 10 runs of the function shellrunTime.
def shellrunTime():    
    
    stimes = []    
    for i in elements:
        arr = random_array(i)
        shellresults = []
        for r in range(num_runs):
            
            start_time = time.time()

            qsort(arr)
            
            end_time = time.time()

            time_elapsed = end_time - start_time
            shellresults.append(time_elapsed)
        s = round(mean(shellresults),3)
        stimes.append(s)
    return stimes
   
# import packages needed    
import numpy as np 
import pandas as pd      

# the main function for the program   
def main():
    # converts the output to an numpy array
    a = np.array(selrunTime())
    b = np.array(qrunTime())
    c = np.array(bucketrunTime())
    d = np.array(mergerunTime())
    e = np.array(shellrunTime())
    # creates a 2D array out of individual arrays
    result = np.column_stack((a,b,c,d,e)).T
    algoList = ["Selection Sort", "Quick Sort", "Bucket Sort", "Merge Sort", "Shell Sort"]
    # uses pandas to format the output (overkill).
    x = pd.DataFrame(result, algoList, elements)
    # send copy to csv file for data wrangling in other software
    #x.to_csv('file1.csv')
    print(x.to_string())


if __name__ =="__main__":
	main()
