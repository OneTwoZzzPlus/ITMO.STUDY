1.1 Напишите запрос для вывода фамилии, имени, названия отдела для всех работников, в фамилии которых есть букву «u» (в строчном регистре). 

INNER JOIN, потому что выбираем только тех сотрудников, у которых есть отдел 
```SQL
SELECT e."FIRST_NAME", e."LAST_NAME", d."DEPARTMENT_NAME"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."DEPARTMENTS" as d
ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
WHERE e."LAST_NAME" LIKE '%u%';
```

1.2 Напишите запрос для вывода имени, фамилии, названия должности и названия отдела для всех работников. Отсортируйте результат по идентификатору работника.

INNER JOIN, потому что выбираются только сотрудники, у которых есть должность и отдел
```SQL
SELECT e."FIRST_NAME", e."LAST_NAME", j."JOB_TITLE", d."DEPARTMENT_NAME"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."DEPARTMENTS" as d 
ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
JOIN "EmployeesDepartments"."JOBS" as j 
ON e."JOB_ID" = j."JOB_ID"
ORDER BY e."EMPLOYEE_ID";
```

1.3 Напишите запрос для вывода названия отдела, фамилии и имени сотрудника для всех сотрудников, у которых есть бонус, работающих в 80-ом и 85-ом отделах. Полученный результат отсортируйте по номеру отдела, размеру бонуса по убыванию, а затем фамилии.

INNER JOIN, так как все необходимые данные есть в обеих таблицах
```SQL
SELECT d."DEPARTMENT_NAME", e."LAST_NAME", e."FIRST_NAME"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."DEPARTMENTS" as d 
ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
JOIN "EmployeesDepartments"."JOBS" as j 
ON e."JOB_ID" = j."JOB_ID"
WHERE e."BONUS" IS NOT NULL AND e."DEPARTMENT_ID" IN (80, 85)
ORDER BY e."DEPARTMENT_ID", e."BONUS" DESC, e."LAST_NAME";
```

1.4 Напишите запрос для вывода фамилии, имени, названия страны и региона для всех работников, работающих в Северной Америке. Отсортируйте результат по названию страны и фамилии сотрудника. 

INNER JOIN, так как нужны только сотрудники, работающие в Северной Америке
```SQL
SELECT e."LAST_NAME", e."FIRST_NAME", c."COUNTRY_NAME", r."REGION_NAME"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."DEPARTMENTS" as d ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
JOIN "EmployeesDepartments"."LOCATIONS" as l ON d."LOCATION_ID" = l."LOCATION_ID"
JOIN "Countries"."COUNTRIES" as c ON l."COUNTRY_ID" = c."COUNTRY_ID"
JOIN "Countries"."REGIONS" as r ON c."REGION_ID" = r."REGION_ID"
WHERE r."REGION_ID" = 21
ORDER BY c."COUNTRY_NAME", e."LAST_NAME";
```

1.5 Напишите запрос для вывода фамилии и идентификатора работника, а также фамилии и идентификатора его начальника. Назовите столбцы результата «Подчиненный», «Идентификатор работника», «Руководитель», «Идентификатор руководителя». Отсортируйте результат по идентификатору руководителя по возрастанию и по идентификатору работника по убыванию. 

INNER JOIN, потому что нужно включить сотрудников, имеющих начальника
```SQL
SELECT 
	e."LAST_NAME" as "Подчиненный", 
	e."EMPLOYEE_ID" as "Идентификатор работника", 
	m."LAST_NAME" as "Руководитель", 
	m."EMPLOYEE_ID" as "Идентификатор руководителя"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."EMPLOYEES" as m
ON e."MANAGER_ID" = m."EMPLOYEE_ID"
ORDER BY m."EMPLOYEE_ID" ASC, e."EMPLOYEE_ID" DESC;
```

1.6 Измените запрос из пункта 1.5. таким образом, чтобы получить фамилии всех работников в столбце «Подчиненный», включая Кинга, который не имеет руководителя. Отсортируйте результат по идентификатору подчиненного, 

