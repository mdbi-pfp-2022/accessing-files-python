#%%

file = open("hello.txt")

for line in file:
    print(line)

file.close()

#%%

with open("hello.txt") as file:
    for line in file:
        print(line)


# %%

with open("hello.txt", "w") as file:
    file.write("This was written from Python!")

# %%


with open("mdbi.txt", "w") as file:
    contents = "Hello y'all, how's it going? today's Alexia's birthday"
    file.write(contents)

#%%

with open("mdbi.txt") as file:
    for line in file:
        print(line)
# %%


with open("data/data.csv") as file:
    for line in file:
        print(line)
# %%

import csv

with open("data/data.csv") as file:
    reader = csv.reader(file)
    count_females = 0
    for line in reader:
        if line[4] == "Female":
            count_females = count_females + 1
            # count_females += 1

    print(count_females)
# %%

# %%

import json

with open("data/data.json") as file:
    data = json.load(file)

    count = 0
    sum = 0
    for person in data:
        sum = sum + person["age"]
        count = count + 1

    print(sum / count)
# %%
