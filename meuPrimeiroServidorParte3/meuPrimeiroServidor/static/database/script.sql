PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS jogadores (
    id_jogador INTEGER NOT NULL,
    valor TEXT NOT NULL,
    nome TEXT NOT NULL,
    PRIMARY KEY (id_jogador)
);

INSERT INTO jogadores(id_jogador, valor, nome) VALUES(1, 'neymar_jr', 'Neymar Jr');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES(2, 'richarlison', 'Richarlison');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES(3, 'daniel_alves', 'Daniel Alves');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES(4, 'vinicius_jr', 'Vinicius Jr');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES(5, 'rodrygo', 'Rodrygo');

COMMIT;