-- SQL script that creates a stored procedure AddBonus that
-- adds a new correction for a student

DELIMITER $$
CREATE PROCEDURE AddBonus (IN user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    DECLARE project_id_var INT;

    IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
		INSERT INTO projects(name) VALUES(project_name);
	END IF;

    SELECT projects.id INTO project_id_var FROM projects WHERE name = project_name;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id_var, score);
END;
$$
