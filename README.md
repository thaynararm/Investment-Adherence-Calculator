# Investment-Adherence-Calculator

Um aplicativo Django para calcular a aderência de carteiras de investimento às estratégias definidas.

Este é um projeto que visa calcular a aderência de investimentos com base em dados de contas e ativos investidos. 

O projeto envolve a criação de um banco de dados PostgreSQL, a ingestão de dados, normalização de tabelas e cálculos de aderência.

## Configuração do Banco de Dados

1. Instale o PostgreSQL em sua máquina e o arquivo 'fake_position.csv'.

2. No pgAdmin, crie um banco de dados chamado `Clients`.

3. Abra o Query Tool e execute os seguintes comandos para criar a tabela `clients` e importar os dados:

    ```sql
    CREATE TABLE clients(
        account_code VARCHAR(6) NOT NULL,
        account_suitability VARCHAR(30),
        asset_name TEXT,
        asset_cnpj VARCHAR(20),
        class_name VARCHAR(50),
        position_value NUMERIC
    );

4. Para importar os dados do arquivo 'fake_position' para a tabela 'clients' utilizaremos o seguinte comando no PSQL Tool:

   OBS: o caminho_do_arquivo_fake_position no código abaixo muda de acordo com o local onde ele foi salvo em sua máquina.

   ```sql
     \copy public.clients (account_code, account_suitability, asset_name, asset_cnpj, class_name, position_value) FROM 'caminho_do_arquivo_fake_position.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8' ESCAPE ''''

## Normalização da Tabela

1. Crie a tabela 'accounts' que conterá apenas as informações sobre a conta dos clientes com o seguinte comando:

     ```sql
     CREATE TABLE accounts(
	      account_code VARCHAR(6) PRIMARY KEY,
	      account_suitability VARCHAR(30)
     );

2. Importe as informações da tabela 'clients', de forma que não tenhamos dados repetidos, utilizando o seguinte comando:

     ```sql
     INSERT INTO accounts(account_code, account_suitability)
     SELECT DISTINCT account_code, account_suitability
     FROM clients

3. Crie a tabela 'assets' que conterá as informações sobre os ativos investidos em cada conta com o seguinte comando:

    ```sql
    CREATE TABLE assets(
       id SERIAL PRIMARY KEY NOT NULL,
	     account_code VARCHAR(6),
       asset_name TEXT,
       asset_cnpj VARCHAR(16),
       class_name VARCHAR(50),
       position_value NUMERIC(12, 2),

       FOREIGN KEY (account_code)
       REFERENCES accounts (account_code)
        );

4. Importe as informações da tabela 'clients' utilizando o seguinte comando:

     ```sql
     INSERT INTO assets(account_code, asset_name, asset_cnpj, class_name, position_value)
     SELECT account_code, asset_name, asset_cnpj, class_name, position_value
     FROM clients

## Como Usar

1. A consulta pode ser feita diretamente no banco de dados usando o comando do arquivo 'adhesion_consultation.sql', mas a informação sobre a classe de ativos mais desrespeitada não é retornada por essa consulta.

2. Para visualizar em uma dashboard clone este repositório para o seu ambiente local.

3. Configure e inicie seu ambiente virtual (se estiver usando um) e instale as dependências listadas no arquivo requiriments.txt.

5. Execute o aplicativo ou script que calcula a aderência com base nos dados do banco de dados usando o comando:
   ```sql
   python manage.py runserver

© 2023 Thaynara Martins
