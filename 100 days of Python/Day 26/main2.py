
student_dict  =  {
    "name": ["John", "Jane", "Jack", "Jill"],
    "score": [80, 70, 90, 100],
}

# for (key, value) in student_dict.items():
#     print(key, value)
    

import pandas


student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)


#print(student_data_frame)

# Loop  through a data frame


# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

for (index, row) in student_data_frame.iterrows():
    if row.name == "Jack":
        print(row.score)
        
# {new_key:new value for (index, row) in df.iterrows()}

#T0DO 1. Create a dictionary in this format:

{"A": "Alfa", "B": "Bravo"}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
