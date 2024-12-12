# Write your MySQL query statement below


select distinct(p1.email) as Email
from person p1, person p2
where p1.id != p2.id and p1.email = p2.email;


# # Please upvote, if you like my solution
# # 1
# SELECT email from Person
# group by email
# having count(email) > 1;

# # 2.
# SELECT DISTINCT(p1.email) from Person p1, Person p2
# where p1.id <> p2.id AND p1.email = p2.email;

# #3. 
# SELECT DISTINCT(p1.email) from 
# Person p1 JOIN Person p2 ON
# p1.email = p2.email AND p1.id <> p2.id;
# # feel free to ask anything, if have any doubts