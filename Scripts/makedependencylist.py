import os
import glob

OUT_DIR = "../Notes"

filenames = glob.glob("*.py")

print(filenames)
    
internal = [os.path.splitext(fn)[0] for fn in filenames]

print("Internal Files:", internal)

importedSet = set()

for fn in filenames:
    with open(fn, "rt") as f:
        for line in f.readlines():
            s = line.split()
            if ((len(s) > 0 ) and 
                ((s[0] == "import") or (s[0] == "from"))):
                imported = s[1]
                if '.' in imported:
                    dotSplit = imported.split('.')
                    imported = dotSplit[0]
                print ("Imported:", imported)
                importedSet.add(imported)

print (importedSet)

python_std = [
    "__future__",
    "argparse",
    "datetime",
    "glob",
    "logging",
    "os",
    "random",
    "string",
    "sys",
    "time",
]

external = []

for i in importedSet:
    if i in internal:
        # do nothing
        pass
    elif i in python_std:
        # do nothng
        pass
    else:
        external.append(i)

external.sort()

with open("../Notes/dependencies.txt", "wt") as f:
    for x in external:
        f.write(x)
        f.write("\n")
