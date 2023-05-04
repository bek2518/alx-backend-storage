-- SQL script that creates a stored procedure computes and
-- store the average weighted score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
    INTO average_score FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;
    UPDATE users SET users.average_score = average_score WHERE users.id = user_id;
END;
$$
