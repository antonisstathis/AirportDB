# -*- coding: utf-8 -*-

import mysql.connector


def connect_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="06051995antonis",
        database="airport_app"
    )

    return mydb


def printDirections():

    directions = """
        Enter one of the following options:

        search flights          insert flight           update flight           delete flights
        search company          insert company          update company          delete company
        search controller       insert controller       update controller       delete controller
        search engineer         insert engineer         update engineer         delete engineer
        search freighter        insert freighter        update freighter        delete freighter
        search plane            insert plane            update plane            delete plane
        search load             insert load                                     delete load
        search service          insert service                                  delete service

        check gates <minutes>
        check airstrip <minutes>

        exit

        """

    print(directions)



def chooseFunction(mydb):

    x = input("[AirportDB ~]$ ")
    while (x != "exit"):

        if x == "search flights":
            searchFlights(mydb)

        elif x == "search company":
            searchCompany(mydb)

        elif x == "search controller":
            searchController(mydb)

        elif x == "search engineer":
            searchEngineer(mydb)

        elif x == "search freighter":
            searchFreighter(mydb)

        elif x == "search load":
            searchLoad(mydb)

        elif x == "search plane":
            searchPlane(mydb)

        elif x == "search service":
            searchService(mydb)

        elif x == "delete flights":
            deleteFlights(mydb)

        elif x == "delete company":
            deleteCompany(mydb)

        elif x == "delete controller":
            deleteController(mydb)

        elif x == "delete engineer":
            deleteEngineer(mydb)

        elif x == "delete freighter":
            deleteFreighter(mydb)

        elif x == "delete load":
            deleteLoad(mydb)

        elif x == "delete plane":
            deletePlane(mydb)

        elif x == "delete service":
            deleteService(mydb)

        elif x == "insert flight":
            insertFlight(mydb)

        elif x == "insert company":
            insertCompany(mydb)

        elif x == "insert controller":
            insertController(mydb)

        elif x == "insert engineer":
            insertEngineer(mydb)

        elif x == "insert frighter":
            insertFreighter(mydb)

        elif x == "insert load":
            insertLoad(mydb)

        elif x == "insert plane":
            insertPlane(mydb)

        elif x == "insert service":
            insertService(mydb)

        elif x == "update flight":
            updateFlight(mydb)

        elif x == "update company":
            updateCompany(mydb)

        elif x == "update controller":
            updateController(mydb)

        elif x == "update engineer":
            updateEngineer(mydb)

        elif x == "update freighter":
            updateFreighter(mydb)

        elif x == "update plane":
            updatePlane(mydb)

        elif x == "check gates":
            checkGates(mydb, 30)

        elif x == "check airstrip":
            checkAirstrip(mydb, 30)

        else:
            analysis = x.split()
            if len(analysis) == 3:
                if analysis[0] == 'check':
                    check_minutes = 30
                    try:
                        check_minutes = int(analysis[2])
                    except:
                        print("Invalid Input")

                    if analysis[1] == 'gates':
                        checkGates(mydb, check_minutes)
                    if analysis[1] == 'airstrip':
                        checkAirstrip(mydb, check_minutes)

        x = input("[AirportDB ~]$ ")


def ask_data(data):
    message = "Enter " + data
    print(message)
    x = input()
    return x


