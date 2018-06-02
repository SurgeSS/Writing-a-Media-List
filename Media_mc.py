import Media_modifier
import Media_searcher
import Media_updater
import Media_writer
import time

print("THE CAPITALIZED WORDS ARE THE POSSIBLE REPLIES")
time.sleep(2)
OpenFIn = input("Do you have a file already; YES or NO? ")
OpenF = OpenFIn.lower()

if OpenF == "no":
    Media_writer.M_write()
else:
    FileIn = input("What is the name of you list file with out the file extension? ")
    dest_filename = FileIn + ".xlsx"

    ExeIn = input("Would you like to ADD a show, SEARCH based on status, UPDATE a show's status, or WRITE a new list? ")
    exe = ExeIn.lower()

    if exe == "add":
        Media_modifier.M_mod(dest_filename)
    elif exe == "search":
        Media_searcher.M_search(dest_filename)
    elif exe == "update":
        Media_updater.M_up(dest_filename)
    else:
        Media_writer.M_write()
