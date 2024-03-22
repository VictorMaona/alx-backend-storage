-- script that generates a list of all students in a view called need_meeting
-- that are less than 80 (strict) and haven not had meeting in more than month.
CREATE VIEW need_meeting AS SELECT name from students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
