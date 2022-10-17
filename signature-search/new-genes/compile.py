import os

gene_list = []
for root, dirs, files in os.walk(r"C:/Users/neelj/Documents/HIVE/FAB Feature Selecion/new-genes"):
    for file in files:
        if file.endswith(".txt"):
            filename = os.path.join(root, file)
            if "compile" not in filename:
                print(filename)
                f = open(filename, "r")
                gene_list += f.read().split("\n")
                f.close()

with open("new-compile.txt", "w") as f:
    f.write(",".join(gene_list))

f.close()


