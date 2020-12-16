CREATE TABLE `Εταιρεία` (
	`Επωνυμία` varchar(255) NOT NULL,
	`Τηλέφωνο` varchar(255) NOT NULL,
	PRIMARY KEY (`Επωνυμία`)
);

CREATE TABLE `Αεροπλάνο` (
	`ID` varchar(255) NOT NULL,
	`Ιδιοκτήτης` varchar(255) NOT NULL,
	`Κατασκευαστής` varchar(255) NOT NULL,
	`Μοντέλο` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Πτήση` (
	`Κωδικός πτήσης` varchar(255) NOT NULL,
	`ID αεροπλάνου` varchar(255) NOT NULL,
	`Αριθμός επιβατών` INT(255),
	`Αναχώρηση από` varchar(255) NOT NULL,
	`Προορισμός` varchar(255) NOT NULL,
	`Ημερομηνία/Ώρα αναχώρησης` DATETIME NOT NULL,
	`Ημερομηνία/Ώρα άφιξης` DATETIME NOT NULL,
	`Πραγματική ώρα αναχώρησης/άφιξης` DATETIME NOT NULL,
	`Αναχώρηση ή άφιξη` BINARY(1) NOT NULL,
	`Ελεγκτής` varchar(255) NOT NULL,
	`Κατάσταση` varchar(255) NOT NULL,
	`Πύλη` varchar(255) NOT NULL,
	`Αεροδιάδρομος` varchar(255) NOT NULL,
	`ID θέσης στάθμευσης` varchar(255),
	`Ώρα άφιξης στη στάθμευση` DATETIME,
	`Ώρα αναχώρησης από στάθμευση` DATETIME,
	PRIMARY KEY (`Κωδικός πτήσης`)
);

CREATE TABLE `Ελεγκτής` (
	`ID` BINARY NOT NULL,
	`Όνομα` varchar(255) NOT NULL,
	`Επώνυμο` varchar(255) NOT NULL,
	`Τηλέφωνο` INT(255) NOT NULL UNIQUE,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Πύλη` (
	`ID` varchar(255) NOT NULL,
	`Terminal ID` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Terminal` (
	`ID` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Συντηρητής` (
	`ID` varchar(255) NOT NULL,
	`Όνομα` varchar(255) NOT NULL,
	`Επώνυμο` varchar(255) NOT NULL,
	`Τηλέφωνο` INT(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Συντηρεί` (
	`Κωδικός πτήσης` varchar(255) NOT NULL,
	`ID συντηρητή` varchar(255) NOT NULL,
	PRIMARY KEY (`Κωδικός πτήσης`,`ID συντηρητή`)
);

CREATE TABLE `Θέση στάθμευσης` (
	`ID` varchar(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Αεροδιάδρομος` (
	`ID αεροδιαδρόμου` varchar(255) NOT NULL,
	PRIMARY KEY (`ID αεροδιαδρόμου`)
);

CREATE TABLE `Φορτωτής` (
	`ID` varchar(255) NOT NULL,
	`Όνομα` varchar(255) NOT NULL,
	`Επώνυμο` varchar(255) NOT NULL,
	`Τηλέφωνο` INT(255) NOT NULL,
	PRIMARY KEY (`ID`)
);

CREATE TABLE `Φορτώνει` (
	`Κωδικός πτήσης` varchar(255) NOT NULL,
	`ID φορτωτή` varchar(255) NOT NULL,
	PRIMARY KEY (`Κωδικός πτήσης`,`ID φορτωτή`)
);

ALTER TABLE `Αεροπλάνο` ADD CONSTRAINT `Αεροπλάνο_fk0` FOREIGN KEY (`Ιδιοκτήτης`) REFERENCES `Εταιρεία`(`Επωνυμία`);

ALTER TABLE `Πτήση` ADD CONSTRAINT `Πτήση_fk0` FOREIGN KEY (`ID αεροπλάνου`) REFERENCES `Αεροπλάνο`(`ID`);

ALTER TABLE `Πτήση` ADD CONSTRAINT `Πτήση_fk1` FOREIGN KEY (`Ελεγκτής`) REFERENCES `Ελεγκτής`(`ID`);

ALTER TABLE `Πτήση` ADD CONSTRAINT `Πτήση_fk2` FOREIGN KEY (`Πύλη`) REFERENCES `Πύλη`(`ID`);

ALTER TABLE `Πτήση` ADD CONSTRAINT `Πτήση_fk3` FOREIGN KEY (`Αεροδιάδρομος`) REFERENCES `Αεροδιάδρομος`(`ID αεροδιαδρόμου`);

ALTER TABLE `Πτήση` ADD CONSTRAINT `Πτήση_fk4` FOREIGN KEY (`ID θέσης στάθμευσης`) REFERENCES `Θέση στάθμευσης`(`ID`);

ALTER TABLE `Πύλη` ADD CONSTRAINT `Πύλη_fk0` FOREIGN KEY (`Terminal ID`) REFERENCES `Terminal`(`ID`);

ALTER TABLE `Συντηρεί` ADD CONSTRAINT `Συντηρεί_fk0` FOREIGN KEY (`Κωδικός πτήσης`) REFERENCES `Πτήση`(`Κωδικός πτήσης`);

ALTER TABLE `Συντηρεί` ADD CONSTRAINT `Συντηρεί_fk1` FOREIGN KEY (`ID συντηρητή`) REFERENCES `Συντηρητής`(`ID`);

ALTER TABLE `Φορτώνει` ADD CONSTRAINT `Φορτώνει_fk0` FOREIGN KEY (`Κωδικός πτήσης`) REFERENCES `Πτήση`(`Κωδικός πτήσης`);

ALTER TABLE `Φορτώνει` ADD CONSTRAINT `Φορτώνει_fk1` FOREIGN KEY (`ID φορτωτή`) REFERENCES `Φορτωτής`(`ID`);

