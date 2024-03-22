-- script that builds the idx_name_first_score index on
-- the table names the name initial letter and the score.
CREATE INDEX idx_name_first_score on names(name(1), score)
