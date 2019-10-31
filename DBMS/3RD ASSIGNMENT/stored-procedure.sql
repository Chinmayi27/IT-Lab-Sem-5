drop procedure list_dept_employees;

Delimiter //
create procedure list_dept_employees(dept VARCHAR(50), INOUT employeeList varchar(4000))
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE employee varchar(100) DEFAULT "";

	DECLARE currEmployee cursor FOR select Name from EMPLOYEE where EMPLOYEE.Dept=dept;

	DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished=1;

	OPEN currEmployee;
	getEmployee: LOOP
        FETCH currEmployee INTO employee;
        IF finished = 1 THEN 
            LEAVE getEmployee;
        END IF;
        
        SET employeeList = CONCAT(employee,", ",employeeList);
    END LOOP getEmployee;
    CLOSE currEmployee;
 
END //
Delimiter ;


SET @employeeList = ""; 
CALL list_dept_employees("HR",@employeeList); 
SELECT @employeeList;