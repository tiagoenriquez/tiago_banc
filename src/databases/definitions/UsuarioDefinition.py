definition = """create table if not exists usuarios (
    id integer primary key autoincrement not null,
    nome varchar (63) not null,
    cpf varchar (15) not null unique,
    perfil varchar (14) not null,
    senha varchar (127)
)"""