with open('./Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    name_=names.readlines()
with open('./Mail Merge Project Start/Input/Letters/starting_letter.txt') as letters:
    letter=letters.read()
    for name in name_:
        stripped_name=name.strip()
        updated_letter = letter.replace('[name]', stripped_name)
        with open(f'./Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt',mode='w') as file:
            file.write(updated_letter)

