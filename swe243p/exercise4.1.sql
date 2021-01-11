# Problem 1
USE ap;
SELECT 
vendor_id, 
SUM(invoice_total) AS invoice_total_sum
FROM
invoices
GROUP BY vendor_id;

# Problem 2
SELECT 
vendor_name, 
SUM(payment_total) AS payment_total_sum
FROM vendors
JOIN invoices
ON invoices.vendor_id = vendors.vendor_id
GROUP BY vendor_name
ORDER BY payment_total_sum DESC;

# Problem 3
SELECT vendor_name, 
COUNT(*) AS invoice_count, 
SUM(invoice_total) AS invoice_total_sum
FROM vendors 
JOIN invoices
ON invoices.vendor_id = vendors.vendor_id
GROUP BY vendor_name
ORDER BY invoice_count DESC;

# Problem 4
SELECT account_description, 
COUNT(*) AS item_count, 
SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts g
JOIN invoice_line_items i
ON g.account_number = i.account_number
GROUP BY g.account_number
HAVING item_count > 1
ORDER BY line_item_amount_sum DESC;

# Problem 5
SELECT account_description, 
COUNT(*) AS item_count, 
SUM(line_item_amount) AS line_item_amount_sum
FROM general_ledger_accounts g
JOIN invoice_line_items il
ON g.account_number = il.account_number
JOIN invoices i
ON il.invoice_id = i.invoice_id
WHERE invoice_date BETWEEN '2018-04-01' AND '2018-06-30'
GROUP BY g.account_number
HAVING item_count > 1
ORDER BY line_item_amount_sum DESC;

# Problem 6
SELECT account_number, 
SUM(line_item_amount) AS line_item_amount_sum
FROM 
invoice_line_items
GROUP BY account_number 
WITH ROLLUP;

# Problem 7
SELECT vendor_name,
COUNT(DISTINCT li.account_number) as account_number_count
FROM vendors v
JOIN invoices i
ON v.vendor_id = i.vendor_id
JOIN invoice_line_items li
ON i.invoice_id = li.invoice_id
GROUP BY vendor_name
HAVING account_number_count > 1;

# Problem 8
# GROUPING can recognize whether a column is null or not 
# if it is null, return 1, else return 0
# IF function: IF(function, if false, if true)
# besides IF function, CASE WHEN THEN ELSE END can also work in the same way.

# WITH ROLLUP is a summary query that includes a final summary row
# Using this, you cannot use the ORDER BY clause. 
SELECT 
IF (GROUPING(terms_id) = 1, 'Grand Total', terms_id) AS terms_id,
IF (GROUPING(vendor_id) = 1, 'Terms ID Totals', vendor_id) AS vendor_id,
MAX(payment_date) AS last_payment_date, 
SUM(invoice_total - credit_total - payment_total) AS sum_balance_due
FROM invoices i
GROUP BY terms_id, vendor_id WITH ROLLUP;

