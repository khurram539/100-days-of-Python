# Day 9 - Beginnner - Directionaires, nesting, and the secret auction program

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."


# Create an empty dictionary
empty_dictionary = {} 

# Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
    

# Grading program

student_scores = {
    "Khurram": 81,
    "Karim": 78,
    "Amberina": 99,
    "Angelina": 74,
    "Aadam": 62,
}    
    
  

student_grades = {}



for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)


# Nesting lists and dictionaries

# Nesting 

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasilia",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota",
    "Peru": "Lima",
    "Venezuela": "Caracas",
}

# Nesting a list in a dictionary
    
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],"total_visits": 12},
    "Germany":  {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],"total_visits": 5},
    "Spain": {"cities_visited": ["Madrid", "Barcelona", "Seville"],"total_visits": 2},
    "United Kingdom": {"cities_visited": ["London", "Birmingham", "Glasgow"],"total_visits": 3},
    "Unite States": {"cities_visited": ["Washington, D.C.", "New York", "Miami"],"total_visits": 5},
    "Canada": {"cities_visited": ["Ottawa", "Montreal", "Toronto"],"total_visits": 2},
    "Mexico": {"cities_visited": ["Mexico City", "Guadalajara", "Cancun"],"total_visits": 3},
    "Brazil": {"cities_visited": ["Brasilia", "Rio de Janeiro", "Sao Paulo"],"total_visits": 2},
    "Argentina": {"cities_visited": ["Buenos Aires", "Cordoba", "Mendoza"],"total_visits": 1},
    "Colombia": {"cities_visited": ["Bogota", "Medellin", "Cartagena"],"total_visits": 1},
    "Peru": {"cities_visited": ["Lima", "Cusco", "Arequipa"],"total_visits": 1},
    "Venezuela": {"cities_visited": ["Caracas", "Maracaibo", "Valencia"],"total_visits": 1},
}
  
    
               
            
   