def searchFlights(mydb):
    directions = """
    print all
    flight id,
    plane id,
    departure,
    destination,
    departure time,
    arrival time,
    real departure time,
    controller,
    status,
    gate id,
    airstrip id,
    parking spot id,
    parking start,
    parking end
    search dates
    """

    keys = ["flight id: ", "plane id: ", "departure: ", "destination: ", "departure time: ", "arrival time: ",
            "real departure time: ", "controller: ", "status: ", "gate id: ", "airstrip id: ", "parking spot id: ",
            "parking start date: ", "parking end date: "]

    keys_dates = ["flight id: ", "plane id: ", "departure: ", "destination: ", "departure time: ", "arrival time: ",
                  "gate id: "]

    message = "Enter one of the above options to select flights:"

    print(directions)
    print(message)
    option = input()

    if option == "departure time" or option == "arrival time" or option == "parking start" or option == "parking end":
        print("Enter datetime data as follows: 2020-03-23 18:00:00")

    if option == "search dates":
        print("Enter date with this format: 2021-03-20")
        start_date = input("Enter start date to search:")
        last_date = input("Enter last date to search:")
        start_datetime = start_date + " 00:00:00"
        last_datetime = last_date + " 23:59:59"
    if option == "print all":

        try:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM flight;")

            i=1
            for row in mycursor:
                print("Flight " + str(i) + " information:")
                print("------------------")
                i=i+1
                for counter in range(len(row)):
                        result = keys[counter] + str(row[counter])
                        print(result)
                print("\n\n")

        except:
            print("Invalid data entered. Try again.")
        return

    else:
        message1 = "Enter " + option + " to search for flights:"
        print(message1)
        data = input()

    queries = {
        "flight id": "SELECT * FROM flight WHERE FlightID = %s;",
        "plane id": "SELECT * FROM flight WHERE PlaneID = %s;",
        "departure": "SELECT * FROM flight WHERE Departure = %s;",
        "destination": "SELECT * FROM flight WHERE Destination = %s;",
        "departure time": "SELECT * FROM flight WHERE DepartTime = %s;",
        "arrival time": "SELECT * FROM flight WHERE ArrivalTime = %s;",
        "real departure time": "SELECT * FROM flight WHERE RealDepartTime = %s;",
        "controller": "SELECT * FROM flight WHERE Controller = %s;",
        "status": "SELECT * FROM flight WHERE Status = %s;",
        "gate id": "SELECT * FROM flight WHERE GateID = %s;",
        "airstrip id": "SELECT * FROM flight WHERE AirstripID = %s;",
        "parking spot id": "SELECT * FROM flight WHERE ParkingSpotID = %s;",
        "parking start": "SELECT * FROM flight WHERE ParkingStart = %s;",
        "parking end": "SELECT * FROM flight WHERE ParkingEnd = %s;",
        "search dates": "SELECT FlightID,PlaneID,Departure,Destination,DepartTime,ArrivalTime,GateID FROM flight WHERE ((DepartTime BETWEEN %s AND %s AND Departure='UPA') OR (ArrivalTime BETWEEN %s AND %s AND Destination='UPA'));"
    }

    if option == "search dates":

        mytuple = (start_datetime, last_datetime, start_datetime, last_datetime)

        try:
            mycursor = mydb.cursor()
            mycursor.execute(queries[option], mytuple)

            i = 1
            for row in mycursor:
                print("Flight " + str(i) + " information:")
                print("------------------")
                i = i + 1
                for counter in range(len(row)):
                    result = keys_dates[counter] + str(row[counter])
                    print(result)
                print("\n\n")

        except:
            print("Invalid data entered. Try again.")


    else:
        try:
            mycursor = mydb.cursor()
            mycursor.execute(queries[option], tuple([data]))

            i=1
            for row in mycursor:
                print("Flight " + str(i) + " information:")
                print("------------------")
                i=i+1
                for counter in range(len(row)):
                        result = keys[counter] + str(row[counter])
                        print(result)
                print("\n\n")

        except:
            print("Invalid data entered. Try again.")


