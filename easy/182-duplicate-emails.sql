-- LeetCode 182: Duplicate Emails
-- --------------------------------
-- Goal:
-- Find all email addresses that appear more than once in the Person table.
--
-- Approach:
-- 1. Group records by email
-- 2. Count how many times each email appears
-- 3. Use HAVING to filter only emails with count > 1
--
-- Note:
-- HAVING is used instead of WHERE because COUNT(*) is an aggregate function.

SELECT 
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;