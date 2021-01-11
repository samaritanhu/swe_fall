# Problem 8
# select vendor_name, vendor_contact_last_name, vendor_contact_first_name
# and add an ORDER BY set by last name and then first name,asendingly.
# Here I used select from, and used order by last name and then first name
select vendor_name, vendor_contact_last_name, vendor_contact_first_name
from vendors
order by vendor_contact_last_name, vendor_contact_first_name;

# Problem 9
# I formatted this full_name column with the last name, a comma, a space, and the first name
# and used LEFT function to sort out whose last name begins with the letter A, B, C, or E. 
# I used count(*) function to calculate the number of rows, which equals 41. 
select concat(vendor_contact_last_name, ', ', vendor_contact_first_name) as full_name
from vendors
where left(vendor_contact_last_name, 1) in ('A', 'B', 'C', 'E')
order by vendor_contact_last_name, vendor_contact_first_name;

# Problem 10
# I enclosed the alias in quotes because there was one blank space between plus and 10%
# I used arthimetic functions to calculate 10% and Plus 10%
# and WHERE function to sort out an invoice total that's greater than or equal to 500
# and less than or equal to 1000. 
# I used ORDER BY DESC to sort the result set in descending sequence by invoice_due_date. 
# I used count(*) function to calculate the number of rows, which equals 12. 
select invoice_due_date, invoice_total,
0.1 * invoice_total as '10%',
invoice_total + 0.1 as 'Plus 10%'
from invoices
where invoice_total >= 500 and invoice_total <= 1000
order by invoice_due_date desc;

# Problem 11
# I used WHERE to sort out invoices that have a balance due that's greater than $50. 
# I used ORDER BY DESC to sort the result set by balance due in descending sequence. 
# I used the LIMIT clause so the result set contains only the rows with the 5 largest balances. 
select invoice_number, invoice_total, 
payment_total + credit_total as payment_credit_total, 
invoice_total - payment_total - credit_total as balence_due 
from invoices
where invoice_total - payment_total - credit_total > 50
order by invoice_total - payment_total - credit_total desc
limit 5;

# Problem 12
# I used "is null" to return only the rows where the payment_date column contains a null value. 
# I used count(*) function to calculate the number of rows, which equals 11. 
select invoice_number, invoice_date, 
invoice_total - payment_total - credit_total as balence_due,
payment_date
from invoices
where payment_date is null;

# Problem 13
# I used convert clause to transfer date into string, then I used LEFT and RIGHT clause to get mm-dd and yyyy. 
# At last, I used concat to join these strings together 
select concat(convert(right(current_date(), 5),char), "-" , convert(left(current_date(), 4),char)) as "current_date";

# Problem 14
# Simply using as clause to write a SELECT statement without a FROM clause 
select 50000 as starting_principal, 
round(.065*50000,2) as interest, 
50000 + round(.065*50000,2) as principalplus_interest
