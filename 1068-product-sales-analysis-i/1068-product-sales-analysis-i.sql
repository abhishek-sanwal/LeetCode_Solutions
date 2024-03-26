# Write your MySQL query statement below

select product_name, year, price 
from sales inner join product
using(product_id);