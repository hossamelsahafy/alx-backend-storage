-- Script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_score FLOAT;

    -- Calculate the sum of weighted scores and total weight for the given user
    SELECT SUM(c.score * p.weight) INTO total_score,
           SUM(p.weight) INTO total_weight
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the weighted average score
    SET weighted_score = total_score / total_weight;

    -- Update the average_score in the users table
    UPDATE users
    SET average_score = weighted_score
    WHERE id = user_id;
END$$

DELIMITER ;
