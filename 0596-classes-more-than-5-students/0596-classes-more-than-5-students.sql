select class from Courses group by class having COUNT(DISTINCT student) >= 5 