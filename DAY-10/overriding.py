# class animal:
#     def speak(self):
#         return "animal makes a sound"
# class dog(animal):
#     def speak(self):
#         return "boof"
# class cat(animal):
#     def speak(self):
#         return "meow"
# class cow(animal):
#     pass
# d=dog()
# c=cat()
# c1=cow()
# print(d.speak())
# print(c.speak())
# print(c1.speak())
# Define the list and group size
# hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
# groupSize = 3

# # Generate combinations of consecutive elements
# consecutive_combinations = [hand[i:i + groupSize] for i in range(len(hand) - groupSize + 1)]

# # Print the combinations
# for combo in consecutive_combinations:
#     print(combo)
# a = [1, 1, 1, 2, 2, 3]

# for element in a:
#     count = a.count(element)
#     if count >= 3:
#         print(element,element, end=' ')
#     elif count == 2:
#         print(element, element, end=' ')
#     elif count == 1:
#         print(element, end=' ')
# def remove_duplicates(lst):
#     seen = set()
#     for x in lst:
#         if x not in seen:
#             seen.add(x)
#             yield x

# a = [1, 1, 1, 2, 2, 3]
# output = list(remove_duplicates(a))
# print(output)

def prime(m):
    if m <= 1:
        return False
    if m == 2:  # Handling case when n is 2
        return True
    for i in range(2, m):  # Changed range from 3 to m to check prime correctly
        if m % i == 0:
            return False
    return True
def check(n):
    f = []
    for i in range(1, n + 1):
        if prime(i):
            f.append(i)
    p = []
    for i in range(len(f) - 1):
        if f[i] + f[i + 1] == n or f[i] ** 2 == n:
            p.append([f[i], f[i + 1]])
    return p
n=int(input())
print(check(n))


