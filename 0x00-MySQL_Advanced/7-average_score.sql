-- SQL script that creates a stored procedure that computes and
-- stores the average score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    SELECT AVG(score) INTO average_score FROM corrections WHERE corrections.user_id = user_id;
    UPDATE users SET users.average_score = average_score WHERE users.id = user_id;
END;
$$
