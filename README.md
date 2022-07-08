# codeplay Aval

Extração de features das turmas do codebench para avaliação do codeplay.

Features extraídas:

- `id_aluno`: id do aluno no sistema codebench.

- `logins`: número de logins durante o semestre.

- tamanho_logs_listas: número total de registros de logs gerados pelo aluno durante a resolução de listas de exercícios

- tamanho_logs_avaliacoes: número total de registros de logs gerados pelo aluno durante a resolução de avaliaçãos práticas

- total_testes_listas: número total de testes feitos pelo aluno durante a resolução de avaliaçãos práticas

- total_erros_sintaticos_testes_listas: número total de erros sintáticos em testes (não submissões) gerados durante a resolução de listas de exercícios

- total_submissoes_listas: número total de submissões feitos pelo aluno durante a resolução de listas de exercícios

- total_submissoes_incorretas_listas: número total de submissões incorretas (com erros sintáticos ou que não passaram nos casos de teste) pelo aluno durante a resolução de listas de exercícios

- total_testes_avaliacoes: número total de testes feitos pelo aluno durante a resolução de avaliaçãos práticas

- total_erros_sintaticos_testes_avaliacoes: número total de erros sintáticos em testes (não submissões) gerados durante a resolução de avaliaçãos práticas

- total_submissoes_avaliacoes: número total de submissões feitos pelo aluno durante a resolução de avaliaçãos práticas

- total_submissoes_incorretas_avaliacoes: número total de submissões incorretas (com erros sintáticos ou que não passaram nos casos de teste) pelo aluno durante a resolução de avaliaçãos práticas

- indice_procrastinacao_listas: tempo médio em minutos entre as submissões feitos pelos alunos e a data de término do trabalho. Para calcular esssa métrica, para cada submissão feita pelo aluno nas listas de exercícios, eu calculei a diferença de tempo entre a data de término do trabalho e o tempo da submissão. Somei todos os tempos encontrados, e depois dividi pelo total de submissões (durante todo o semestre, considerando todas as submissões feitas nas listas de exercícios).