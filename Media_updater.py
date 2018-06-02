def M_up(dest_filename):
    import openpyxl
    wb = openpyxl.load_workbook(dest_filename, data_only=True)
    ws1 = wb.active
    ws2 = wb["TV"]
    ws3 = wb["background data"]

    s1str = ws3['A1'].value
    s2str = ws3['A2'].value

    s1v = int(s1str)
    s2v = int(s2str)

    #print("PLEASE WRITE ANSWERS IN ALL CAPS")
    R1IN = input("What list would you like to check, Anime or TV? ")
    R1 = R1IN.lower()

    back_val = 2
    if R1 == "anime":
        R2 = input("What show would you like to check? ")
        while back_val <= s1v:
            s = str(back_val)
            p = 'A' + s
            q = 'B' + s
            if ws1[p].value == R2:
                print("The current status of this show is: ", ws1[q].value)
                R3IN = input("Do you want to update this status? ")
                R3 = R3IN.lower()
                if R3 == "yes":
                    ans1 = input("What is the new status of this show? ")
                    ws1[q] = ans1
                    print("Update Successful")
                    back_val = s1v + 1
                else:
                    print("Show status not updated")
                    back_val = s1v + 1
            else:
                back_val += 1
    elif R1 == "tv":
        R2 = input("What show would you like to check? ")
        while back_val <= s2v:
            s = str(back_val)
            p = 'A' + s
            q = 'B' + s
            if ws2[p].value == R2:
                print("The current status of this show is: ", ws2[q].value)
                R3IN = input("Do you want to update this status? ")
                R3 = R3IN.lower()
                if R3 == "yes":
                    an1 = input("What is the new status of this show? ")
                    ws2[q] = an1
                    print("Update Successful")
                    back_val = s2v + 1
                else:
                    print("Show status not updated")
                    back_val = s2v + 1
            else:
                back_val += 1
    else:
        print("That is not a valid list")

    wb.save(filename = dest_filename)
