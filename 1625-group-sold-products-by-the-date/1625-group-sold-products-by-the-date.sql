# Write your MySQL query statement below
select sell_date, COUNT(DISTINCT product) AS num_sold, GROUP_CONCAT(DISTINCT product) AS products from Activities GROUP BY 1;