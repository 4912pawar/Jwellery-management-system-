create table transactions
(tran_id integer primary key auto_increment , 
total_amount integer,
trans_date varchar(30),
orn_id integer,
customer_id integer,
foreign key (orn_id) references ornaments(orn_id),
foreign key (customer_id) references customers(customer_id));
