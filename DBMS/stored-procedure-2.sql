Delimiter //

create procedure update_salary()
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE employeeDesignation varchar(100) DEFAULT "";

	DECLARE currEmployee cursor FOR select Designation from EMPLOYEE FOR UPDATE;

	DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished=1;

	OPEN currEmployee;
	updateEmployee: LOOP
        FETCH currEmployee INTO employeeDesignation;
        IF finished = 1 THEN 
            LEAVE updateEmployee;
        END IF;
        
        IF (@employeeDesignation=="Manager") THEN
            SET Salary = 20000;
        END IF;

        IF (@employeeDesignation=="Trainer") THEN
            SET Salary = Salary+30000;
        END IF;
    END LOOP updateEmployee;
    CLOSE currEmployee;
 
END //
Delimiter ;