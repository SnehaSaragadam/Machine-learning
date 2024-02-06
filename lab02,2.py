import math

def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):#checking if vectors have same dimension 
        raise ValueError("Vectors must have the same dimension")
    
    squared_distances = [(vector1[i] - vector2[i]) ** 2 for i in range(len(vector1))]#list of square of differences
    sum_of_squares = sum(squared_distances)#sum of squares
    return math.sqrt(sum_of_squares)#square root of sum 

def k_nearest_neighbors(train_data, train_labels, test_instance, k=3):
    if k > len(train_data) or k <= 0:#checks if value of k is positive and greater than the length of the data 
        raise ValueError("Invalid value of k")
    
    distances = []

    for i in range(len(train_data)):
        dist = euclidean_distance(train_data[i], test_instance)
        distances.append((dist, train_labels[i]))

    
    distances.sort(key=get_distance)# Sorting distances based on the first element 

     
    k_nearest = distances[:k]#top k smallest distances

    
    label_counts = {}

    for _, label in k_nearest:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1

    
    most_common_label = max(label_counts, key=label_counts.get)#most occuring label

    return most_common_label


def get_distance(item):
    return item[0]


train_data = [[1, 2], [2, 3], [3, 4], [4, 5]]
train_labels = ['Beliza', 'Beliza', 'BMW', 'BMW']
test_instance = [3, 2.5]
k = 2

predicted_label = k_nearest_neighbors(train_data, train_labels, test_instance, k)

print(f"The predicted label is : {predicted_label}")
