def label_encode(data):
    unique_data = list(set(data))#list consisting of unique values in data 
    label_dict = {}
    num_data = []

    for i in unique_data:
        label_dict[i] = len(label_dict)#assigning numeric values 

    for j in data:
        num_data.append(label_dict[j])#list storing numeric representation of the data  

    return num_data, label_dict


cat_data = ['car','bike','scooter','car']

num_data, label_dict = label_encode(cat_data)

print("Original Categorical Data:", cat_data)
print("Numerical Data:", num_data)
print("Label Dictionary:", label_dict)
