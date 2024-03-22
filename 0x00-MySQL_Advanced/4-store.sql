-- script that establishes a stopping point for
-- amount of a product once a new order is added.
CREATE TRIGGER decrease_q AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name=NEW.item_name;
