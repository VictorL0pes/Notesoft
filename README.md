# Notesoft

## 1. Introdução

O **Notesoft** é um projeto desenvolvido para a disciplina de **Desenvolvimento Web** do curso BICT da UFMA. Este sistema foi concebido para demonstrar a aplicação prática dos conceitos e técnicas de desenvolvimento web, integrando o uso do framework Flask com boas práticas de programação, modularidade e escalabilidade. O objetivo é oferecer uma plataforma que possibilite a organização e o gerenciamento de conteúdos de forma intuitiva e eficiente, servindo tanto para fins educacionais quanto para experimentação de soluções tecnológicas.

## 2. Contexto

### 2.1 Base Teórica e Objetivos

- **Fundamentação Técnica:**  
  O projeto utiliza o **Flask**, um micro-framework em Python que possibilita a criação de aplicações web de maneira simples e flexível. Essa escolha se justifica pela capacidade do Flask de oferecer um ambiente leve e customizável, permitindo a integração com diversas bibliotecas e extensões conforme as necessidades do projeto.

- **Objetivo da Aplicação:**  
  Demonstrar, na prática, os conceitos aprendidos na disciplina de Desenvolvimento Web, evidenciando a implementação de rotas, gerenciamento de sessões, integração com banco de dados e organização modular do código, elementos essenciais para a construção de sistemas robustos e de fácil manutenção.

### 2.2 Alcance do Projeto

- **Aplicação Didática:**  
  Voltado para o ensino e experimentação, o Notesoft permite que estudantes e desenvolvedores visualizem a aplicação prática dos conceitos teóricos em um ambiente de desenvolvimento real.
- **Integração de Tecnologias:**  
  O projeto integra ferramentas e bibliotecas complementares ao Flask, demonstrando a aplicabilidade de técnicas modernas no desenvolvimento web.

## 3. Desenvolvimento

### 3.1 Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework Web:** [Flask](https://flask.palletsprojects.com/)
- **Front-end:** HTML5, CSS3 e JavaScript
- **Gerenciamento de Dependências:** Utilização do arquivo `requirements.txt` para listar as bibliotecas necessárias.

# Como Inicializar o Projeto Notesoft na IDE

Este guia apresenta os passos necessários para configurar e iniciar o projeto Notesoft em sua IDE, garantindo que todas as dependências estejam corretamente instaladas e o ambiente esteja preparado para o desenvolvimento.

---

## 1. Clonagem do Repositório

1. Certifique-se de que o Git está instalado em sua máquina.
2. Abra o terminal e execute o seguinte comando para clonar o repositório:

   ```bash
   git clone https://github.com/VictorL0pes/Notesoft.git
   ```

3. Após a clonagem, abra a pasta do projeto na sua IDE (como PyCharm, VS Code, etc.).

---

## 2. Configuração do Ambiente Virtual

1. No terminal integrado da sua IDE, crie um ambiente virtual para isolar as dependências do projeto:

   - **Linux/macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. Configure sua IDE para utilizar o interpretador Python do ambiente virtual recém-criado:
   - **No PyCharm:**  
     Vá em **File > Settings > Project: [Nome do Projeto] > Python Interpreter** e selecione o interpretador localizado na pasta `venv`.
   - **No VS Code:**  
     Utilize a paleta de comandos (Ctrl+Shift+P ou Cmd+Shift+P) e selecione **Python: Select Interpreter**, escolhendo o interpretador dentro da pasta `venv`.

---

## 3. Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto executando:

```bash
pip install -r requirements.txt
```

Isso garante que todas as bibliotecas necessárias, conforme listadas no arquivo `requirements.txt`, sejam instaladas.

---

## 4. Configuração da Run Configuration

O ponto de entrada da aplicação é o script `run.py`. Configure sua IDE para executar este arquivo:

- **No PyCharm:**
  1. Vá em **Run > Edit Configurations...**
  2. Clique no ícone **+** para adicionar uma nova configuração e selecione **Python**.
  3. Em **Script path**, aponte para o arquivo `run.py`.
  4. Certifique-se de que o interpretador está definido como o ambiente virtual criado.
  5. Salve a configuração.

- **No VS Code:**
  1. Abra a paleta de comandos e selecione **Debug: Open launch.json** para criar ou editar o arquivo de configuração.
  2. Configure uma entrada para executar `run.py`, por exemplo:
  
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "name": "Run Notesoft",
                 "type": "python",
                 "request": "launch",
                 "program": "${workspaceFolder}/run.py",
                 "console": "integratedTerminal"
             }
         ]
     }
     ```
  3. Salve o arquivo `launch.json`.

---

## 5. Execução do Projeto

1. Execute a run configuration criada na sua IDE.
2. O script `run.py` iniciará o servidor de desenvolvimento do Flask.
3. Abra o navegador e acesse o endereço:

   ```
   http://localhost:5000
   ```

   para visualizar a aplicação em funcionamento.

---

## 6. Considerações Finais

- **Modo Debug:**  
  O projeto é configurado para rodar em modo debug (por meio do parâmetro `debug=True` em `app.run()`), o que facilita a identificação de erros e o recarregamento automático durante o desenvolvimento.
  
- **Variáveis de Ambiente:**  
  Para ajustes de configuração, como a definição de variáveis sensíveis ou parâmetros específicos, recomenda-se utilizar arquivos de configuração ou variáveis de ambiente, garantindo maior flexibilidade e segurança.

Seguindo estas orientações, seu ambiente de desenvolvimento estará pronto para executar e depurar o projeto Notesoft de forma eficiente.


