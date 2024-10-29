            TRANSCRIPT REDACTOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This program will read and process .pdf, .jpg / .jpeg, .png transcript images from a folder
It generates redacted images for each transcipt showing the result of the column edge detector 
    and the un-tilter.
Running all transcripts also creates an All_English_Learners.txt storing english learner
    booleans for every transcript in one central .txt file


-First install all dependencies:
open-cv
numpy
fitz
easyocr
json
nltk
difflib


-Use a terminal to enter commands:

    process single transcript:
    python main.py run <transcript-name.pdf> <Folder name>
        eg. python main.py run 000000001.pdf Transcripts

    process all transcripts:
    python main.py run all <Folder name>
        eg. python main.py run all Transcripts



