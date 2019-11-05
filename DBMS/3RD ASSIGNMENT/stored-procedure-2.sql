drop procedure update_salary; 

Delimiter //

create procedure update_salary()
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE employeeId INTEGER DEFAULT -1;

    DECLARE employeeDesignation VARCHAR(100) DEFAULT "";
    DECLARE employeeSalary INTEGER DEFAULT 1;

	DECLARE currEmployee cursor FOR select Id from EMPLOYEE FOR UPDATE;

	DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished=1;

	OPEN currEmployee;
	updateEmployee: LOOP
        FETCH currEmployee INTO employeeId;
        IF finished = 1 THEN 
            LEAVE updateEmployee;
        END IF;
        
        select EMPLOYEE.Salary into employeeSalary from EMPLOYEE where EMPLOYEE.Id=employeeId;
        select EMPLOYEE.Designation into employeeDesignation from EMPLOYEE where EMPLOYEE.Id=employeeId;

        IF employeeDesignation="Manager" THEN
            UPDATE EMPLOYEE set EMPLOYEE.Salary=EMPLOYEE.Salary+2000 where EMPLOYEE.Id=employeeId;
        END IF;

        IF employeeDesignation="Trainer" THEN
            UPDATE EMPLOYEE set EMPLOYEE.Salary=EMPLOYEE.Salary+3000 where EMPLOYEE.Id=employeeId;
        END IF;

        
    END LOOP updateEmployee;
    CLOSE currEmployee;
 
END //
Delimiter ;

CALL update_salary();
select * from EMPLOYEE;