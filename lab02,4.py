def one_hot_encode(data):
    unique_labels = list(set(data))#list consisting of unique values in data 
    label_dict = {}
    for i in range(len(unique_labels)):
        label_dict[unique_labels[i]] = i#assigning numeric values 

    
    num_labels = len(unique_labels)
    num_data = []

    for i in data:
        encoding = [0] * num_labels#list with all elements 0
        index = label_dict[i]
        encoding[index] = 1#setting that particular label to 1 
        num_data.append(encoding)

    return num_data, label_dict


cat_data = ['car','bike','scooter','car']
num_data, label_dict = one_hot_encode(cat_data)

print("Original Categorical Data:", cat_data)
print("Numerical Data:", num_data)
print("Label Dictionary:", label_dict)
