import math

def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):#checking if vectors have same dimension 
        raise ValueError("Vectors must have the same dimension")
    
    squared_distances = [(vector1[i] - vector2[i]) ** 2 for i in range(len(vector1))]#list of square of differences
    sum_of_squares = sum(squared_distances)#sum of squares
    return math.sqrt(sum_of_squares)#square root of sum 

def manhattan_distance(vector1, vector2):
    if len(vector1) != len(vector2):#checking if vectors have same dimension 
        raise ValueError("Vectors must have the same dimension")
    
    absolute_diff = [abs(vector1[i] - vector2[i]) for i in range(len(vector1))]#list of differences
    return sum(absolute_diff)#sum of the differences 


vector1 = eval(input("enter vector A"))
vector2 = eval(input("enter vector B"))

eucdis = euclidean_distance(vector1, vector2)
mandis = manhattan_distance(vector1, vector2)

print(f"Euclidean Distance: {eucdis}")
print(f"Manhattan Distance: {mandis}")
