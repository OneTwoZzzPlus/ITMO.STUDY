--Функция сравнения зарплаты сотрудника со средним значением в его отделе
CREATE OR REPLACE FUNCTION "EmployeesDepartments".get_salary_difference(
    p_emp_id INT,
    p_percent BOOLEAN
)
RETURNS NUMERIC AS
$$
DECLARE
    v_dep_id INT;
    v_salary NUMERIC;
    v_avg NUMERIC;
BEGIN
    SELECT "DEPARTMENT_ID", "SALARY"
    INTO v_dep_id, v_salary
    FROM "EmployeesDepartments"."EMPLOYEES"
    WHERE "EMPLOYEE_ID" = p_emp_id;

    IF v_dep_id IS NULL THEN
        RETURN 0;
    END IF;

    SELECT AVG("SALARY") INTO v_avg
    FROM "EmployeesDepartments"."EMPLOYEES"
    WHERE "DEPARTMENT_ID" = v_dep_id;

    IF v_avg IS NULL THEN
        RETURN 0;
    END IF;

    IF p_percent THEN
        RETURN ROUND((v_salary - v_avg) / v_avg * 100, 2);
    ELSE
        RETURN ROUND((v_salary - v_avg), 2);
    END IF;
END;
$$ LANGUAGE plpgsql;