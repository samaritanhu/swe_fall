# Problem 1
# I used inner join, using key equlas vendor id to join vendors table and invoices table together
# I used count(*) function to calculate the number of rows, which equals 114. 
select *
from vendors v
inner join invoices i 
on v.vendor_id = i.vendor_id;

# Problem 2
# I used count(*) function to calculate the number of rows, which equals 11. 
select vendor_name,
invoice_number,
invoice_date,
invoice_total - payment_total - credit_total as balance_due
from vendors v
inner join invoices i
on v.vendor_id = i.vendor_id
where invoice_total - payment_total - credit_total <> 0
order by v.vendor_name;

# Problem 3
# I used count(*) function to calculate the number of rows, which equals 122. 
select vendor_name, 
default_account_number,
account_description as "description"
from vendors v
inner join general_ledger_accounts g
on v.default_account_number = g.account_number
order by account_description, vendor_name;

# Problem 4
# I used count(*) function to calculate the number of rows, which equals 118. 
select vendor_name,
invoice_date,
invoice_number,
invoice_sequence as li_sequence,
line_item_amount as li_amount
from vendors v
inner join invoices i
on v.vendor_id = i.vendor_id
inner join invoice_line_items li
on li.invoice_id = i.invoice_id
order by vendor_name, invoice_date, invoice_number, invoice_sequence;

# Problem 5
# I used count(*) function to calculate the number of rows, which equals 2. 
select v1.vendor_id, 
v1.vendor_name, 
concat(v1.vendor_contact_first_name, ' ', v1.vendor_contact_last_name) as contact_name
from vendors v1 join vendors v2
on v1.vendor_id <> v2.vendor_id
and v1.vendor_contact_last_name = v2.vendor_contact_last_name;

# Problem 6
# I used count(*) function to calculate the number of rows, which equals 54. 
select 
gl.account_number,
account_description
from 
general_ledger_accounts gl
left join invoice_line_items li
on gl.account_number = li.account_number
where invoice_id is null
order by gl.account_number;

# Problem 7
select vendor_name, vendor_state
from vendors
where vendor_state='CA'
union 
select vendor_name, "Outside CA" as vendor_state
from vendors
where vendor_state <> 'CA'
order by vendor_name;
