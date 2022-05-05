create table if not exists posts(
  id bigserial primary key not null unique,
  title varchar(300) not null,
  body varchar(65536),
  createdat varchar(50)
);