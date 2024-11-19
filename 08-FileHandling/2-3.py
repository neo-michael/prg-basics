###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as source_file:
   content = source_file.read()

with open(target_file, 'w') as destination_file:
    destination_file.write(content)

