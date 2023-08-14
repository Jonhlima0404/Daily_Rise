Código do Programa Daily Rise
============================

Desenvolvido por Jônatas Mascarenhas Lima

Este programa implementa o "Daily Rise", uma aplicação para rastrear tarefas diárias e acompanhar o progresso do usuário.

Estrutura do Código
-------------------

1. Importação de Módulos Necessários:
   - `datetime` para lidar com datas
   - `sys` para interagir com o sistema
   - `PyQt5.QtWidgets`, `PyQt5.QtGui` e `PyQt5.QtCore` para construir a interface gráfica

2. Classe `DailyRiseApp(QMainWindow)`:
   Esta classe define a janela principal do programa.

   2.1. Método `__init__`:
       - Configura o título e ícone da janela
       - Define o tamanho da janela
       - Cria a estrutura da interface do usuário usando layouts

   2.2. Métodos para Interação com as Tarefas:
       - `load_xp`: Carrega a quantidade de XP do arquivo 'xp.txt'
       - `load_level`: Carrega o nível do usuário do arquivo 'level_user.txt'
       - `view_current_quests`: Exibe as missões atuais no campo de texto 'quests_text'
       - `view_completed_quests`: Exibe as missões completas no campo de texto 'completed_quests_text'
       - `view_progress`: Calcula e exibe a progressão de nível com uma barra de progresso
       - `add_quest`: Adiciona uma nova missão à lista de missões
       - `complete_quest`: Marca uma missão como completa, atualiza XP e nível
       - `set_background`: Define um plano de fundo para a janela

   2.3. Método `main`:
       - Inicializa o aplicativo e a janela principal

3. Função `main`:
   - Cria a instância do aplicativo
   - Cria e mostra a janela principal
   - Inicia o loop do aplicativo

Execução do Programa
--------------------

1. Ao iniciar o programa:
   - A janela de entrada `MainMenu` é exibida, contendo o título "Daily Rise", uma imagem de fundo e um botão "Entrar no programa".

2. Ao clicar no botão "Entrar no programa":
   - A janela `MainMenu` é fechada
   - A janela principal `DailyRiseApp` é aberta

3. Na janela principal:
   - Exibe informações sobre missões, progresso de nível, XP atual e nível atual
   - Permite adicionar novas missões e marcar missões como completas

4. Menu de Saída:
   - O usuário pode acessar o menu "Menu" na barra superior e selecionar "Sair" para fechar o programa.

Este programa foi desenvolvido por Jônatas Mascarenhas Lima, com o objetivo de ajudar os usuários a acompanhar suas tarefas diárias, monitorar seu progresso e manter um registro das missões completas.
