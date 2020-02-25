create table sessions
(
	sessionid uuid not null
		constraint sessions_pk
			primary key,
	uid integer not null,
	start_time timestamp with time zone,
	end_time timestamp with time zone
);

alter table sessions owner to postgres;