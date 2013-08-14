# PhoneBook
# Developed with Python  2.7.5
# Tested with Windows 7

import csv

phoneBookDictionary = {}
helpFile = "phonebookhelp.txt"
phoneBookRoot = "phonebook.csv"
#phoneBookRoot_tmp = "phonebook_tmp.csv"
headers = []

def phoneBookHelp():

    """
    Reads PhoneBooks Help from phonebookhelp.txt 
    """
    print "\n############################"
    print "###         Help         ###"    
    print "############################\n"    

    reader = open(helpFile, "r")
    print reader.read()
    reader.close()
    showMainMenu()

def showMainMenu():

    """
    This function is the Main Menu of the PhoneBook. Each Option is a number.
    """
    
    print "\n############################"
    print "###       Main Menu      ###"    
    print "############################\n"
    print "Option 1. Search PhoneBook"
    print "Option 2. Add new Entry"
    print "Option 3. Delete Entry"
    print "Option 4. Show PhoneBook"    
    print "Option 5. Read PhoneBook from file"
    print "Option 6. Save PhoneBook to file"
    print "Option 7. PhoneBook Help"    
    print "Option 8. Exit"    

    option = raw_input("Enter an Option [1-7] -> ")
    
    if option == "1":
        searchPhoneBook()
    elif option == "2":
        addNewEntry()
    elif option == "3":
        deleteEntry()
    elif option == "4":
        showPhoneBook()
    elif option == "7":
        phoneBookHelp()
    elif option == "5":
        readFromFile()
    elif option == "6":
        saveToFile()
    elif option == "8":
        exitPhoneBook()         
        
