CREATE TABLE Εταιρεία (
	Επωνυμία varchar,
	Τηλέφωνο varchar
);

CREATE TABLE Αεροπλάνο (
	ID varchar,
	Ιδιοκτήτης varchar,
	Κατασκευαστής varchar,
	Μοντέλο varchar
);

CREATE TABLE Πτήση (
	Κωδικός πτήσης varchar,
	ID αεροπλάνου varchar,
	Αριθμός επιβατών integer,
	Αναχώρηση από varchar,
	Προορισμός varchar,
	Ημερομηνία/Ώρα αναχώρησης datetime,
	Ημερομηνία/Ώρα άφιξης datetime,
	Πραγματική ώρα αναχώρησης/άφιξης datetime,
	Αναχώρηση ή άφιξη binary,
	Ελεγκτής varchar,
	Κατάσταση varchar,
	Πύλη varchar,
	Αεροδιάδρομος varchar,
	ID θέσης στάθμευσης varchar,
	Ώρα άφιξης στη στάθμευση datetime,
	Ώρα αναχώρησης από στάθμευση datetime
);

CREATE TABLE Ελεγκτής (
	ID binary,
	Όνομα varchar,
	Επώνυμο varchar,
	Τηλέφωνο integer
);

CREATE TABLE Πύλη (
	ID varchar,
	Terminal ID varchar
);

CREATE TABLE Terminal (
	ID varchar PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE Συντηρητής (
	ID varchar,
	Όνομα varchar,
	Επώνυμο varchar,
	Τηλέφωνο integer
);

CREATE TABLE Συντηρεί (
	Κωδικός πτήσης varchar,
	ID συντηρητή varchar
);

CREATE TABLE "Θέση στάθμευσης" (
	ID varchar
);

CREATE TABLE Αεροδιάδρομος (
	ID αεροδιαδρόμου varchar
);

CREATE TABLE Φορτωτής (
	ID varchar,
	Όνομα varchar,
	Επώνυμο varchar,
	Τηλέφωνο integer
);

CREATE TABLE Φορτώνει (
	Κωδικός πτήσης varchar,
	ID φορτωτή varchar
);

