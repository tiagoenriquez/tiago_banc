definition = """create table if not exists contas (
    id integer primary key autoincrement not null,
    numero integer not null unique,
    saldo numeric not null,
    usuario_id integer not null,
    foreign key (usuario_id) references usuarios(id)
)"""