select * from STUDENT_MARKS;
drop trigger if exists update_after;
delimiter //
create trigger update_after 
before UPDATE on STUDENT_MARKS
for each row
BEGIN 

set NEW.TOTAL=NEW.SUB1+NEW.SUB2+NEW.SUB3+NEW.SUB4+NEW.SUB5;
SET NEW.PER_MARKS = NEW.TOTAL/5;
IF NEW.PER_MARKS>=90 THEN set NEW.GRADE = "EXCELLENT";
ELSEIF NEW.PER_MARKS>=75 THEN set NEW.GRADE = "VERY GOOD";
ELSEIF NEW.PER_MARKS>=60 THEN set NEW.GRADE = "GOOD";
ELSEIF NEW.PER_MARKS>=40 THEN set NEW.GRADE = "AVERAGE";
ELSE set NEW.GRADE = "NOT PROMOTED";
END IF;

end //
delimiter ;


UPDATE STUDENT_MARKS SET SUB1=60,SUB2=50,SUB3=70,SUB4=60,SUB5=65 WHERE STUDENT_ID=1;
UPDATE STUDENT_MARKS SET SUB1=6,SUB2=4,SUB3=0,SUB4=8,SUB5=2 WHERE STUDENT_ID=2;
UPDATE STUDENT_MARKS SET SUB1=100,SUB2=100,SUB3=90,SUB4=80,SUB5=100 WHERE STUDENT_ID=3;
UPDATE STUDENT_MARKS SET SUB1=80,SUB2=65,SUB3=75,SUB4=80,SUB5=83 WHERE STUDENT_ID=4;
UPDATE STUDENT_MARKS SET SUB1=40,SUB2=45,SUB3=35,SUB4=50,SUB5=33 WHERE STUDENT_ID=5;
select * from STUDENT_MARKS;


select * from audit;
drop trigger if exists insert_after;
DELIMITER //
create trigger insert_after 
after insert on blog 
for each row
BEGIN
if NEW.deleted=1 then 
insert into audit values (NEW.id,"DELETE",CURRENT_TIMESTAMP);
ELSEIF NEW.deleted=0 then 
insert into audit values (NEW.id,"NEW",CURRENT_TIMESTAMP);
END IF;
END //
DELIMITER ;


insert into blog values (1,"Test","TEst sample",0);
insert into blog values (2,"Test","TEst sample",1);

select * from audit;


select * from patient;
select * from bill;
select * from medicine;
select * from room;

drop trigger if exists after_delete;
DELIMITER //
create trigger after_delete 
after delete on patient 
for each row
BEGIN
DELETE from bill where pid=OLD.id;
DELETE from medicine where pid=OLD.id;
UPDATE room set pid=NULL,status='Empty' where pid=OLD.id;
END //
DELIMITER ;


delete from patient where id=3;
select * from patient;
select * from bill;
select * from medicine;
select * from room;