LEFT JOIN, потому что нужно включить вообще всех сотрудников
```SQL
SELECT 
	e."LAST_NAME" as "Подчиненный", 
	e."EMPLOYEE_ID" as "Идентификатор работника", 
	m."LAST_NAME" as "Руководитель", 
	m."EMPLOYEE_ID" as "Идентификатор руководителя"
FROM "EmployeesDepartments"."EMPLOYEES" as e
LEFT JOIN "EmployeesDepartments"."EMPLOYEES" as m
ON e."MANAGER_ID" = m."EMPLOYEE_ID"
ORDER BY e."EMPLOYEE_ID" ASC;
```

1.7 Напишите запрос для вывода названия отдела, фамилии сотрудника и фамилий всех его коллег для сотрудников Fay, Hartstein и Davies. Назовите столбцы результата «Отдел», «Работник», «Коллеги». Отсортируйте результат по отделу и фамилии сотрудника. 

INNER JOIN, так как нужны только существующие сотрудники и их отделы

+GROUP BY для STRING_AGG

```SQL
SELECT 
	d."DEPARTMENT_NAME" as "Отдел",
	e."LAST_NAME" as "Работник",
	STRING_AGG(c."LAST_NAME", ', ') as "Коллеги"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."EMPLOYEES" as c
ON e."DEPARTMENT_ID" = c."DEPARTMENT_ID"
JOIN "EmployeesDepartments"."DEPARTMENTS" as d
ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
WHERE e."LAST_NAME" IN ('Fay', 'Hartstein', 'Davies')
	AND e."LAST_NAME" != c."LAST_NAME"
GROUP BY d."DEPARTMENT_NAME", e."LAST_NAME"
ORDER BY d."DEPARTMENT_NAME", e."LAST_NAME";
```

1.8 Напишите запрос для вывода всех категорий работников (GRADE_LEVEL), их фамилий, размеров оклада, названий должностей и названий отделов. Если в некоторой категории нет работников, то эта категория всё равно должна присутствовать в результате. Отсортируйте результат по категории работника, отделу и фамилии. 

LEFT JOIN гарантирует, что категории без работников тоже попадут в результат.

```SQL
SELECT g."GRADE_LEVEL", e."LAST_NAME", e."SALARY", j."JOB_TITLE", d."DEPARTMENT_NAME"
FROM "EmployeesDepartments"."JOB_GRADES" as g
LEFT JOIN "EmployeesDepartments"."EMPLOYEES" as e
	ON e."SALARY" BETWEEN g."LOWEST_SAL" AND g."HIGHEST_SAL"
LEFT JOIN "EmployeesDepartments"."JOBS" as j
	ON e."JOB_ID" = j."JOB_ID"
LEFT JOIN "EmployeesDepartments"."DEPARTMENTS" as d
	ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
ORDER BY g."GRADE_LEVEL", d."DEPARTMENT_NAME", e."LAST_NAME";
```

1.9 Напишите запрос для вывода фамилий и дат найма всех сотрудников, а также фамилий и дат найма их руководителей, для всех сотрудников, руководители которых устроились на работу в 2008ом году, но при это сами подчиненные устроились на работу до 2008 года. 

Проверка года у начальника поставлена в ON, чтобы выполняться во время присоединения, хотя для INNER JOIN это не играет роли, но, например, при LEFT JOIN это работало бы быстрее.

INNER JOIN обеспечит только существующие пары сотрудник-менеджер.
```SQL
SELECT e."LAST_NAME", e."HIRE_DATE", m."LAST_NAME", m."HIRE_DATE"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."EMPLOYEES" as m
ON e."MANAGER_ID" = m."EMPLOYEE_ID" 
	AND EXTRACT(year FROM m."HIRE_DATE") = 2008
WHERE EXTRACT(year FROM e."HIRE_DATE") < 2008; 
```

