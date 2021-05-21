import os


for filename in map(lambda filename: filename[:-3], os.listdir("ui/source")):
    os.system(f"pyuic5 ui/source/{filename}.ui -o ui/converted/{filename}.py")
