-- Τρέχουσα ώρα: '2021-02-01 07:30:00'

-- Company
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('NtuaAirlines', '1234567890') ;
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('AuthAirlines', '4567890123') ;
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('UpatrasAirlines', '7894560123') ;
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('UmistAirlines', '9638527410') ;


-- Plane
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAA', 'NtuaAirlines', 'Boeing', '737') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAB', 'NtuaAirlines', 'Airbus', 'A320') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAD', 'NtuaAirlines', 'Boeing', '727') ;

INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAE', 'AuthAirlines', 'Airbus', 'A330') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAF', 'AuthAirlines', 'Boeing', '777') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAG', 'AuthAirlines', 'Airbus', 'A330') ;

INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAH', 'UpatrasAirlines', 'Boeing', '727') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAI', 'UpatrasAirlines', 'Boeing', '737') ;

INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('N00001', 'UmistAirlines', 'McDonnellDouglas', 'DC-9') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('N00002', 'UmistAirlines', 'McDonnellDouglas', 'DC-9') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('N00003', 'UmistAirlines', 'Boeing', '747') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('N00004', 'UmistAirlines', 'Airbus', 'A320') ;


-- Flight
INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('NT811','SX-AAA','UPA','JFK', '2021-02-01 08:00:00', '2021-02-01 18:00:00',
NULL,'001','Boarding','A1','002','001','2021-02-01 06:00:00','2021-02-01 07:20:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('NT951','SX-AAA','JFK','UPA', '2021-02-02 19:00:00', '2021-02-03 03:00:00',
NULL,'001',NULL,'A2','002','002','2021-02-01 04:00:00','2021-02-01 08:35:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('NT325','SX-AAB','UPA','LHR', '2021-02-01 08:30:00', '2021-02-01 13:00:00',
NULL,'002','Parking','B1','001','003','2021-02-01 04:00:00','2021-02-01 07:45:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('NT729','SX-AAD','UPA','LGW', '2021-02-01 07:25:00', '2021-02-01 13:00:00',
'2021-02-01 07:28:00','001','TakeOff','B2','001','001','2021-02-01 05:00:00','2021-02-01 06:50:00') ;
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('UP811','SX-AAH','UPA','MJT', '2021-02-01 08:00:00', '2021-02-01 08:00:00',
'2021-02-01 08:00:00','001','TakeOff','A1','002','001','2021-02-01 08:00:00','2021-02-01 08:00:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('UP811','SX-AAH','UPA','MJT', '2021-02-01 08:00:00', '2021-02-01 08:00:00',
'2021-02-01 08:00:00','001','Service','A1','002','001','2021-02-01 08:00:00','2021-02-01 08:00:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('UP811','SX-AAH','UPA','MJT', '2021-02-01 08:00:00', '2021-02-01 08:00:00',
'2021-02-01 08:00:00','001','Service','A1','002','001','2021-02-01 08:00:00','2021-02-01 08:00:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('UP811','SX-AAH','UPA','MJT', '2021-02-01 08:00:00', '2021-02-01 08:00:00',
'2021-02-01 08:00:00','001','Service','A1','002','001','2021-02-01 08:00:00','2021-02-01 08:00:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('UP811','SX-AAH','UPA','MJT', '2021-02-01 08:00:00', '2021-02-01 08:00:00',
'2021-02-01 08:00:00','001','Boarding','A1','002','001','2021-02-01 08:00:00','2021-02-01 08:00:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('UP811','SX-AAH','UPA','MJT', '2021-02-01 08:00:00', '2021-02-01 08:00:00',
'2021-02-01 08:00:00','001','Boarding','A1','002','001','2021-02-01 08:00:00','2021-02-01 08:00:00') ;

INSERT INTO `Flight`(`FlightID`,`PlaneID`,`Departure`,`Destination`, 'DepartTime',`ArrivalTime`,
`RealDepartTime`,`Controller`,`Status`,`GateID`,`AirstripID`,`ParkingSpotID`,
`ParkingStart`,`ParkingEnd`)
VALUES ('UP811','SX-AAH','UPA','MJT', '2021-02-01 08:00:00', '2021-02-01 08:00:00',
'2021-02-01 08:00:00','001','Landing','A1','002','001','2021-02-01 08:00:00','2021-02-01 08:00:00') ;


-- Controller
INSERT INTO `Controller`(`ID`,`Name`,`Surname`,`Phone`)
VALUES ('001', 'Peggy', 'Zina', '8527416530') ;
INSERT INTO `Controller`(`ID`,`Name`,`Surname`,`Phone`)
VALUES ('002', 'Panos', 'Kiamos', '4214524542') ;
INSERT INTO `Controller`(`ID`,`Name`,`Surname`,`Phone`)
VALUES ('003', 'Vassilis', 'Tsitsanis', '3410045429') ;

-- Gate
INSERT INTO `Gate`(`GateID`,`TerminalID`)
VALUES ('A1', '001') ;
INSERT INTO `Gate`(`GateID`,`TerminalID`)
VALUES ('A2', '001') ;
INSERT INTO `Gate`(`GateID`,`TerminalID`)
VALUES ('B1', '002') ;
INSERT INTO `Gate`(`GateID`,`TerminalID`)
VALUES ('B2', '002') ;

-- Terminal
INSERT INTO `Terminal`(`ID`) VALUES ('001') ;
INSERT INTO `Terminal`(`ID`) VALUES ('002') ;

--Engineer
INSERT INTO `Engineer`(`EngineerID`,`Name`,`Surname`,`Phone`)
VALUES ('001', 'Nikolaos', 'Karvelas', '1245648796') ;
INSERT INTO `Engineer`(`EngineerID`,`Name`,`Surname`,`Phone`)
VALUES ('002', 'Georgios', 'Samoladas', '9431554780') ;
INSERT INTO `Engineer`(`EngineerID`,`Name`,`Surname`,`Phone`)
VALUES ('003', 'Mims', 'Plessas', '6478202354') ;
INSERT INTO `Engineer`(`EngineerID`,`Name`,`Surname`,`Phone`)
VALUES ('003', 'Ioannis', 'Oikonomopoulos', '5469875311') ;

-- Services

-- ParkingSpot
INSERT INTO `ParkingSpot`(`ID`) VALUES ('001') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('002') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('003') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('004') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('005') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('006') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('007') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('008') ;
INSERT INTO `ParkingSpot`(`ID`) VALUES ('009') ;

-- Airstrip
INSERT INTO `Airstrip`(`AirstripID`) VALUES ('001') ;
INSERT INTO `Airstrip`(`AirstripID`) VALUES ('002') ;

-- Freighter
INSERT INTO `Engineer`(`FreighterID`,`Name`,`Surname`,`Phone`)
VALUES ('001', 'Dimitrios', 'Efthimiou', '4568790123') ;
INSERT INTO `Engineer`(`FreighterID`,`Name`,`Surname`,`Phone`)
VALUES ('002', 'Petros', 'Mokas', '6958741230') ;
INSERT INTO `Engineer`(`FreighterID`,`Name`,`Surname`,`Phone`)
VALUES ('003', 'Ioannis', 'Vassiliou', '5846321745') ;

-- Loads