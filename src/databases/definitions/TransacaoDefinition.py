definition = """create table if not exists transacoes (
    id integer primary key autoincrement not null,
    valor numeric not null,
    tipo varchar (9),
    conta_id integer not null,
    foreign key (conta_id) references contas(id)
)"""