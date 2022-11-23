select p.nome as professor, c.nome as nome_curso, count(c.id_curso) as qtde_alunos 
from alunosEG a
inner join professoresEG p
on a.id_curso = p.id_curso
inner join cursoEG c
on p.id_curso = c.id_curso
group by (p.nome, c.nome, c.id_curso)
