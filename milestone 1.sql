Create Database Used_Car_Marketplace; 
Alter Database Used_Car_Marketplace  character set=utf8mb4;
use Used_Car_Marketplace;
drop table ad;
drop table Details;
drop table Purchases;
drop table Details_features;

Create table IF NOT EXISTS Ad(
ad_id VARCHAR(20) NOT NULL PRIMARY KEY, 
title VARCHAR(70) NOT NULL,
regionLocation VARCHAR(25) NOT NULL, 
cityLocation VARCHAR(25) NOT NULL,
postDate VARCHAR(50) );

Create table IF NOT EXISTS Details(
ad_id VARCHAR(20) NOT NULL,
Brand varchar(20) NOT NULL,
Make varchar(20) NOT NULL,
caryear year NOT NULL,
/*Ad_type varchar(10) NOT NULL,*/
Price VARCHAR(20) NOT NULL,
Transmisson varchar(10) ,
Body_type VARCHAR(20) ,
Color VARCHAR(20) ,
min_CC  VARCHAR(20)  COMMENT "FIXED RANGE",
max_CC  VARCHAR(20),
Fuel_type VARCHAR(15) ,
min_Kilos VARCHAR(20) ,
max_Kilos VARCHAR(20) ,
Payment_method VARCHAR(15) ,
Car_description VARCHAR(4096),
foreign key(ad_id) references ad (ad_id) on delete restrict on update cascade,
primary key (ad_id,Brand));

Create table IF NOT EXISTS Details_features(
ad_id VARCHAR(40) NOT NULL, 
Brand varchar(40) NOT NULL,
feature varchar(50) NOT NULL,
primary key(ad_id, brand, feature),
foreign key(ad_id,Brand) references Details (ad_id,Brand) 
);

Create Table IF NOT EXISTS Register( 
UserName VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL PRIMARY KEY,
birthdate date NOT NULL,
gender CHAR);

Create table IF NOT EXISTS Register_Interest(
email VARCHAR(100) NOT NULL,
foreign key (email) references Register(email) ,
interest VARCHAR(20) NOT NULL,
primary key( email, interest));

Create table IF NOT EXISTS Purchases(
ad_id VARCHAR(20) NOT NULL,
user_email VARCHAR(100) NOT NULL,
price VARCHAR(20) NOT NULL,
Review VARCHAR(1000) NOT NULL, 
Rating int(1) check(rating between 1 and 5) NOT NULL,
Foreign key(ad_id) references Ad (ad_id) ,
foreign key (user_email) references Register(email) ,
Primary key(ad_id, user_email));



Create Table IF NOT EXISTS  Seller(
seller_id Varchar(150) NOT NULL Primary key,
member_since VARCHAR(20),
seller_name VARCHAR(100) NOT NULL
/*phone_number VARCHAR(11),*/
); 
