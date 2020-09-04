words = {
    'apple': 'is a fruit',
    'book': 'has words in it'
}
# to access apple, runtime is: O(1)

words = ["apple", "book", "cat", "dog", "egypt", "france"]
# to access egypt runtime is: O(n)


# Wat if we had a magic function
# takes a word ----> return the index for where that word is located in some array
# book -> 1
# egypt -> 4
# fake_word -> None
# this function is 0(1)

# Hash FUNCTIONS
# Any string input ---> specific number (within some range)
# MOST IMPORTANT:
# This function must be deterministic
# Same input will always return the same output

def my_hash(s, limit):
    # take every character in teh string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()
    # print(string_utf)

    total = 0
    for char in string_utf:
        # print(char)
        total += char
        total &= 0xffffffff  # limit total to 32 bits
    return total % limit

# my_hash('Hello')
# print(my_hash('Hello'))
# print(my_hash('World'))

# Collision
# print(my_hash('card', 8))
# print(my_hash('apple', 8))

# modulo
print(f'card hashes to {my_hash("card", 8) % 8}')

print(f'card hashes to {my_hash("apple", 8) % 8}')

# create an array with 8 none values. Prefer it be a power of 2 etc.. 1,2,4,8,16,32,64,128,512,1024,2048,4096,8192,16384,
hash_table = [None] * 8

hash_table_python = dict() # same as going {}

# ADD items to hash_table using the my_hash function
# Hash the key to get an index
# Store the value at the generated Index
index = my_hash('Hello', len(hash_table))
# print('index:',index)
hash_table[index] = 'Value for Hello'

index = my_hash('World', len(hash_table))
print('index:', index)
hash_table[index] = 'Value for World'


# Retrive some items from hash_table
# Lets retrieve the value for 'Hello'
index = my_hash('Hello', len(hash_table))
print(hash_table[index])
print('hash_table:', hash_table)
