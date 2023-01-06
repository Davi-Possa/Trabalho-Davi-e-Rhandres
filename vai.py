create database banco;
use banco;

CREATE TABLE `PESSOA` (
    `n_identidade` int not null,
    `nome` varchar(100) not null,
    `fone` varchar(50) not null,
    PRIMARY KEY (n_identidade));

CREATE TABLE `VIAGEM` (
    `cod_viagem` int auto_increment,
    `data_viagem` date not null,
    `cidade` varchar(50),
    PRIMARY KEY(cod_viagem));

CREATE TABLE `PESSOA_VIAGEM` (
    `cod_viagem` int,
    `n_identidade` int,
    `hora` varchar(60) not null,
    `turno` varchar(60) not null,
    `parada` varchar(60),
    `destino` varchar(60) not null,
    FOREIGN KEY(cod_viagem) REFERENCES VIAGEM(cod_viagem),
    FOREIGN KEY(n_identidade) REFERENCES PESSOA(n_identidade));