def searchCompany(mydb):
    directions = """
    name,
    phone    
    """

    message = "Enter one of the above options to select a comapny:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to search for a company:"
    print(message1)
    data = input()

    queries = {
        "name": "SELECT * FROM company WHERE Name = %s;",
        "phone": "SELECT * FROM company WHERE Phone = %s;"
    }

    keys = ["name: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print("Company " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def searchController(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    message = "Enter one of the above options to select a controller:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to search for a controller:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM controller WHERE ID = %s;",
        "name": "SELECT * FROM controller WHERE Name = %s;",
        "surname": "SELECT * FROM controller WHERE Surname = %s;",
        "phone": "SELECT * FROM controller WHERE Phone = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print("Controller " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def searchEngineer(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    message = "Enter one of the above options to select an engineer:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to search for an engineer:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM engineer WHERE EngineerID = %s;",
        "name": "SELECT * FROM engineer WHERE Name = %s;",
        "surname": "SELECT * FROM engineer WHERE Surname = %s;",
        "phone": "SELECT * FROM engineer WHERE Phone = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print("Engineer " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def searchFreighter(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    message = "Enter one of the above options to select a freighter:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to search for a freighter:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM freighter WHERE FreighterID = %s;",
        "name": "SELECT * FROM freighter WHERE Name = %s;",
        "surname": "SELECT * FROM freighter WHERE Surname = %s;",
        "phone": "SELECT * FROM freighter WHERE Phone = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print("Freighter " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def searchLoad(mydb):
    directions = """
    flight id,
    freighter id   
    """

    message = "Enter one of the above options to select a load:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to search for a load:"
    print(message1)
    data = input()

    queries = {
        "flight id": "SELECT * FROM loads WHERE FlightID = %s;",
        "freighter id": "SELECT * FROM loads WHERE FreighterID = %s;"
    }

    keys = ["id: ", "name: ", "surname: ", "phone: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print("Load " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def searchPlane(mydb):
    directions = """
    id,
    owner,
    maker,
    model   
    """

    message = "Enter one of the above options to select a plane:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to search for a plane:"
    print(message1)
    data = input()

    queries = {
        "id": "SELECT * FROM plane WHERE ID = %s;",
        "owner": "SELECT * FROM plane WHERE Owner = %s;",
        "maker": "SELECT * FROM plane WHERE Maker = %s;",
        "model": "SELECT * FROM plane WHERE Model = %s;"
    }

    keys = ["id: ", "owner: ", "maker: ", "model: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print("Plane " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def searchService(mydb):
    directions = """
    flight id,
    engineer id 
    """

    message = "Enter one of the above options to select a service:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to search for a service:"
    print(message1)
    data = input()

    queries = {
        "flight id": "SELECT * FROM services WHERE FlightID = %s;",
        "engineer": "SELECT * FROM services WHERE EngineerID = %s;"
    }

    keys = ["flight id: ", "engineer: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))

        i = 1
        for row in mycursor:
            print("Service " + str(i) + " information:")
            print("------------------")
            i = i + 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def deleteFlights(mydb):
    directions = """
    flight id,
    plane id,
    departure,
    destination,
    departure time,
    arrival time,
    controller,
    status,
    gate id,
    airstrip id,
    parking spot id,
    parking start,
    parking end    
    """

    message = "Enter one of the above options to delete flights:"

    print(directions)
    print(message)
    option = input()

    if option == "deaprture time" or option == "arrival time" or option == "parking start" or option == "parking end":
        print("Enter datetime data as follows: 2020-03-23 18:00:00")

    message1 = "Enter " + option + " to delete flights:"
    print(message1)
    data = input()

    queries = {
        "flight id": "DELETE FROM flight WHERE FlightID = %s;",
        "plane id": "DELETE FROM flight WHERE PlaneID = %s;",
        "departure": "DELETE FROM flight WHERE Departure = %s;",
        "destination": "DELETE FROM flight WHERE Destination = %s;",
        "departure time": "DELETE FROM flight WHERE DepartTime = %s;",
        "arrival time": "DELETE FROM flight WHERE ArrivalTime = %s;",
        "controller": "DELETE FROM flight WHERE Controller = %s;",
        "status": "DELETE FROM flight WHERE Status = %s;",
        "gate id": "DELETE FROM flight WHERE GateID = %s;",
        "airstrip id": "DELETE FROM flight WHERE AirstripID = %s;",
        "parking spot id": "DELETE FROM flight WHERE ParkingSpotID = %s;",
        "parking start": "DELETE FROM flight WHERE ParkingStart = %s;",
        "parking end": "DELETE FROM flight WHERE ParkingEnd = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteCompany(mydb):
    directions = """
    name,
    phone    
    """

    message = "Enter one of the above options to delete a comapny:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to delete a company:"
    print(message1)
    data = input()

    queries = {
        "name": "DELETE FROM company WHERE Name = %s;",
        "phone": "DELETE FROM company WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteController(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    message = "Enter one of the above options to delete a controller:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to delete a controller:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM controller WHERE ID = %s;",
        "name": "DELETE FROM controller WHERE Name = %s;",
        "surname": "DELETE FROM controller WHERE Surname = %s;",
        "phone": "DELETE FROM controller WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteEngineer(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    message = "Enter one of the above options to delete an engineer:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to delete an engineer:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM engineer WHERE EngineerID = %s;",
        "name": "DELETE FROM engineer WHERE Name = %s;",
        "surname": "DELETE FROM engineer WHERE Surname = %s;",
        "phone": "DELETE FROM engineer WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteFreighter(mydb):
    directions = """
    id,
    name,
    surname,
    phone    
    """

    message = "Enter one of the above options to delete a freighter:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to delete a freighter:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM freighter WHERE FreighterID = %s;",
        "name": "DELETE FROM freighter WHERE Name = %s;",
        "surname": "DELETE FROM freighter WHERE Surname = %s;",
        "phone": "DELETE FROM freighter WHERE Phone = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteLoad(mydb):
    directions = """
    flight id,
    freighter id    
    """

    message = "Enter one of the above options to delete a load:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to delete a load:"
    print(message1)
    data = input()

    queries = {
        "flight id": "DELETE FROM loads WHERE FlightID = %s;",
        "freighter id": "DELETE FROM loads WHERE FreighterID = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deletePlane(mydb):
    directions = """
    id,
    owner,
    maker,
    model    
    """

    message = "Enter one of the above options to delete a plane:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to delete a plane:"
    print(message1)
    data = input()

    queries = {
        "id": "DELETE FROM plane WHERE ID = %s;",
        "owner": "DELETE FROM plane WHERE Owner = %s;",
        "maker": "DELETE FROM plane WHERE Maker = %s;",
        "model": "DELETE FROM plane WHERE Model = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def deleteService(mydb):
    directions = """
    flight id,
    engineer id    
    """

    message = "Enter one of the above options to delete a service:"

    print(directions)
    print(message)
    option = input()

    message1 = "Enter " + option + " to delete a service:"
    print(message1)
    data = input()

    queries = {
        "flight id": "DELETE FROM services WHERE FlightID = %s;",
        "engineer id": "DELETE FROM services WHERE EngineerID = %s;"
    }

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[option], tuple([data]))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data deleted successfully.")


def insertFlight(mydb):
    mycursor = mydb.cursor()

    flight = {
        "flight_id:": "",
        "plane_id:": "",
        "departure:": "",
        "destination:": "",
        "departure time:": "",
        "arrival time:": "",
        "real departure time:": "",
        "controller:": "",
        "status:": "",
        "gate_id:": "",
        "airstrip_id:": "",
        "parkingspot_id:": "",
        "parking start date:": "",
        "parking end date:": ""
    }

    for key in flight:
        flight[key] = ask_data(key)
        print(flight[key])

    try:
        mycursor.execute(
            "INSERT INTO flight (FlightID,PlaneID,Departure,Destination,DepartTime,ArrivalTime,RealDepartTime,Controller,Status,GateID,AirstripID,ParkingSpotID,ParkingStart,ParkingEnd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (flight['flight_id:'], flight['plane_id:'], flight['departure:'], flight['destination:'],
             flight['departure time:'], flight['arrival time:'], flight['real departure time:'], flight['controller:'],
             flight['status:'], flight['gate_id:'], flight['airstrip_id:'], flight['parkingspot_id:'],
             flight['parking start date:'], flight['parking end date:']))
    except:
        print("You entered invalid data. Try again.")

    mydb.commit()
    print("Data inserted successfully.")


def insertCompany(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "company name:": "",
        "company phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO company (Name,Phone) VALUES (%s,%s)",
                         (mydict['company name:'], mydict['company phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertController(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "controller id:": "",
        "controller name:": "",
        "controller surname:": "",
        "controller phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO controller (ID,Name,Surname,Phone) VALUES (%s,%s,%s,%s)", (
        mydict['controller id:'], mydict['controller name:'], mydict['controller surname:'],
        mydict['controller phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertEngineer(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "engineer id:": "",
        "engineer name:": "",
        "engineer surname:": "",
        "engineer phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO engineer (EngineerID,Name,Surname,Phone) VALUES (%s,%s,%s,%s)", (
        mydict['engineer id:'], mydict['engineer name:'], mydict['engineer surname:'], mydict['engineer phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertFreighter(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "freighter id:": "",
        "freighter name:": "",
        "freighter surname:": "",
        "freighter phone:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO freighter (FreighterID,Name,Surname,Phone) VALUES (%s,%s,%s,%s)", (
        mydict['freighter id:'], mydict['freighter name:'], mydict['freighter surname:'], mydict['freighter phone:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertLoad(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "flight id:": "",
        "freighter id:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO loads (FlightID,FreighterID) VALUES (%s,%s)",
                         (mydict['flight id:'], mydict['freighter id:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertPlane(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "plane id:": "",
        "plane owner:": "",
        "plane maker:": "",
        "plane model:": "",
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO plane (ID,Owner,Maker,Model) VALUES (%s,%s,%s,%s)",
                         (mydict['plane id:'], mydict['plane owner:'], mydict['plane maker:'], mydict['plane model:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def insertService(mydb):
    mycursor = mydb.cursor()

    mydict = {
        "flight id:": "",
        "engineer id:": ""
    }

    for key in mydict:
        mydict[key] = ask_data(key)
        print(mydict[key])

    try:
        mycursor.execute("INSERT INTO Services (FlightID,EngineerID) VALUES (%s,%s)",
                         (mydict['flight id:'], mydict['engineer id:']))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Data inserted successfully.")


def updateFlight(mydb):
    print("Enter flight ID:")
    flight_id = input()

    directions = """
    flight_id,
    plane_id,
    departure,
    destination,
    departure time,
    arrival time,
    real departure time,
    controller,
    status,
    gate_id,
    airstrip_id,
    parkingspot_id,
    parking start date,
    parking end date    
    """

    print(directions)
    print("Enter one of the above fields to update it:")
    choice = input()

    flight = {
        "flight_id": "FlightID",
        "plane_id": "PlaneID",
        "departure": "Departure",
        "destination": "Destination",
        "departure time": "DepartTime",
        "arrival time": "ArrivalTime",
        "real departure time": "RealDepartTime",
        "controller": "Controller",
        "status": "Status",
        "gate_id": "GateID",
        "airstrip_id": "AirstripID",
        "parkingspot_id": "ParkingSpotID",
        "parking start date": "ParkingStart",
        "parking end date": "ParkingEnd"
    }

    queries = {
        "flight_id": "UPDATE flight SET FlightID = %s WHERE FlightID = %s;",
        "plane_id": "UPDATE flight SET PlaneID = %s WHERE FlightID = %s;",
        "departure": "UPDATE flight SET Departure = %s WHERE FlightID = %s;",
        "destination": "UPDATE flight SET Destination = %s WHERE FlightID = %s;",
        "departure time": "UPDATE flight SET DepartTime = %s WHERE FlightID = %s;",
        "arrival time": "UPDATE flight SET ArrivalTime = %s WHERE FlightID = %s;",
        "real departure time": "UPDATE flight SET RealDepartTime = %s WHERE FlightID = %s;",
        "controller": "UPDATE flight SET Controller = %s WHERE FlightID = %s;",
        "status": "UPDATE flight SET Status = %s WHERE FlightID = %s;",
        "gate_id": "UPDATE flight SET GateID = %s WHERE FlightID = %s;",
        "airstrip_id": "UPDATE flight SET AirstripID = %s WHERE FlightID = %s;",
        "parkingspot_id": "UPDATE flight SET ParkingSpotID = %s WHERE FlightID = %s;",
        "parking start date": "UPDATE flight SET ParkingStart = %s WHERE FlightID = %s;",
        "parking end date": "UPDATE flight SET ParkingEnd = %s WHERE FlightID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in flight:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, flight_id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateCompany(mydb):
    print("Enter companies' name:")
    company_name = input()

    directions = """
    name,
    phone    
    """

    print(directions)
    print("Enter one of the above fields to update it:")
    choice = input()

    company = {
        "name": "Name",
        "phone": "Phone"
    }

    queries = {
        "name": "UPDATE company SET Name = %s WHERE Name = %s;",
        "phone": "UPDATE company SET Phone = %s WHERE Name = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in company:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, company_name))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateController(mydb):
    print("Enter controller's id:")
    controller_id = input()

    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    print("Enter one of the above fields to update it:")
    choice = input()

    controller = {
        "id": "ID",
        "name": "Name",
        "surname": "Surname",
        "phone": "Phone"
    }

    queries = {
        "id": "UPDATE controller SET ID = %s WHERE ID = %s;",
        "name": "UPDATE controller SET Name = %s WHERE ID = %s;",
        "surname": "UPDATE controller SET Surname = %s WHERE ID = %s;",
        "phone": "UPDATE controller SET Phone = %s WHERE ID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in controller:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, controller_id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateEngineer(mydb):
    print("Enter engineer's id:")
    engineer_id = input()

    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    print("Enter one of the above fields to update it:")
    choice = input()

    engineer = {
        "id": "EngineerID",
        "name": "Name",
        "surname": "Surname",
        "phone": "Phone"
    }

    queries = {
        "id": "UPDATE engineer SET EngineerID = %s WHERE EngineerID = %s;",
        "name": "UPDATE engineer SET Name = %s WHERE EngineerID = %s;",
        "surname": "UPDATE engineer SET Surname = %s WHERE EngineerID = %s;",
        "phone": "UPDATE engineer SET Phone = %s WHERE EngineerID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in engineer:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, engineer_id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updateFreighter(mydb):
    print("Enter freighter's id:")
    id = input()

    directions = """
    id,
    name,
    surname,
    phone    
    """

    print(directions)
    print("Enter one of the above fields to update it:")
    choice = input()

    freighter = {
        "id": "FreighterID",
        "name": "Name",
        "surname": "Surname",
        "phone": "Phone"
    }

    queries = {
        "id": "UPDATE freighter SET FreighterID = %s WHERE FreighterID = %s;",
        "name": "UPDATE freighter SET Name = %s WHERE FreighterID = %s;",
        "surname": "UPDATE freighter SET Surname = %s WHERE FreighterID = %s;",
        "phone": "UPDATE freighter SET Phone = %s WHERE FreighterID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in freighter:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def updatePlane(mydb):
    print("Enter plane's id:")
    id = input()

    directions = """
    id,
    maker,
    model    
    """

    print(directions)
    print("Enter one of the above fields to update it:")
    choice = input()

    plane = {
        "id": "ID",
        "maker": "Maker",
        "model": "Model"
    }

    queries = {
        "id": "UPDATE plane SET ID = %s WHERE ID = %s;",
        "Maker": "UPDATE plane SET Maker = %s WHERE ID = %s;",
        "Model": "UPDATE plane SET Model = %s WHERE ID = %s;"
    }

    message = "Enter new " + choice + ":"
    print(message)
    if choice in plane:
        new_field = input()
    else:
        print("No such field in database.")
        exit(1)

    try:
        mycursor = mydb.cursor()
        mycursor.execute(queries[choice], (new_field, id))
        mydb.commit()
    except:
        print("You entered invalid data. Try again.")

    print("Table updated successfully.")


def checkGates(mydb, check_minutes):
    check_minutes = str(check_minutes)
    query = '''SELECT A.FlightID, B.FlightID,A.destination,A.GateID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Destination='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))<%s) )
    UNION SELECT A.FlightID, B.FlightID,A.departure,A.GateID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Departure='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))<%s) )
    UNION SELECT A.FlightID, B.FlightID,A.departure,A.GateID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Departure='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))<%s) )
    UNION SELECT A.FlightID, B.FlightID,A.destination,A.GateID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.GateID=B.GateID) WHERE ((A.Destination='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))<%s) );'''
    mytuple = (check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes,
               check_minutes)

    keys = ["flight 1: ", "flight 2: ", "airport: ", "gate: ", "time difference: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(query, mytuple)

        i = 1
        for row in mycursor:
            print("Collision: "+str(i))
            print("------------------")
            i += 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def checkAirstrip(mydb, check_minutes):
    check_minutes = str(check_minutes)
    query = '''SELECT A.FlightID, B.FlightID,A.destination,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Destination='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.ArrivalTime))<%s) )
        UNION SELECT A.FlightID, B.FlightID,A.departure,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Departure='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.DepartTime))<%s) )
        UNION SELECT A.FlightID, B.FlightID,A.departure,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Departure='UPA') AND (B.Destination='UPA') AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.DepartTime,B.ArrivalTime))<%s) )
        UNION SELECT A.FlightID, B.FlightID,A.destination,A.AirstripID,abs(TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime)) AS minutes FROM flight A INNER JOIN Flight B ON (A.FlightID<B.FlightID AND A.AirstripID=B.AirstripID) WHERE ((A.Destination='UPA') AND (B.Departure='UPA') AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))>-%s) AND ((TIMESTAMPDIFF(minute,A.ArrivalTime,B.DepartTime))<%s) );'''
    mytuple = (check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes, check_minutes,
               check_minutes)

    keys = ["flight 1: ", "flight 2: ", "airport: ", "airstrip: ", "time difference: "]

    try:
        mycursor = mydb.cursor()
        mycursor.execute(query, mytuple)

        i = 1
        for row in mycursor:
            print("Collision: "+str(i))
            print("------------------")
            i += 1
            for counter in range(len(row)):
                result = keys[counter] + str(row[counter])
                print(result)
            print("\n\n")

    except:
        print("Invalid data entered. Try again.")


def main():
    mydb = connect_database()
    printDirections()
    chooseFunction(mydb)

    exit(1)


main()








