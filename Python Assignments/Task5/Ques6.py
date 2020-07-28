# Write a program in Python using generators to reverse the string. Input String = “Consultadd Training”

def reverse_string(sample):
    yield sample[::-1]

sample_string = 'Consult Training'

sample_string = reverse_string(sample_string)

print(sample_string.__next__())