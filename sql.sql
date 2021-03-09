create table employee(employee_name varchar(255), employee_role varchar(255));

alter table employee add column index_number varchar(255) first; 

alter table employee drop column index_number;

select * from employee order by 1
insert into employee values ('nitin', 'student');
select * from mysql.user;
----
alter table employee drop column index_number;
delete from employee where employee_name = "Nitin"