1.10 Для всех работников, менеджеры которых устроились на работу в январе, и длина названий должностей этих работников(подчиненных) более 15ти символов, сформируйте запрос для вывода названия должности, фамилии работника, даты найма, фамилии руководителя и его даты найма. Результат отсортировать по названию должности, фамилии руководителя, идентификатору работника. 

INNER JOIN обеспечит только существующие пары сотрудник-менеджер и их должности.

```SQL
SELECT 
	j."JOB_TITLE" as "Должность", 
	e."LAST_NAME" as "Работник", 
	e."HIRE_DATE" as "Дата найма работника", 
	m."LAST_NAME" as "Начальник", 
	m."HIRE_DATE" as "Дата найма начальника"
FROM "EmployeesDepartments"."EMPLOYEES" as e
JOIN "EmployeesDepartments"."EMPLOYEES" as m
	ON e."MANAGER_ID" = m."EMPLOYEE_ID"
	AND EXTRACT(month FROM m."HIRE_DATE") = 1
JOIN "EmployeesDepartments"."JOBS" as j
	ON e."JOB_ID" = j."JOB_ID"
WHERE LENGTH(j."JOB_TITLE") > 15
ORDER BY j."JOB_TITLE", m."LAST_NAME", e."EMPLOYEE_ID";
```

1.11 Напишите запрос для вывода идентификатора отдела и его названия для всех отделов, в которых нет работников. 

LEFT JOIN гарантирует все отделы, а IS NULL оставит только пустые.

```SQL
SELECT d."DEPARTMENT_ID", d."DEPARTMENT_NAME"
FROM "EmployeesDepartments"."DEPARTMENTS" as d
LEFT JOIN "EmployeesDepartments"."EMPLOYEES" as e
	ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
WHERE e."DEPARTMENT_ID" IS NULL;
```

2.1 Напишите запрос для вывода идентификатора отдела, количества работников в нём, минимальной, максимальной и средней заработной платы по отделу, а также дат первого и последнего приёма в отдел. Для всех столбцов результата задайте понятные наименования и отсортируйте результат по количеству сотрудников (по убыванию). 

```SQL
SELECT 
	d."DEPARTMENT_ID" AS "Отдел",
    COUNT(e."EMPLOYEE_ID") AS "Количество сотрудников",
    MIN(e."SALARY") AS "Минимальная зарплата",
    MAX(e."SALARY") AS "Максимальная зарплата",
    ROUND(AVG(e."SALARY"), 2) AS "Средняя зарплата",
    MIN(e."HIRE_DATE") AS "Первая дата найма",
    MAX(e."HIRE_DATE") AS "Последняя дата найма"
FROM "EmployeesDepartments"."DEPARTMENTS" as d
JOIN "EmployeesDepartments"."EMPLOYEES" as e
	ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
GROUP BY d."DEPARTMENT_ID"
ORDER BY COUNT(e."EMPLOYEE_ID") DESC;
```

2.2 Напишите запрос для вывода названия должности, самого низкого, самого высокого и среднего оклада по ней, а также суммы окладов по каждой должности. Отсортируйте результат по названию должности.

```SQL
SELECT 
	j."JOB_TITLE" AS "Должность",
    MIN(e."SALARY") AS "Минимальный оклад",
    MAX(e."SALARY") AS "Максимальный оклад",
    ROUND(AVG(e."SALARY"), 2) AS "Средний оклад",
    SUM(e."SALARY") AS "Сумма окладов"
FROM "EmployeesDepartments"."JOBS" as j
JOIN "EmployeesDepartments"."EMPLOYEES" as e
	ON e."JOB_ID" = j."JOB_ID"
GROUP BY j."JOB_TITLE"
ORDER BY j."JOB_TITLE";
```

2.3 Напишите запрос, который позволяет получить список отделов (идентификаторов отделов), их наименований и округленную среднюю заработную плату работников в каждом из них. Для всех столбцов результата задайте понятные наименования, отсортируйте по округленной средней заработной плате.

