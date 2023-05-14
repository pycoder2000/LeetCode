# Write your MySQL query statement below
select unique_id,name from Employees e LEFT JOIN EmployeeUNI em on e.id = em.id;