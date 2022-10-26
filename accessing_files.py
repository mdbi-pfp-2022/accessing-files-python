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
