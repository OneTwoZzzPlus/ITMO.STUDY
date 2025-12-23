# Код с картинок ЛР 5

1.1

```SQL
-- Посмотрим значение до изменения
SELECT 'Before' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 101;
-- Начинаем транзакцию
BEGIN;
-- Повышаем зарплату на 10% сотруднику с ID 101
UPDATE "EmployeesDepartments". "EMPLOYEES"
SET "SALARY" = "SALARY" * 1.1
WHERE "EMPLOYEE_ID" = 101;
-- Сморим значение внутри транзакции (до коммита)
SELECT 'During' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 101;
-- Фиксация изменений
COMMIT;
-- Проверяем итоговое значение
SELECT 'After' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 101;
```

1.2

```SQL
-- Значения до изменений
SELECT 'Before' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" <= 103
ORDER BY 2;
-- Начинаем транзакцию
BEGIN;
-- Повышаем зарплату всем сотрудникам до ID 103
UPDATE "EmployeesDepartments"."EMPLOYEES"
SET "SALARY" = "SALARY" * 1.1
WHERE "EMPLOYEE_ID" <= 103;
-- Значения внутри транзакции, до отката
SELECT 'Within transaction' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" <= 103
ORDER BY 2;
-- Откат транзакции
ROLLBACK;
-- Проверяем, что изменения не сохранены
SELECT
'After' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" <= 103
ORDER BY 2;
```

1.3

```SQL
BEGIN;
SELECT 'Trans started' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 104;

-- Первая точка сохранения с именем sp1
SAVEPOINT sp1;
UPDATE "EmployeesDepartments"."EMPLOYEES"
SET "SALARY" = 3000
WHERE "EMPLOYEE_ID" = 104;

SELECT 'After SAVEP sp1' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 104;

-- Вторая точка сохранения с именем sp2
SAVEPOINT sp2;
UPDATE "EmployeesDepartments"."EMPLOYEES"
SET "SALARY" = 10000
WHERE "EMPLOYEE_ID" = 104;

SELECT 'After SAVEP sp2' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 104;

-- Откат только до второго savepoint
ROLLBACK TO SAVEPOINT sp2;

SELECT 'After ROLLB sp2' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 104;

UPDATE "EmployeesDepartments"."EMPLOYEES"
SET "SALARY" = "SALARY"+100
WHERE "EMPLOYEE_ID" = 104;

-- Фиксация полной транзакции
COMMIT;

SELECT 'After trans' AS stage, "EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "SALARY"
FROM "EmployeesDepartments"."EMPLOYEES"
WHERE "EMPLOYEE_ID" = 104;
```

2.1

```SQL
DROP TABLE IF EXISTS public.t1;

CREATE TABLE public.t1 (
    id int PRIMARY KEY,
    price numeric(10,2)
);

INSERT INTO public.t1 VALUES
(1, 10.00),
(2, 20.00),
(3, 30.00);
```

2.3

```SQL
BEGIN;

UPDATE public.t1
SET price = price + 1.00
WHERE id = 2;

SELECT 'Inside Connection 1' AS stage, id, price
FROM public.t1
WHERE id = 2;
```

2.4

```SQL
BEGIN;

SELECT id, price
FROM public.t1
WHERE id = 2;

UPDATE public.t1
SET price = 0
WHERE id = 2;

SELECT id, price
FROM public.t1
WHERE id = 2;
```

2.5

```SQL
SELECT
    pid,
    usename,
    application_name,
    state,
    wait_event_type,
    wait_event,
    query
FROM pg_stat_activity
WHERE datname = current_database()
ORDER BY pid;
```

2.6

```SQL
SELECT
    l.pid,
    a.application_name,
    a.state,
    l.locktype,
    l.relation::regclass AS locked_relation,
    l.page,
    l.tuple,
    l.virtualxid,
    l.transactionid,
    l.mode,
    l.granted
FROM pg_locks l
LEFT JOIN pg_stat_activity a ON a.pid = l.pid
WHERE a.datname = current_database()
ORDER BY l.pid, l.locktype;
```

3.1

```SQL
BEGIN;

SELECT id, price
FROM public.t1
WHERE id = 3;

UPDATE public.t1
SET price = 100
WHERE id = 3;

SELECT id, price
FROM public.t1
WHERE id = 3;
```

3.2

```SQL
BEGIN ISOLATION LEVEL READ COMMITTED;
SELECT id, price
FROM public.t1
WHERE id = 3;
```

4.1

```SQL
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT id, price
FROM public.t1
WHERE id = 3;   
```

4.2

```SQL
BEGIN;
UPDATE public.t1
SET price = 1
WHERE id = 3;
COMMIT;
```

4.3

```SQL
SELECT id, price
FROM public.t1
WHERE id = 3;
COMMIT;
```

4.4

```SQL
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT id, price
FROM public.t1
WHERE price = 1;
```

4.5

```SQL
BEGIN;
INSERT INTO public.t1
VALUES (4, 1);
COMMIT;
```

4.6

```SQL
SELECT id, price
FROM public.t1
WHERE price = 1;
COMMIT;
```

5.1

```SQL
BEGIN ISOLATION LEVEL SERIALIZABLE;

-- Обновляем строку с id = 1
UPDATE public.t1
SET price = 111
WHERE id = 1;

-- Читаем строку с id = 1
SELECT id, price
FROM public.t1
WHERE id = 1;
```

5.2

```SQL
BEGIN ISOLATION LEVEL SERIALIZABLE;
UPDATE public.t1
SET price = 222
WHERE id = 1;
COMMIT;
```