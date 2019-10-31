DELIMITER //
 
CREATE PROCEDURE usp_get_employees_salary_above(
    IN salary INT
)
BEGIN
    SELECT Fname, Lname 
     FROM EMPLOYEE
    WHERE Salary>=salary order by Fname, Lname;
END //
 
DELIMITER ;


DELIMITER //
 
CREATE PROCEDURE usp_get_towns_starting_with(
    IN prefix VARCHAR(50))
BEGIN
	SET @pattern = CONCAT(prefix,"%");
    SELECT Tname 
    FROM TOWN
    WHERE Tname like @pattern order by Tname;
END //
 
DELIMITER ;



DELIMITER //
 
CREATE FUNCTION ufn_get_salary_level(
    salary INT) RETURNS VARCHAR(10)
BEGIN
	IF (salary<30000) then
	return "Low";
	END IF;
	IF (salary<50000) then
	return "Average";
	END IF;
	return ("High");
END //
 
DELIMITER ;

