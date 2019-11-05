drop table STUDENT_MARKS1; 
drop table STUDENT_MARKS;

drop table audit;
drop table blog; 

drop table patient; 
drop table room ;
drop table bill ;
drop table medicine; 

create table STUDENT_MARKS (STUDENT_ID INT,NAME VARCHAR(25),SUB1 FLOAT,SUB2 FLOAT,SUB3 FLOAT,SUB4 FLOAT,SUB5 FLOAT,TOTAL FLOAT,PER_MARKS FLOAT,GRADE VARCHAR(20));

INSERT INTO STUDENT_MARKS VALUES (1,"STEVEN KING",0,0,0,0,0,0,0.00,"");
INSERT INTO STUDENT_MARKS VALUES (2,"NEENA KOCHHAR",0,0,0,0,0,0,0.00,"");
INSERT INTO STUDENT_MARKS VALUES (3,"LEX DE HAAN",0,0,0,0,0,0,0.00,"");
INSERT INTO STUDENT_MARKS VALUES (4,"ALEXANDER HUNOLD",0,0,0,0,0,0,0.00,"");

INSERT INTO STUDENT_MARKS VALUES (5,"HUNOLD",0,0,0,0,0,0,0.00,"");
alter table STUDENT_MARKS ADD PRIMARY KEY(STUDENT_ID);
create table STUDENT_MARKS1 (STUDENT_ID INT,TOTAL FLOAT,PER_MARKS FLOAT,GRADE FLOAT,foreign key(STUDENT_ID) references STUDENT_MARKS(STUDENT_ID) ON DELETE CASCADE);


CREATE TABLE blog (
id int,
title varchar(20),
content varchar(20),
deleted int,
PRIMARY KEY (id)
);
CREATE TABLE audit( blog_id int,
changetype enum('NEW','EDIT','DELETE') NOT NULL,
changetime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE
CURRENT_TIMESTAMP,
foreign key(blog_id) references blog(id)
) ;


create table patient (id int,name varchar(10),PRIMARY KEY(id));
create table room(pid int,status varchar(10));
create table medicine(pid int,mcode int); 
create table bill(pid int,bill int); 

insert into patient values (1,'a');
insert into patient values (2,'b');
insert into patient values (3,'c');
insert into patient values (4,'d');


insert into room values (1,'filled');
insert into room values (2,'filled');
insert into room values (3,'filled');

insert into bill values (1,100);
insert into bill values (2,200);
insert into bill values (3,300);

insert into medicine values (1,1);
insert into medicine values (2,2);
insert into medicine values (3,2);

