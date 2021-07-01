# Count of customers w.r.t the status of their credit card
q1 = "select CC_STATUS,count(*) as countofc from customers GROUP BY CC_STATUS"

# Age and Income of customers
q2 = "select timestampdiff(YEAR,DOB,curdate()) as age, INCOME from customers"

# Age and Average of Income
q3 = "select timestampdiff(YEAR,DOB,curdate()) as age, avg(INCOME) as INCOME from customers group by age"

# Income Type
q4="select INCOME_TYPE,count(*) as countofc from customers group by INCOME_TYPE"

q5="select count(*) as hascar from customers where CAR='Y'"
q6="select count(*) as hascar from customers where REALTY='Y'"
q7="select count(*) as hascar from customers where CAR='Y' and REALTY = 'Y'"

q8="select * from card_applications"