```SQL
SELECT 
	d."DEPARTMENT_ID" AS "ID отдела",
    d."DEPARTMENT_NAME" AS "Отдел",
    ROUND(AVG(e."SALARY"), 2) AS "Средняя зарплата"
FROM "EmployeesDepartments"."DEPARTMENTS" as d
JOIN "EmployeesDepartments"."EMPLOYEES" as e
	ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
GROUP BY d."DEPARTMENT_ID", d."DEPARTMENT_NAME"
ORDER BY "Средняя зарплата";
```

2.4 Напишите запрос, который позволяет получить список руководителей (их имя, фамилию, должность), у которых количество подчиненных больше 5 и сумма всех зарплат его подчиненных больше 50000. 

```SQL
SELECT m."FIRST_NAME", m."LAST_NAME", j."JOB_TITLE"
FROM "EmployeesDepartments"."EMPLOYEES" AS m
JOIN "EmployeesDepartments"."JOBS" AS j 
	ON j."JOB_ID" = m."JOB_ID"
JOIN "EmployeesDepartments"."EMPLOYEES" AS e 
	ON e."MANAGER_ID" = m."EMPLOYEE_ID"
GROUP BY m."FIRST_NAME", m."LAST_NAME", j."JOB_TITLE"
HAVING COUNT(e."EMPLOYEE_ID") > 5 AND SUM(e."SALARY") > 50000;
```

2.5 Напишите запрос для вывода идентификатора отдела и разности между самым высоким и самым низким окладами по каждому отделу. Результат отсортируйте по убыванию разности окладов.

```SQL
SELECT 
	d."DEPARTMENT_ID" AS "Отдел",
    MAX(e."SALARY") - MIN(e."SALARY") AS "Разность окладов"
FROM "EmployeesDepartments"."DEPARTMENTS" as d
JOIN "EmployeesDepartments"."EMPLOYEES" as e
	ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
GROUP BY d."DEPARTMENT_ID"
ORDER BY "Разность окладов" DESC;
```

2.6 Напишите запрос для вывода идентификатора каждого руководителя, имеющего подчинённых, и средней заработной платы этих подчинённых, но только для тех руководителей, которые не получают бонусов, и у которых средняя заработная плата подчинённых находится в диапазоне от 6000 до 9000. Отсортируйте результат по идентификатору руководителя.

```SQL
SELECT m."EMPLOYEE_ID", AVG(e."SALARY")
FROM "EmployeesDepartments"."EMPLOYEES" AS m
JOIN "EmployeesDepartments"."EMPLOYEES" AS e
	ON e."MANAGER_ID" = m."EMPLOYEE_ID"
WHERE m."BONUS" IS NULL
GROUP BY m."EMPLOYEE_ID"
HAVING AVG(e."SALARY") BETWEEN 6000 AND 9000
ORDER BY m."EMPLOYEE_ID";
```

2.7 Напишите запрос для вывода названия отдела, местоположения отдела (город, адрес) и количества служащих в нём, но только для тех отделов, в которых работники занимают различные должности. Для всех столбцов результата задайте понятные наименования и отсортируйте результат по количеству служащих (по убыванию).

```SQL
SELECT 
	d."DEPARTMENT_NAME" AS "Отдел", 
	l."CITY" AS "Город", 
	l."STREET_ADDRESS" AS "Адрес",
	COUNT(e."EMPLOYEE_ID") AS "Количество сотрудников"
FROM "EmployeesDepartments"."DEPARTMENTS" AS d
JOIN "EmployeesDepartments"."LOCATIONS" AS l ON l."LOCATION_ID" = d."LOCATION_ID"
JOIN "EmployeesDepartments"."EMPLOYEES" AS e ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
GROUP BY d."DEPARTMENT_NAME", l."CITY", l."STREET_ADDRESS"
HAVING COUNT(DISTINCT e."JOB_ID") > 1
ORDER BY COUNT(e."EMPLOYEE_ID") DESC;
```

