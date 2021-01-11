# Problem 1
SELECT vendor_name 
FROM vendors 
WHERE vendor_id IN 
(SELECT DISTINCT vendor_id FROM invoices)
ORDER BY vendor_name; 

# Problem 2
SELECT count(*), invoice_number,
invoice_total
FROM invoices
WHERE payment_total >
(SELECT AVG(payment_total) FROM invoices
WHERE payment_total > 0);

# Problem 3
SELECT account_number,
account_description
FROM general_ledger_accounts gl
WHERE NOT EXISTS
(SELECT * FROM invoice_line_items ili
WHERE gl.account_number = ili.account_number)
ORDER BY account_number;

# Problem 4
SELECT v.vendor_name, 
i.invoice_id, 
ili.invoice_sequence, 
ili.line_item_amount
FROM 
vendors v 
JOIN invoices i
ON i.vendor_id = v.vendor_id
JOIN invoice_line_items ili
ON i.invoice_id = ili.invoice_id
WHERE i.invoice_id in 
(SELECT DISTINCT invoice_id FROM invoice_line_items WHERE invoice_sequence > 1)
ORDER BY vendor_name, invoice_id, invoice_sequence;

# Problem 5
SELECT a.largest_unpaid_invoice
FROM  (
SELECT vendor_id, MAX(invoice_total) AS largest_unpaid_invoice
FROM invoices 
WHERE invoice_total - credit_total - payment_total > 0
GROUP BY vendor_id
) a;

# Problem 6
SELECT vendor_name, 
vendor_city, 
vendor_state
FROM 
vendors
WHERE CONCAT(vendor_state, vendor_city) NOT IN 
(SELECT CONCAT(vendor_state, vendor_city) AS CONCAT_VV
FROM vendors
GROUP BY CONCAT_VV
HAVING COUNT(CONCAT_VV) > 1)
ORDER BY vendor_state, vendor_city;

# Problem 7
SELECT vendor_name, 
invoice_number,
invoice_date,
invoice_total
FROM 
invoices i
JOIN vendors v
ON v.vendor_id = i.vendor_id
WHERE CONCAT(v.vendor_id, invoice_date) IN (
SELECT CONCAT(vendor_id, MIN(invoice_date)) FROM invoices 
GROUP BY vendor_id
)
ORDER BY vendor_name;

