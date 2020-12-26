-- Company
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('NtuaAirlines', 1234567890) ;
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('AuthAirlines', 4567890123) ;
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('UpatrasAirlines', 7894560123) ;
INSERT INTO `Company`(`Name`, `Phone`)
VALUES ('UmistAirlines', 9638527410) ;


-- Plane
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAA', 'NtuaAirlines', 'Boeing', '737') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAB', 'NtuaAirlines', 'Airbus', 'A320') ;

INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAC', 'AuthAirlines', 'Airbus', 'A330') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAD', 'AuthAirlines', 'Boeing', '777') ;

INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAE', 'UpatrasAirlines', 'Boeing', '727') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('SX-AAF', 'UpatrasAirlines', 'Boeing', '737') ;

INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('N00001', 'UmistAirlines', 'McDonnellDouglas', 'DC-9') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('N00002', 'UmistAirlines', 'McDonnellDouglas', 'DC-9') ;
INSERT INTO `Plane`(`ID`,`Owner`,`Maker`,`Model`)
VALUES ('N00003', 'UmistAirlines', 'Boeing', '747') ;

-- Flight



-- Controller
INSERT INTO `Controller`(`ID`,`Name`,`Surname`,`Phone`)
VALUES ('001', 'Peggy', 'Zina', 8527416530) ;
INSERT INTO `Controller`(`ID`,`Name`,`Surname`,`Phone`)
VALUES ('002', 'Panos', 'Kiamos', 4214524542) ;
INSERT INTO `Controller`(`ID`,`Name`,`Surname`,`Phone`)
VALUES ('003', 'Vassilis', 'Tsitsanis', 3410045429) ;

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
VALUES ('001', 'Nikos', 'Karvelas', 1245648796) ;
INSERT INTO `Engineer`(`EngineerID`,`Name`,`Surname`,`Phone`)
VALUES ('002', 'Giorgos', 'Samoladas', 9431554780) ;
INSERT INTO `Engineer`(`EngineerID`,`Name`,`Surname`,`Phone`)
VALUES ('003', 'Mims', 'Plessas', 6478202354) ;

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
VALUES ('001', 'Makis', 'Dimakis', 4568790123) ;
INSERT INTO `Engineer`(`FreighterID`,`Name`,`Surname`,`Phone`)
VALUES ('002', 'Petros', 'Mokas', 6958741230) ;
INSERT INTO `Engineer`(`FreighterID`,`Name`,`Surname`,`Phone`)
VALUES ('003', 'Petroloukas', 'Chalkias', 5846321745) ;

-- Loads