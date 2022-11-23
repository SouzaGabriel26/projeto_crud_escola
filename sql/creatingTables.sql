-- apaga os relacionamentos
ALTER TABLE AlunosEG DROP CONSTRAINT ALUNOS_PK;
ALTER TABLE ProfessoresEG DROP CONSTRAINT PROFESSORES_PK;
ALTER TABLE CursoEG DROP CONSTRAINT CURSO_PK;

ALTER TABLE AlunosEG DROP CONSTRAINT CURSO_ALUNOS_FK;
ALTER TABLE ProfessoresEG DROP CONSTRAINT CURSO_PROFESSORES_FK;

-- apaga as tabelas
DROP TABLE CursoEG;
DROP TABLE ProfessoresEG;
DROP TABLE AlunosEG;

-- apaga as sequences
DROP SEQUENCE CURSO_ID_CURSO_SEQ_1;
DROP SEQUENCE PROFESSOR_ID_PROFESSOR;
DROP SEQUENCE ALUNOS_MATRICULA_SEQ;


-- cria as tabelas
CREATE TABLE CursoEG (
                id_curso NUMBER NOT NULL,
                nome VARCHAR2(255) NOT NULL,
                coordenador VARCHAR2(255) NOT NULL,
                CONSTRAINT CURSO_PK PRIMARY KEY (id_curso)
);

CREATE TABLE ProfessoresEG (
                id_professor NUMBER NOT NULL,
                nome VARCHAR2(255) NOT NULL,
                qtde_turmas NUMBER NOT NULL,
                id_curso NUMBER NOT NULL,
                CONSTRAINT PROFESSORES_PK PRIMARY KEY (id_professor)
);

CREATE TABLE AlunosEG (
                matricula NUMBER NOT NULL,
                nome VARCHAR2(255) NOT NULL,
                cpf VARCHAR2(11) NOT NULL,
                id_curso NUMBER NOT NULL,
                CONSTRAINT ALUNOS_PK PRIMARY KEY (matricula)
);

-- cria as sequences
CREATE SEQUENCE CURSO_ID_CURSO_SEQ_1;
CREATE SEQUENCE PROFESSOR_ID_PROFESSOR;
CREATE SEQUENCE ALUNOS_MATRICULA_SEQ;

-- cria os relacionamentos
ALTER TABLE AlunosEG ADD CONSTRAINT CURSO_ALUNOS_FK
FOREIGN KEY (id_curso)
REFERENCES CursoEG(id_curso);

ALTER TABLE ProfessoresEG ADD CONSTRAINT CURSO_PROFESSORES_FK
FOREIGN KEY (id_curso)
REFERENCES CursoEG(id_curso);





