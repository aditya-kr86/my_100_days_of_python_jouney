import os
# from docx import Document

# Change the current working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Verify the current working directory
# print("Current working directory:", os.getcwd())

# Open the file using a relative path
with open("Input/Names/invited_names.txt") as file:
    contents = file.read()
    invited_names = contents.split('\n')

# print(invited_names)

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

# Directory where the invitations will be saved
output_directory = "Output"  # Replace with your desired directory

# Ensure the directory exists
os.makedirs(output_directory, exist_ok=True)

################ TO SAVE IN .txt Format
for inv_name in invited_names:
    invitation_message = letter.replace('[name]',inv_name)

    filename = f"{inv_name}_invitation.txt"
    filepath = os.path.join(output_directory, filename)
    with open(filepath, 'w') as file:
        # file.write(f"Birthday Invitation\n\n{invitation_message}")
        file.write(invitation_message)
    print(f"Invitation for {inv_name} saved as {filepath}")
