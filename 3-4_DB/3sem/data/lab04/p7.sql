CREATE OR REPLACE PROCEDURE "EmployeesDepartments".raise_salaries(
    p_id INT,
    p_is_man BOOLEAN
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_is_man THEN
        UPDATE "EmployeesDepartments"."EMPLOYEES"
        SET "SALARY" = "SALARY" + 1000
        WHERE "MANAGER_ID" = p_id;

    ELSE
        UPDATE "EmployeesDepartments"."EMPLOYEES"
        SET "SALARY" = "SALARY" + 2000
        WHERE "DEPARTMENT_ID" = p_id;
    END IF;
END;
$$;