def readFromFile():

    """
    Initializing the PhoneBook within a Dictionary data structure. Reads PhoneBookDate.xls            
    """

    print "\n############################"
    print "###   Reading from file  ###"    
    print "############################\n"
    
    # read phonebook.csv
    
    with open(phoneBookRoot, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')

        # avoid headers info
        h = reader.next()
        for n in h:
            headers.append(n)

        # create a auxiliar list with the phonebook data
        phoneBookList_aux = []
        i = 0
        for row in reader:
            phoneBookList_aux.append(row)            
            i += 1

                                                      
        # reorganize the list adding a list inside for phonetypes and phonenumbers                
        phoneBookList = []
        j = 0
        
        for row in phoneBookList_aux:

            # first element
            if j == 0: 
                phoneBookList.append(row)
                phoneBookList[j][2] = [row[2]]
                phoneBookList[j][3] = [row[3]]
                j += 1

            # same Id    
            elif row[0] == phoneBookList[j-1][0]:                
                if type(phoneBookList[j-1][2]) == type("string"):
                    phoneBookList[j-1][2] = [phoneBookList[j-1][2],row[2]]
                    phoneBookList[j-1][3] = [phoneBookList[j-1][3],row[3]]
                    
                elif type(phoneBookList[j-1][2]) == type([0,1]):
                    phoneBookList[j-1][2].append(row[2])
                    phoneBookList[j-1][3].append(row[3])
                    
                else:
                    print type(phoneBookList[j-1][2])
                    print type(phoneBookList[j-1][3])
                    print "something  wrong"

            # new Id    
            else:
                phoneBookList.append(row)
                phoneBookList[j][2] = [row[2]]
                phoneBookList[j][3] = [row[3]]
                j += 1

        # phoneBookList_aux is no longer needed
        del phoneBookList_aux
        
        # transform  phoneBookList into a Dictionary
        
        for row in phoneBookList:
            phoneBookDictionary[row[0]] = row[1:]

        # phoneBookList is no longer needed
        del phoneBookList
        
        print "\n-->> "+phoneBookRoot + " has been readed.\n"
    
        

    # back to menu
    showMainMenu()

def showPhoneBook():
    """
    Print the phoneBookDictionary.
    """

    print "\n############################"
    print "###   Showing PhoneBook  ###"    
    print "############################\n"
    
    # Checking if phoneBook was already readed from file
    if phoneBookDictionary == {}:
        print "\n-->> Before showing you need to read a PhoneBook, with option 6 of main menu.\n"
    else:
        # print phoneBookDictionary
        for row in phoneBookDictionary:
            print "Id: "+row
            print "   Name: "+phoneBookDictionary[row][0]
            print "   Phone(s): "            
            n = 0
            while n < len(phoneBookDictionary[row][1]):
                print "     "+phoneBookDictionary[row][1][n]+"> "+phoneBookDictionary[row][2][n]
                n += 1
                
            print "   Address: "+phoneBookDictionary[row][3]
            print "   Average Salary: "+phoneBookDictionary[row][4]
        

    showMainMenu()

def addNewEntry():
    """
    Adds a new entry to phoneBookDictionary
    """

    print "\n############################"
    print "###   Adding new Entry    ###"    
    print "############################\n"

    # Checking if phoneBook was already readed from file
    if phoneBookDictionary == {}:
        print "\n-->> Before adding a new entry you need to read a PhoneBook, with option 6 of main menu.\n"
    else:
        if inputData():
            print "\n-->> Phone Book has been updated.\n"
        else:
            print "\n-->> Something went wrong\n"
        
    showMainMenu()

def inputData():
    """
    Input Data from keyboard
    """
    
    ids = raw_input("Input Id -> ")
    name = raw_input("Input Name -> ")
    phonetype = raw_input("Input Phone Type -> ")
    phonenumber = raw_input("Input Phone Number -> ")
    address = raw_input("Input Address -> ")
    avgsalary = raw_input("Input Average Salary -> ")

    phoneBookDictionary[ids] = [name,[phonetype],[phonenumber],address,avgsalary]

    return True

def deleteEntry():
    """
    Delete a entry to phoneBookDictionary
    """

    print "\n############################"
    print "###    Deleting Entry ###"    
    print "############################\n"

    # Checking if phoneBook was already readed from file
    if phoneBookDictionary == {}:
        print "\n-->> Before deleting an entry you need to read a PhoneBook, with option 6 of main menu.\n"
    else:
        if deleteData():
            print "\n-->> Phone Book has been updated.\n"
        else:
            print "\n-->> Something went wrong\n"
        
    showMainMenu()

def deleteData():
    """
    Input Data from keyboard
    """
    
    ids = raw_input("Id to delete -> ")
    if phoneBookDictionary.has_key(ids):
        del phoneBookDictionary[ids]
        return True
    else:
        return False

def searchPhoneBook():
    """
    Search an Entry into phoneBookDictionary
    """    

    print "\n############################"
    print "###  Searching Entry     ###"    
    print "############################\n"

    # Checking if phoneBook was already readed from file
    if phoneBookDictionary == {}:
        print "\n-->> Before looking for an entry you need to read a PhoneBook, with option 6 of main menu.\n"
    else:
        ids = raw_input("Id to look for -> ")
        if phoneBookDictionary.has_key(ids):
            print "Id: "+str(ids)
            print "   Name: "+phoneBookDictionary[ids][0]
            print "   Phone(s): "            
            n = 0
            while n < len(phoneBookDictionary[ids][1]):
                print "     "+phoneBookDictionary[ids][1][n]+"> "+phoneBookDictionary[ids][2][n]
                n += 1
                
            print "   Address: "+phoneBookDictionary[ids][3]
            print "   Average Salary: "+phoneBookDictionary[ids][4]
        else:
            print "\n-->> Noy key value found\n"
        
    showMainMenu()

def saveToFile():
    """
    Save phoneBookDictionary into a file
    """    

    print "\n############################"
    print "###    Saving File        ###"    
    print "############################\n"

    # Checking if phoneBook was already readed from file
    if phoneBookDictionary == {}:
        print "\n-->> Before save to file you need to read a PhoneBook, with option 6 of main menu.\n"
    elif areyousure():

        # Writing phoneBook to file
        with open(phoneBookRoot, 'wb') as csvfile:
            writer = csv.writer(csvfile)

            # Writing headers            
            writer.writerow(headers)            

            # Writing each row 
            for row in phoneBookDictionary:
                element = phoneBookDictionary[row]
                i = 0
                for n in element[1]:
                    writer.writerow([row,element[0],element[1][i],element[2][i],element[3],element[4]])
                    i+=1

            print "\n-->> File "+phoneBookRoot+" updated\n"
        
    showMainMenu()

def areyousure():
    """
    Ask for confirmation of overriding de phonebook csv file
    """

    answer = 'xxx'
    while answer != 'n' and answer != 'y':
        answer = raw_input("\n-->> You are about to override the "+phoneBookRoot+" file, are you sure? (y/n) -> \n").lower()

    if answer == 'n':
        return False
    elif answer == 'y':
        return True
    else:
        print "\n-->> Something went wrong\n"
    
def exitPhoneBook():
    raise SystemExit

# main
showMainMenu()