2.8 Напишите запрос для вывода года и количества принятых на работу сотрудников в указанном году по всем годам. Результат отсортировать по количеству принятых на работу сотрудников в год.

```SQL
SELECT 
	EXTRACT(year FROM "HIRE_DATE") AS "Год",
	COUNT("EMPLOYEE_ID") AS "Количество сотрудников"
FROM "EmployeesDepartments"."EMPLOYEES"
GROUP BY EXTRACT(year FROM "HIRE_DATE")
ORDER BY COUNT("EMPLOYEE_ID");
```

2.9 Напишите запрос, который выводит длину имени и количество сотрудников с соответствующей длиной имени. В результат включите только тех сотрудников, у которых длина имени больше 5, а количество сотрудников с такой длиной — больше 3. Результат отсортируйте по длине имени.

```SQL
SELECT 
	LENGTH("FIRST_NAME") AS "Длина имени",
	COUNT("EMPLOYEE_ID") AS "Количество сотрудников"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE LENGTH("FIRST_NAME") > 5
GROUP BY "Длина имени"
HAVING COUNT("EMPLOYEE_ID") > 3
ORDER BY "Длина имени";
```

2.10 Напишите запрос, который выводит названия отделов, их идентификационный номер, адрес и город, а также количество работников в каждом отделе, включая те, где пока нет ни одного работника. Укажите, какой тип соединения таблиц используется в данном запросе. Для всех столбцов результата задайте понятные наименования, отсортируйте по номеру отдела.

```SQL
SELECT 
	d."DEPARTMENT_NAME" AS "Отдел",
	d."DEPARTMENT_ID" AS "ID отдела",
	l."STREET_ADDRESS" AS "Адрес",
	l."CITY" AS "Город",
	COUNT(e."EMPLOYEE_ID") AS "Количество сотрудников"
FROM "EmployeesDepartments"."DEPARTMENTS" AS d
JOIN "EmployeesDepartments"."LOCATIONS" AS l
	ON d."LOCATION_ID" = l."LOCATION_ID"
LEFT JOIN "EmployeesDepartments"."EMPLOYEES" AS e
	ON d."DEPARTMENT_ID" = e."DEPARTMENT_ID"
GROUP BY d."DEPARTMENT_NAME", d."DEPARTMENT_ID",
	l."STREET_ADDRESS",	l."CITY"
ORDER BY d."DEPARTMENT_ID";
```

2.11 Напишите запрос, который выводит название должности, количество работников, занимающих эту должность, а также среднюю заработную плату по каждой должности в отделах Administration и IT. В результат включите только те должности, где средняя зарплата превышает 4000, и на которых работает более двух сотрудников. Для всех столбцов результата задайте понятные наименования, отсортируйте данные по убыванию количества сотрудников.

```SQL
SELECT 
	j."JOB_TITLE" AS "Должность",
	COUNT(e."EMPLOYEE_ID") AS "Количество работников",
	ROUND(AVG(e."SALARY"), 2) AS "Средняя зарплата"
FROM "EmployeesDepartments"."JOBS" AS j
JOIN "EmployeesDepartments"."EMPLOYEES" AS e
	ON e."JOB_ID" = j."JOB_ID"
JOIN "EmployeesDepartments"."DEPARTMENTS" AS d
	ON e."DEPARTMENT_ID" = d."DEPARTMENT_ID"
WHERE d."DEPARTMENT_NAME" IN ('Administration', 'IT')
GROUP BY j."JOB_TITLE"
HAVING AVG(e."SALARY") > 4000 AND COUNT(e."EMPLOYEE_ID") > 2
ORDER BY COUNT(e."EMPLOYEE_ID") DESC;
```

ПРОБЛЕМЫ и ЗНАНИЯ
- Двойные кавычки в алиасах в 1.5
- При совмещении нескольких соединений любой INNER JOIN убирает эффект от LEFT и RIGHT JOIN в 1.8
- Понять, что значит "различные должности" в 2.7

