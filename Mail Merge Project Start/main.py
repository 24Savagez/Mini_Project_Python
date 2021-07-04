# TODO: Create a letter using starting_letter.txt
with open(
        r"\Users\chuta\Documents\GitHub\mini_project_python\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    letter = file.read()
    print(letter)

# for each name in invited_names.txt
all_name = []
with open(
        r"\Users\chuta\Documents\GitHub\mini_project_python\Mail Merge Project Start\Input\Names\invited_names.txt") as file:
    names = file.read().split("\n")
    for name in names:
        all_name.append(name)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
for name in all_name:
    with open(
            f"/Users/chuta/Documents/GitHub/mini_project_python/Mail Merge Project Start/Output/ReadyToSend/{name}.txt",
            mode="w") as file:
        finish_letter = letter.replace("[name]", f"{name}")
        file.write(f"{finish_letter}")

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
