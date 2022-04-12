from main import get_data, scrape_the_web, add_to_database, see_notes
while True:
    print("Hello, Welcome to the Definition extractor app")
    print("Enter 1 to scrape a defintion")
    print("Enter 2 to see a defintion")
    print("Enter 3 to exit")
    try:
        choice = int(input("Enter your choice:"))
        if choice == 1:
            scrape_the_web(str(input("What would you like to scrape:")))
            print("data added to database")
        elif choice == 2:
            see_notes(str(input("Which definition to search in database:")))
            print("database searched")
        elif choice == 3:
            exit()
        else:
            print("invalid option")

    except ValueError:
        print("Please choose either 1 or 2")
    except Exception as e:
        print(e)




