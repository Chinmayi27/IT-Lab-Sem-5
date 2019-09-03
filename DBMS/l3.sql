SELECT Fname, Bdate,Address FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.Dno=DEPARTMENT.Dnumber AND DEPARTMENT.Dname='Administration';


SELECT SUM(Salary) FROM EMPLOYEE, DEPARTMENT WHERE Dname = 'Research' AND EMPLOYEE.Dno=DEPARTMENT.Dnumber;


SELECT Count(*) FROM EMPLOYEE, DEPARTMENT WHERE Dname = 'Administration' AND EMPLOYEE.Dno = DEPARTMENT.Dnumber;


SELECT Pname, Pnumber, COUNT(*) FROM PROJECT, WORKS_ON WHERE PROJECT.Pnumber = WORKS_ON.Pno GROUP BY PROJECT.Pnumber;


SELECT Pname, Pnumber, COUNT(*) FROM PROJECT, WORKS_ON WHERE PROJECT.Pnumber = WORKS_ON.Pno AND PROJECT.Dnum=5 GROUP BY PROJECT.Pnumber;


SELECT Pnumber, Dno, Lname, Address from PROJECT, DEPARTMENT, EMPLOYEE WHERE PROJECT.Plocation='Houston' AND PROJECT.Dnum=DEPARTMENT.Dnumber AND DEPARTMENT.Mgr_ssn = EMPLOYEE.Ssn;


SELECT  Fname, Lname, Pno, Dno from EMPLOYEE, WORKS_ON WHERE EMPLOYEE.Ssn=WORKS_ON.Essn ORDER BY Dno, Fname, Lname;


SELECT Fname, Lname FROM EMPLOYEE WHERE EMPLOYEE.Super_ssn IS NULL;


SELECT Fname, Lname FROM EMPLOYEE WHERE EMPLOYEE.Super_Ssn IN ( SELECT Ssn FROM EMPLOYEE WHERE EMPLOYEE.Super_Ssn IN (SELECT Ssn FROM EMPLOYEE WHERE EMPLOYEE.Ssn='987654321' ));



SELECT Dname, Fname, Lname, Salary FROM DEPARTMENT, EMPLOYEE WHERE DEPARTMENT.Mgr_Ssn = EMPLOYEE.Ssn;



SELECT e1.Fname, (SELECT e2.Fname, e2.Lname from EMPLOYEE as e2 where e2.Ssn=e1.Super_ssn) as Manager_name, e1.Salary from EMPLOYEE as e1 where Dno=(SELECT Dnumber from DEPARTMENT where Dname="Research");



SELECT Pname, Dnum, Count(*), Sum(Hours) from WORKS_ON, PROJECT, DEPARTMENT where PROJECT.Dnum=DEPARTMENT.Dnumber and WORKS_ON.Pno=PROJECT.Pnumber GROUP BY PROJECT.Pnumber;


SELECT Pname, (SELECT Dname from DEPARTMENT where Dnumber=PROJECT.Dnum) as Dept_Name, (SELECT count(Essn) from WORKS_ON where Pno=PROJECT.Pnumber) as No_of_EMPLOYEEs, (SELECT sum(Hours) from WORKS_ON where Pno=PROJECT.Pnumber) as No_of_hours from PROJECT where (SELECT count(Essn) from WORKS_ON where Pno=PROJECT.Pnumber)>1;



SELECT fname, lname from EMPLOYEE where not exists (SELECT pnumber from PROJECT where Dnum=4 and Pnumber not in (SELECT pno from WORKS_ON where Ssn=Essn));    


SELECT Fname, Lname, Pno, Dno from EMPLOYEE, PROJECT, WORKS_ON where EMPLOYEE.Ssn=WORKS_ON.Essn and WORKS_ON.Pno=PROJECT.Pnumber and EMPLOYEE.Dno=5;


SELECT Fname, Hours, Dno, Pname, Pno from EMPLOYEE, WORKS_ON, PROJECT where EMPLOYEE.Ssn=WORKS_ON.Essn AND EMPLOYEE.Dno=5 and WORKS_ON.Hours>10 and PROJECT.Pname="ProductX" and WORKS_ON.Pno=PROJECT.Pnumber;


SELECT Fname from EMPLOYEE where Fname=any(SELECT DEPENDENT_name from DEPENDENT where Essn=EMPLOYEE.ssn);


SELECT Fname from EMPLOYEE where Super_ssn=(SELECT Ssn from EMPLOYEE where Fname="Franklin" and Lname="Wong");



SELECT Pname, (SELECT sum(Hours) from WORKS_ON where Pno=PROJECT.Pnumber) as No_of_hours from PROJECT;


SELECT avg(Salary) as Avg_Salary from EMPLOYEE where Sex="F";









