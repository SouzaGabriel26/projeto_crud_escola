-- junção de tabelas
SELECT a.matricula, a.nome, a.cpf, a.id_curso, c.nome, c.coordenador
FROM AlunosEG a
INNER JOIN CursoEG c
ON a.id_curso = c.id_curso
ORDER BY a.matricula
