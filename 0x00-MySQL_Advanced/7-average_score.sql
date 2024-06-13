-- Write a SQL script that creates a stored
-- procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student.
-- Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN input_user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(8, 2) DEFAULT 0.0;
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = input_user_id;
    UPDATE users SET average_score = avg_score WHERE id = input_user_id;
END $$
DELIMITER ;
