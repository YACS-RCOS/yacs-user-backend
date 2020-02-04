create table users
(
	uid serial not null
		constraint users_pk
			primary key,
	name text,
	email text not null,
	phone text,
	password text,
	major text,
	degree text,
	enable boolean default true
);

alter table users owner to postgres;

create unique index users_email_uindex
	on users (email);
