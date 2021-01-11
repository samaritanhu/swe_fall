--  Problem 1
INSERT INTO terms
(terms_id, terms_description, terms_due_days)
VALUES
(6, "Net due 120 days", 120);

# see the results by this line
# select * from terms;

--  Problem 2
UPDATE terms 
SET terms_description = "Net due 125 days", terms_due_days = 125
WHERE terms_id = 6;

--  Problem 3
DELETE FROM terms WHERE terms_id = 6;

--  Problem 4
INSERT INTO invoices
(vendor_id, invoice_number, invoice_date, invoice_total, 
payment_total, credit_total, terms_id, invoice_due_date)
VALUES
(32, "AX-014-027", "2018-08-01", 434.58, 0,
0, 2, "2018-08-31");
--  check the results by this line
SELECT * FROM invoices;

--  Problem 5
INSERT INTO invoice_line_items
(invoice_id, invoice_sequence, account_number, line_item_amount, line_item_description)
VALUES
(115, 1, 160, 180.23, "Hard drive"),
(115, 2, 527, 254.35, "Exchange Server update");

SELECT * FROM invoice_line_items;

--  Problem 6
UPDATE invoices
SET credit_total = 0.1 * invoice_total, payment_total = invoice_total - credit_total
WHERE invoice_id = 115;

--  Problem 7
UPDATE vendors
SET default_account_number = 403
WHERE vendor_id = 44;
--  check the results by this line
SELECT * FROM vendors WHERE vendor_id = 44;

--  Problem 8
UPDATE inovices
SET terms_id = 2
WHERE terms_id in 
(
SELECT terms_id 
FROM invoices
WHERE default_terms_id = 2);

-- Problem 9
DELETE FROM invoice_line_items
WHERE invoice_id = 115;
DELETE FROM invoices 
WHERE invoice_id = 115;