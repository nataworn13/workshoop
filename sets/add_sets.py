thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# output: {'cherry', 'apple', 'banana', 'orange'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pipneapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# output: {'pipneapple', 'papaya', 'banana', 'mango', 'cherry', 'apple'}
