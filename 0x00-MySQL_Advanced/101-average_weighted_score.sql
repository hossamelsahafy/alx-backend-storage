--  script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store
-- the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS User, 
        (SELECT User.id, SUM(score * weight) / SUM(weight) AS w_avg 
        FROM users AS User 
        JOIN corrections as Corr ON User.id = Corr.user_id 
        JOIN projects AS Pro ON Corr.project_id = Pro.id 
        GROUP BY User.id)
    AS WA
    SET User.average_score = WA.w_avg 
    WHERE User.id=WA.id;
END
$$
DELIMITER ;
