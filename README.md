# Avaliação do CodePlay

Extração de features das turmas do codebench para avaliação do codeplay. Para computar as features abaixo, eu ignorei os Lab 0, que são laboratórios de ambientação com o sistema codebench.

Features extraídas:

- `id_aluno`: id do aluno no sistema codebench.

- `logins`: número de logins durante o semestre.

- `tamanho_logs_listas`: número total de registros de logs gerados pelo aluno durante a resolução de listas de exercícios.

- `tamanho_logs_avaliacoes`: número total de registros de logs gerados pelo aluno durante a resolução de avaliaçãos práticas.

- `total_testes_listas`: número total de testes feitos pelo aluno durante a resolução de listas de exercícios.

- `total_testes_avaliacoes`: número total de testes feitos pelo aluno durante a resolução de avaliaçãos práticas.

- `total_erros_sintaticos_testes_listas`: número total de erros sintáticos em testes (não submissões) gerados durante a resolução de listas de exercícios.

- `total_erros_sintaticos_testes_avaliacoes`: número total de erros sintáticos em testes (não submissões) gerados durante a resolução de avaliaçãos práticas.

- `total_submissoes_listas`: número total de submissões feitos pelo aluno durante a resolução de listas de exercícios.

- `total_submissoes_avaliacoes`: número total de submissões feitos pelo aluno durante a resolução de avaliaçãos práticas.

- `total_submissoes_incorretas_listas`: número total de submissões incorretas (com erros sintáticos ou que não passaram nos casos de teste) feitas pelo aluno durante a resolução de listas de exercícios.

- `total_submissoes_incorretas_avaliacoes`: número total de submissões incorretas (com erros sintáticos ou que não passaram nos casos de teste) feitas pelo aluno durante a resolução de avaliaçãos práticas.

- `indice_procrastinacao_listas`: tempo médio (em minutos) entre as submissões feitos pelos alunos e a data de término do trabalho. Para calcular esssa métrica, para cada submissão feita pelo aluno nas listas de exercícios, eu calculei a diferença de tempo entre a data de término do trabalho e o tempo da submissão. Somei todos os tempos encontrados, e depois dividi pelo total de submissões (feitas durante todo o semestre em todas as listas de exercícios). Note que, quanto maior o valor dessa feature, menos o aluno procrastinou.

- `indice_procrastinacao_listas`: Esta métrica define o quão próximo da data de entrega o aluno deixou para solucionar os exercícios de um dado trabalho. Para calcular esssa métrica, para cada submissão feita pelo aluno nas listas de exercícios, eu calculei o percentual do tempo já decorrido entre a data de início e a data de término do trabalho. Por exemplo, se o aluno fez a submissão no primeiro segundo após o início do trabalho, esse percentual será 0. Se o aluno fez a submissão no último segundo do prazo de entrega do trabalho, então esse percentual será 1. Somei todos os percentuais encontrados, e depois dividi pelo total de submissões (feitas durante todo o semestre em todas as listas de exercícios). Note que, quanto maior o valor dessa feature, mais o aluno procrastinou.

# Campos do questionário demográfico

- `id_user`: ID do usuário

- `computador_pessoal`: Tem acesso a um computador pessoal (PC, desktop ou notebook)?
  -- 1: Sim;
  -- 2: Não
  -- 3: Sim, mas ele é de um parente ou vizinho e preciso sair de cada para acessá-lo

- `gosto_jogos`: Você gosta de jogar video games?
  -- 1: Gosto demais!
  -- 2: Gosto
  -- 3: Mais ou menos
  -- 4: Pouco
  -- 5: Não gosto

- `frequencia_jogos`: Com que frequência você joga video games?
  -- 1: Todos os dias
  -- 2: 3 vezes por semana
  -- 3: 1 vez por semana
  -- 4: Eu raramente jogo
  -- 5: Eu nunca jogo

- `gosto_jogos_aventura`: O quanto você gosta de jogos de aventura?
  -- 1: Gosto demais!
  -- 2: Gosto
  -- 3: Mais ou menos
  -- 4: Pouco
  -- 5: Não gosto

- `gosto_jogos_luta_acao`: O quanto você gosta de jogos de luta e ação?
  -- 1: Gosto demais!
  -- 2: Gosto
  -- 3: Mais ou menos
  -- 4: Pouco
  -- 5: Não gosto

- `gosto_jogos_rpg`: O quanto você gosta de jogos de RPG (Role-Playing Game)?
  -- 1: Gosto demais!
  -- 2: Gosto
  -- 3: Mais ou menos
  -- 4: Pouco
  -- 5: Não gosto

- `gosto_jogos_puzzle`: O quanto você gosta de jogos Puzzle (raciocínio, quebra-cabeças)?
  -- 1: Gosto demais!
  -- 2: Gosto
  -- 3: Mais ou menos
  -- 4: Pouco
  -- 5: Não gosto

- `gosto_jogos_esporte`: O quanto você gosta de jogos de esporte?
  -- 1: Gosto demais!
  -- 2: Gosto
  -- 3: Mais ou menos
  -- 4: Pouco
  -- 5: Não gosto

- `ja_jogou_rpg_eletronico`: Você já jogou video games de RPG? Ex: Final Fantasy, Diablo, World of Warcraft, The Whitcher, Assassin's Creed, etc.
  -- 1: Joguei várias vezes
  -- 2: Joguei algumas vezes
  -- 3: Joguei uma vez
  -- 4: Nunca joguei
  -- 5: Não conheço esse tipo de jogo

- `ja_jogou_rpg_mesa`: Você já jogou jogos de RPG de mesa? Ex: Dungeons and Dragons, Vampiro – A Máscara, Pathfinder, O chamado de Cthulhu, etc.
  -- 1: Joguei várias vezes
  -- 2: Joguei algumas vezes
  -- 3: Joguei uma vez
  -- 4: Nunca joguei
  -- 5: Não conheço esse tipo de jogo-
- `ano_nascimento`: Qual o ano em que você nasceu?

- `sexo`: Qual é o seu sexo?
  -- 1: Masculino
  -- 2: Feminino

- `estado_civil`: Qual o seu estado civil?
  -- 1: Solteiro(a)
  -- 2: Casado(a)
  -- 3: Viúvo(a)
  -- 4: Separado(a)
  -- 5: União estável

- `filhos`: Você tem filho(s)?
  -- 1: Sim
  -- 2: Não
