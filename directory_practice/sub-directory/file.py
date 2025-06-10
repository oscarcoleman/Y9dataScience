parent_folder = "directory_practice"
parent_file = "athlete_events.csv"

parent_file_path = parent_folder + "/" + parent_file

file = open(parent_file_path, "r", encoding="utf-8")

contents = file.read()

print(contents)

file.close()