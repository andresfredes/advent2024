# Day 3
Iterating in pairs:
```python
it = iter(my_list)
for a, b in zip(it, it):
    print(f"{a}-{b}")

# my_list = [1,2,3,4,5,6]
# prints:
# 1-2
# 3-4
# 5-6
```

# Day 6 - part 2
Checking one location is quite slow, but managable. This gets immediately compounded when both having to check every position, but also getting caught in potentially infinite loops. Breaking out of the inifinite loops was solved by counting the number of times that the guard passed the location. The search space can be narrowed by recognising that many of the locations will never be reached by an initial path. The stoppers only needed to be tested ALONG THE ORIGINAL PATH

