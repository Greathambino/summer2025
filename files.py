import os
# r = read (error if it doesn't exist)
# a = append creates the file if it doesn't exist
# w = write (overwrites existing content)
# x = exclusive creation (fails if file exists)

# very similar to crud, create, read, update, delete

f = open('names.txt') # can specify if it's a binary or text file too! Defaults to read text
# same as f = open('names.txt', 'rt')

#print(f.read())  # read the entire file
#print(f.read(4))  # read the first 4 characters

# print(f.readline())  # read the first line (ends with new line)
# print(f.readline())  # read the second line

# for line in f:
#     print(line) # basically uses f.readline() until the end

f.close()  # close the file when done

try:
    f = open('name_list.txt')
    print(f.read())
except:
    print('File not found!')
finally:
    f.close()  # ensure the file is closed even if an error occurs

# Append time
f = open("names.txt", "a")  # open for appending
f.write("Neil\n")
f.close()

f = open("names.txt", "r")  # open for reading
print('\n'+f.read())
f.close()

# Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates file if it does not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file already exists

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file does not exist, so it cannot be deleted.")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)

