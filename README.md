
<p align="center">
  <img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

Processador de Dados em Python com *args e **kwargs
Este projeto contém uma classe base ProcessaDados para processar dados com parâmetros variáveis usando *args e **kwargs. 
Há também uma subclasse ProcessaDadosCustomizado que sobrescreve o método de processamento para comportamento customizado.

Descrição das Classes
ProcessaDados: Classe base com método processar(self, *args, **kwargs) que imprime os parâmetros recebidos de forma genérica.
ProcessaDadosCustomizado: Subclasse que sobrescreve o método processar para implementar processamento específico.

Informações Técnicas
O uso de *args permite passar uma quantidade variável de argumentos posicionais para o método.
O uso de **kwargs permite passar uma quantidade variável de argumentos nomeados (chave-valor).
A herança é usada para especializar o comportamento do método de processamento.
