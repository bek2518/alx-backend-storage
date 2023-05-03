-- SQL script that creates a trigger that decreses the quantity
-- of an item after adding a new order

CREATE TRIGGER decrease_quantity  AFTER INSERT ON orders
FOR EACH ROW SET items.quantity = OLD.quantity - orders.number
