# Job Insights

Projeto desenvolvido no bloco 33 da **Trybe** com objetivo de praticar e consolidar conhecimentos em Python.

## Habilidades desenvolvidas
* Análise e visualização de dados usando Python.
* Estruturas condicionais e de repetição.
* Utilização de funções built-in do Python.
* Manipulação de arquivos e dados.
* Escrita de testes unitários usando Pytest.
* Criação e importação de módulos.
* Implementação de features e testes dentro de um projeto já existente.
* Implementação de uma nova rota sem experiência prévia em Flask.

## Arquivos
Funções e testes foram implementados, respectivamente, nos seguintes arquivos:
* `src/insights.py`
* `src/jobs.py`
* `src/routes_and_views.py` - `def job(index)`
* `tests/brazilian/test_brazilian_jobs.py`
* `tests/counter/test_counter.py`
* `tests/sorting/test_sorting.py`

Outros arquivos presentes nesse projeto foram implementados pelo time da Trybe.

## Executando a aplicação
Será necessário ter instalado as tecnologias [Docker](https://docs.docker.com/engine/install/) e [Docker Compose](https://docs.docker.com/compose/install/) em sua máquina para executar a aplicação e testes.

1. Clone o repositório:
```sh
 git clone git@github.com:raelnogpires/job-insights.git
```

2. Entre no repositório:
```sh
 cd job-insights
```

4. Execute o docker-compose:
```sh
 docker-compose up
```  

Ela estará disponível em `http://localhost:5000` .

Para executar os testes, execute:
```sh
 docker-compose run python3 -m pytest
```

Para parar a aplicação, execute:
```sh
 docker-compose down
```