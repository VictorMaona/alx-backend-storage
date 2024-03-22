-- Script that establishes idx_name_first index on
-- the names of the tables and the name initial letter.
CREATE INDEX idx_name_first ON names(name(1))
