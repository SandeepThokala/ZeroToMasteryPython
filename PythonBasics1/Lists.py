#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1]) #'b'
print(new_list[-2]) #'b'
print(new_list[1:3]) #
new_list[0] = 'z'
print(new_list) #['z', 'b', 'c']

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list) #['z', 2, 3]
print(bonus) #[1, 2, 3, 5]

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.remove('Banana')

# 2. Remove "Blueberries" from the list.
basket.remove('Blueberries')

# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')

# 4. Add "Apples" at the beginning of the list
basket.insert( 1, 'Apples')

# 5. Count how many apples in the basket
print(basket.count('Apples'))

# 6. empty the basket
basket.clear()

print(basket)