-- SQL script that creates a view that lists all students
-- that have score under 80

CREATE VIEW need_meeting AS SELECT name FROM students 
WHERE students.score < 80 AND (ISNULL(students.last_meeting) OR DATEDIFF(CURDATE(), students.last_meeting) > 30)
