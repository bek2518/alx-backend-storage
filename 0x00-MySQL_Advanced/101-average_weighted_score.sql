-- SQL script that creates a stored procedure that computes and
-- store the average weighted score of all students

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE average_score FLOAT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
        INTO average_score FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
        UPDATE users SET users.average_score = average_score WHERE users.id = user_id;
    
    END LOOP;
    CLOSE cur;
END;
$$
