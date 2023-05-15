# Write your MySQL query statement below
select w.id AS Id from Weather w, Weather w_old where w_old.recordDate = DATE_SUB(w.recordDate, interval 1 day) and w.temperature > w_old.temperature;