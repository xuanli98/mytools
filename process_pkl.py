import pickle

# read pkl file

with open("results/net-Xception_traindb-ff-c23-720-140-140_face-scale_size-64_seed-41_bestval/ff-c23-720-140-140_test.pkl", "rb") as ffpp_res:
    ffpp_data = pickle.load(ffpp_res)
print(ffpp_data)
for num, key in enumerate(ffpp_data):
    print(key,ffpp_data[key][0])