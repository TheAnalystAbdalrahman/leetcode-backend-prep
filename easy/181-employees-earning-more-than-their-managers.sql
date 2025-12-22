-- LeetCode 181: Employees Earning More Than Their Managers
-- --------------------------------------------------------
-- Goal:
-- Find employees whose salary is greater than the salary of their direct manager.
--
-- Approach:
-- Use a self-join on the Employee table:
-- - One instance represents the employee
-- - The other instance represents the manager
--
-- Key idea:
-- An employee earns more than their manager if:
-- employee.salary > manager.salary
-- and employee.managerId = manager.id

SELECT 
    e.name AS Employee
FROM Employee e
JOIN Employee m
    ON e.managerId = m.id
WHERE e.salary > m.salary;
