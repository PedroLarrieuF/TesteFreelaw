# Teste FreeLaw

## Autores

- [@Pedro Larrieu](https://github.com/PedroLarrieuF)

## Documentação

[Documentação](https://link-da-documentação)

## Configuração de Ambiente

Para executar este projeto, siga estas etapas:

- Clone o repositório para o seu ambiente local.
- Crie um ambiente virtual na raiz do projeto executando o comando `python -m venv env`.
- Ative o ambiente virtual:
  - No Windows: `env\Scripts\activate`
  - No macOS/Linux: `source env/bin/activate`
- Instale as dependências necessárias executando o comando `pip install -r requirements.txt`.
- Execute o servidor de desenvolvimento Django usando o comando `python manage.py runserver`.

## Acessos

Após a configuração, você terá acesso a dois endpoints:

- `/api` para acessar a API.
- `/admin` para acessar a interface administrativa.

Por padrão, um usuário de superusuário chamado 'admin' é criado com a senha 'admin'. Certifique-se de atualizar as credenciais de login conforme necessário para o seu ambiente de desenvolvimento.

## Todo o código possui docstring sobre o que cada função está fazendo.

## Endpoints

### API de Gerenciamento de Eventos

Esta API oferece endpoints para gerenciar eventos e participantes associados a esses eventos.

- **Contagem Total de Eventos em Formato CSV**
  - `GET /eventos/count-total-csv/`
  - Retorna o número total de eventos em formato CSV.

- **Contagem de Eventos por Região**
  - `GET /eventos/count-by-region/`
  - Retorna a contagem de eventos por região.

- **Contagem de Eventos por Região e Dia**
  - `GET /eventos/count-by-region-and-day/`
  - Retorna a contagem de eventos por região e dia.

- **Contagem de Eventos em um Mês Específico**
  - `GET /eventos/count-in-month/<int:month>/`
  - Retorna a contagem de eventos em um mês específico, onde `<int:month>` é o número do mês (1 para janeiro, 2 para fevereiro, etc.).

- **Usuário com Mais Eventos Criados**
  - `GET /eventos/user-with-most-events/`
  - Retorna o usuário que criou o maior número de eventos.

- **Listagem de Participantes de Eventos**
  - `GET /eventos/list-event-participants/`
  - Retorna uma lista de participantes de eventos.

- **Adicionar Participante a um Evento**
  - `GET /eventos/add_participant_event/<int:id>/`
  - Adiciona um participante a um evento específico, onde `<int:id>` é o ID do evento.

- **Atualizar um Evento**
  - `PUT /eventos/update/<int:id>`
  - Atualiza os detalhes de um evento existente, onde `<int:id>` é o ID do evento.

### API de Gerenciamento de Usuários

Esta API oferece endpoints para gerenciar usuários e operações relacionadas a eles.

- **Contagem Total de Usuários**
  - `GET /usuarios/count/`
  - Retorna o número total de usuários cadastrados.

- **Exportar Usuários para CSV**
  - `GET /usuarios/export_csv`
  - Exporta a lista de usuários em formato CSV.

- **Atualizar Detalhes de um Usuário**
  - `PUT /usuarios/<int:pk>/update_user/`
  - Atualiza os detalhes de um usuário específico, onde `<int:pk>` é o ID do usuário.
