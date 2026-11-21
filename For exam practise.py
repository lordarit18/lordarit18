#Code here
basket=['apple', 'guava', 'cherry', 'banana']
my_fruits=['apple', 'kiwi', 'grapes', 'banana']

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])