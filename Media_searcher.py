def M_search(dest_filename):
    import openpyxl
    wb = openpyxl.load_workbook(dest_filename, data_only=True)
    ws1 = wb.active
    ws2 = wb["TV"]
    ws3 = wb["background data"]

    # Scrape the background variables from the document
    s1str = ws3['A1'].value
    s2str = ws3['A2'].value

    # Convert the strings to the integer and move the writer to the next cell
    s1v = int(s1str)
    s2v = int(s2str)

    #print("PLEASE WRITE ANSWERS IN ALL CAPS")
    # Ask what sheet needs to be updated
    R1IN = input("What list would you like to check, ANIME or TV? ")
    R1 = R1IN.lower()

    # Setup while loop variable
    back_val = 2
    if R1 == "anime":
        R2IN = input("What status list do you want to check: completed, inprogress, or queued? ")
        R2 = R2IN.lower()
        while back_val <= s1v:
            s = str(back_val)
            p = 'A' + s # Setup to check the specified anime
            q = 'B' + s
            if ws1[q].value == R2:
                print(ws1[p].value)
                back_val += 1
            else:
                back_val += 1
    elif R1 == "tv":
        R2IN = input("What status list do you want to check: completed, inprogress, or queued? ")
        R2 = R2IN.lower()
        while back_val <= s2v:
            s = str(back_val)
            p = 'A' + s # Setup to check the specified anime
            q = 'B' + s
            if ws2[q].value == R2:
                print(ws2[p].value)
                back_val += 1
            else:
                back_val += 1
    else:
        print("That is not a valid list")

    # Save the changes to the document
    wb.save(filename = dest_filename)
