-- Script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_sum DECIMAL(10,2);
    DECLARE total_weight DECIMAL(10,2);
    DECLARE avg_weighted_score DECIMAL(10,2);

    -- Calculate the sum of all weighted scores for the user
    SELECT SUM(score * weight) INTO weighted_sum
    FROM scores
    WHERE user_id = user_id;

    -- Calculate the sum of all weights for the user
    SELECT SUM(weight) INTO total_weight
    FROM scores
    WHERE user_id = user_id;

    -- Calculate the average weighted score
    SET avg_weighted_score = weighted_sum / total_weight;

    -- Store the result in the users table or another table as needed
    UPDATE users
    SET average_weighted_score = avg_weighted_score
    WHERE id = user_id;
END$$

DELIMITER ;
