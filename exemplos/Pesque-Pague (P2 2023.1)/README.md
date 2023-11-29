# Sistema de Pesque-Pague

Este é um sistema de Pesque-Pague desenvolvido em Python utilizando a biblioteca Tkinter. O sistema permite cadastrar peixes, consultar informações sobre os peixes cadastrados, fechar comandas e gerar relatórios de faturamento.

## Funcionalidades

- Cadastro de peixes: Permite cadastrar informações sobre os peixes, como nome e preço.

- Consulta de peixes: Permite consultar as informações dos peixes cadastrados.

- Fechamento de comandas: Permite fechar uma comanda, registrando o consumo dos peixes pescados e calculando o valor total a ser pago.

- Geração de relatórios de faturamento: Permite gerar um relatório com o faturamento do pesque-pague.

## Arquivos

- `main.py`: Contém a classe `LimitePrincipal` que representa a janela principal do sistema e a classe `ControlePrincipal` que controla o fluxo do programa.

- `peixe.py`: Contém as classes `Peixe`, `PeixeComanda`, `Comanda`, `LimiteCadastrarPeixe`, `LimiteConsultaPeixe`, `LimiteFechaComanda`, `LimiteRelatorio` e `CtrlPeixe`, que são responsáveis pela definição das entidades e das interfaces do sistema relacionadas aos peixes.

## Como usar

Certifique-se de ter o Python instalado em seu computador. Em seguida, siga as instruções abaixo:

1. Faça o download dos arquivos do projeto.

2. Abra um terminal e navegue até o diretório onde os arquivos estão localizados.

3. Execute o seguinte comando para iniciar o sistema:
   ```
   python main.py
   ```

4. O sistema será iniciado e uma janela principal será exibida.

5. Utilize os menus e botões disponíveis na janela para acessar as diferentes funcionalidades do sistema.

## Exemplo

Aqui está um exemplo de como o sistema pode ser utilizado:

1. Cadastrar um peixe:
   - Selecione a opção "Peixe" no menu principal.
   - Clique em "Cadastrar" no submenu.
   - Preencha as informações solicitadas sobre o peixe e clique em "Enter".

2. Consultar informações de um peixe:
   - Selecione a opção "Peixe" no menu principal.
   - Clique em "Consultar" no submenu.
   - Será exibida uma lista com os peixes cadastrados. Selecione o peixe desejado para visualizar suas informações.

3. Fechar uma comanda:
   - Selecione a opção "Comanda" no menu principal.
   - Clique em "Fecha Comanda".
   - Escolha o peixe a ser adicionado na comanda e informe o peso.
   - Clique em "Adiciona Peixe" para adicionar o peixe à comanda.
   - Quando todos os peixes forem adicionados, clique em "Fecha Comanda" para fechar a comanda e exibir um resumo.

4. Gerar um relatório de faturamento:
   - Selecione a opção "Relatório" no menu principal.
   - Clique em "Faturamento".
   - Será gerado um relatório com as informações de faturamento do pesque-pague.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para fazer sugestões ou melhorias para este sistema de pesque-pague.