import os 




# get all the directories in chords/
chords = os.listdir('chords')

# for each directory in chords/
for chord in chords:
    # get all the files in chords/xxx/
    files = os.listdir('chords/' + chord)
    # for each file in chords/xxx/
    for file in files:
        # move the file from chords/xxx/ to melody/xxx/
        os.rename('chords/' + chord + '/' + file, 'melody/' + chord + '/' + file)




