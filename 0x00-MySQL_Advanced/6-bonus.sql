-- script for generating a saved procedure AddBonus
-- that gives a pupil an additional corrective.
DELIMITER $$ ;
CREATE PROCEDURE AddBonus(
	IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER
)
BEGIN
	IF NOT EXISTS(SELECT name FROM projects WHERE name=project_name) THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, (SELECT id from projects WHERE name=project_name), score);
END;$$
DELIMITER ;
