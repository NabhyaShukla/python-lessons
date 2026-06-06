fruits= ["apple", "banana", "grapes", "kiwi"]
print(fruits)

# enumerate() = adds a counter to an iterable and returns it in a form of enumerate object
for i, fruit in enumerate(fruits, start=1): # start=1 is used to start the counter from 1 instead of 0
    print(f"{i} : {fruit}")

# explicit args and kwargs
def test(*args):
    return sum(args)

print(test(1,2,3,179))