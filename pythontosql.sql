/*
Tabele erstellen für immport
*/

/*
create database pythontosql;
*/

use pythontosql;

drop table if exists kunden;

CREATE TABLE KundenJMI (
    Kundennr INT PRIMARY KEY,
    Name VARCHAR(100),
    Kundenalter INT,
    PLZ VARCHAR(10),
    Stadt VARCHAR(100)
);

create index inx_PLZ
on KundenJMI (PLZ);

