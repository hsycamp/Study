# Function Practice

# f1
# Write a function f1(list) that will return the number of odd elements in a given list.


def f1(lst):
    count = 0
    for i in lst:
        if i % 2 == 1:
            count += 1
    return count


# f2
# Write a function f2(list) that will print each odd element in a given list


def f2(lst):
    for i in lst:
        if i % 2 == 1:
            print(i)


# f3
# Write a func f3(list) that will return the sum of all odd elements in a given list.


def f3(lst):
    result = 0
    for i in lst:
        if i % 2 == 1:
            result += i
    return result


# f4
# Write a func f4(list) that will return the sum of all the index positions whose corresponding element
# is odd in a given list


def f4(lst):
    result = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            result += i
    return result


# f5
# Write a function f5(list) that will return the same list where each element has been squared


def f5(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] ** 2
    return lst


# f6
# Write a function f6(list) that will return the largest number in a given list.


def f6(lst):
    largest = None
    for i in lst:
        if largest is None:
            largest = i
        elif largest < i:
            largest = i
    return largest


# f7
# Write a function f7(list) that will return the avg of all the numbers in a given list.


def f7(lst):
    result = 0
    for i in lst:
        result += i
    return result / len(lst)


# f8
# Write a function f8(a,b,n) that will print all the numbers divisible by n within the range a and b inclusive.
# Assume n is positive


def f8(a, b, n):
    for i in range(a, b + 1):
        if i % n == 0:
            print(i)


# f9
# Write a function f9(width,height) that will print an ASCII rectangle with the given width and height.

def f9(width, height):
    if width * height > 0:
        for h in range(height):
            print("*" * width)


# f10
# Write a function f10(n) that will print a triangle with the given height n. Assume n is not negative.


def f10(n):
    for i in range(n):
        print("*" * (i + 1))


# f11 Write a function f11(list) that will return True if the list is sorted in descending order and False otherwise.
# Return True for the empty list.


def f11(lst):
    if len(lst) == 0:
        return True
    else:
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                return False
        return True


# f12
# Write a function f12(list) that will return True if the list consists of all negative numbers and False otherwise.
# Return True for the empty list.


def f12(lst):
    if len(lst) == 0:
        return True
    else:
        for i in lst:
            if i >= 0:
                return False
        return True


# f13
# Write a function f13(list,target) that will return the index of the last occurrence of target in the list.
# Assume the list is nonempty and always contains the target


def f13(lst, target):
    idx = None
    for i in range(len(lst)):
        if lst[i] == target:
            idx = i
    return idx


# f14
# Write a function f14(list) that will return the index of the last negative number in the list.
# Assume the list is nonempty and always contains a negative number

def f14(lst):
    idx = None
    for i in range(len(lst)):
        if lst[i] < 0:
            idx = i
    return idx


# f15
# Write a function f15(list) that will return the sum of all the elements at even index positions.


def f15(lst):
    result = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            result += lst[i]
    return result


# f16
# Write a function f16(n) that will print out an upside down triangle


def f16(n):
    for i in range(n, 0, -1):
        print("*" * i)


# f17
# Write a function f17(list) that will print out every other element in a list in reverse order.


def f17(lst):
    for i in range(len(lst)):
        if i % 2 == 1:
            print(lst[-i])


# f18
# Write a function f18(n) that will return n!


def f18(n):
    fact = 1
    for i in range(n, 0, -1):
        fact *= i
    return fact


# f19
# Write a function f19(list) that will print the factorial of each element of a given list


def f19(lst):
    for i in lst:
        fact = 1
        for j in range(i, 0, -1):
            fact *= j
        print(fact)


# f20
# Write a function f20(list) that will print a countdown starting from each element to zero for a given list.


def f20(lst):
    for i in lst:
        for j in range(i, -1, -1):
            print(j, end=' ')
        print()


# f21
# Write a function f21(list1, list2) that will return a new list where each index in the new list corresponds to
# list1[index] + list2[index]. Assume list1 and list2 are the same length .


def f21(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i] + lst2[i])
    return result


# f22
# Write a function f22(n) that will print all the numbers from 1 to n inclusive that is a multiple of 2 or 3.


def f22(n):
    for k in range(1, n+ 1):
        if k % 2 == 0 or k % 3 == 0:
            print(k)


# f23
# Write a function f23(list) that will return the largest value in the list(of all the nested lists inside list).
# Note that list is a nested list. Assume list starts with a nonempty list.

def f23(lst):
    largest = lst[0][0]
    for i in lst:
        for j in i:
            if j > largest:
                largest = j
    return largest


# f24
# Write a function f24(list) that will return the second largest value in the list.
# Assume that the elements of list are all unique and it contains at least 2 elements

def f24(lst):
    if lst[0] > lst[1]:
        largest, s_largest = lst[0], lst[1]
    else:
        largest, s_largest = lst[1], lst[0]
    for i in lst:
        if largest < i:
            largest, s_largest = i, largest
        elif s_largest < i:
            s_largest = i
    return s_largest


# f25
# Write a function f25(n) that will return the leftmost digit in n. Assume n is positive

def f25(n):
    while n > 9:
        n = n // 10
    return n


# f26
# Write a function f25(list) that will print the largest value of each of the nested lists in the given list.
# Note that list is a nested list. Assume each nested list in the given list is not empty.


def f26(lst):
    for i in range(len(lst)):
        largest = lst[i][0]
        for j in lst[i]:
            if largest < j:
                largest = j
        print(largest)
