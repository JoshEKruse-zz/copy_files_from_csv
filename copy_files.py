import csv
import os
import shutil

csv_file = os.path.join( r"C:\Users\heyjo\Documents\School\Capstone\ESC-50-master\meta\esc50.csv" )
# location of files
existing_path_prefix = r"C:\Users\heyjo\Documents\School\Capstone\ESC-50-master\audio"

# creates new folder in for location of resulting folders w/ files and sets path
try:
    os.mkdir( os.path.join( existing_path_prefix, "audio_folders" ) )
except OSError as error: # if file already exists
    print( error )
new_path_prefix = os.path.join( existing_path_prefix, "audio_folders" )

# open csv
with open( csv_file, 'r' ) as f:
    reader = csv.reader( f)
    for i, row in enumerate( reader ):
        if i == 0:
            pass    # Skip header row
        else:
            # -!!!- Match this with columns from csv file -!!!-
            filename, fold, target, category, esc10, src_file, take = row

            try: 
                os.mkdir( os.path.join( new_path_prefix, category ) ) 
            except OSError as error: # if file already exists
                print( error )

            # copy files into new folders
            new_filedir = os.path.join( new_path_prefix, category )
            existing_filedir = os.path.join( existing_path_prefix, filename )
            shutil.copy( existing_filedir, new_filedir )
            
