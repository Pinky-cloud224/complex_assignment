#Assignment-1:
sample_string="google.com"

character_frequency={}

for i in sample_string:
    if i in character_frequency:
        character_frequency [i] +=1
    else:
        character_frequency [i] =1

print(character_frequency)

