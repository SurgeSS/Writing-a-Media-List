def M_mod(dest_filename):
    import openpyxl
    wb = openpyxl.load_workbook(dest_filename, data_only=True)
    # Active the initial sheet and setup all the sheets
    ws1 = wb.active
    ws2 = wb["TV"]
    ws3 = wb["background data"]

    # Scrape the background variables from the document
    s1str = ws3['A1'].value
    s2str = ws3['A2'].value

    # Convert the strings to the integer and move the writer to the next cell
    s1v = int(s1str) + 1
    s2v = int(s2str) + 1

    #print("PLEASE WRITE ANSWERS IN ALL CAPS")
    # Ask what sheet needs to be added to
    R1IN = input("What list would you like to add to ANIME or TV? ")
    R1 = R1IN.lower()

    # Setup while loop variable
    n = 2
    if R1 == "anime":
        while n <= s1v:
            s = str(n)
            p = 'A' + s # Setup to write into the next empty cell
            q = 'B' + s
            if ws1[p].value == None: # When an empty cell is reached an addition can be made
                ans1 = input("What is the name of the Anime? ")
                ans2IN = input("Is it completed, inprogress, or queued? ")
                ans2 = ans2IN.lower()
                ws1[p] = ans1
                ws1[q] = ans2
                ws3['A1'] = s1v # Rewrite to background variable to setup for next addition
                print("Anime added successfully")
            else:
                n += 1
    elif R1 == "tv":
        while n <= s2v:
            s = str(n)
            p = 'A' + s # Setup to write into the next empty cell
            q = 'B' + s
            if ws2[p].value == None: # When an empty cell is reached an addition can be made
                an1 = input("What is the name of the TV show? ")
                an2IN = input("Is it completed, inprogress, or queued? ")
                an2 = an2IN.lower()
                ws2[p] = an1
                ws2[q] = an2
                ws3['A2'] = s2v # Rewrite to background variable to setup for next addition
                print("TV show added successfully")
            else:
                n += 1
    else:
        print("That is not a valid list") # Reply to a unnamed sheet

    # Save the changes to the document
    wb.save(filename = dest_filename)
