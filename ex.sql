create database my_database;
create role my_username with password 'my_password' LOGIN;
grant all privileges on database my_database to my_username;

create table phonebook (
  firstname varchar not null,
  lastname varchar,
  number varchar not null,
  email varchar
);
insert into phonebook(firstname, lastname, number, email)
values ('Madina', 'Leker', '+77474245834', 'madina12@mail.ru' );