create table if not exists user_notifications
(
id int not null auto_increment, 
notification text not null,
is_read int default 0, 
created_time datetime default null,
read_time datetime default null,
user_id int not null,
PRIMARY KEY (`id`),
constraint `fk_user_notifications_user_id` foreign key(user_id) references users(id) ON UPDATE CASCADE
)engine=InnoDB;
