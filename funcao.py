# criaum programa que processa dados e recebe *args e *kwargs

class ProcessaDados:
    def processar(self, *args, **kwargs):
        # Implementação básica ou genérica do processamento
        print("Processando dados na classe base com args:", args, "e kwargs:", kwargs)

# Exemplo de subclasse que sobrescreve o método processar
class ProcessaDadosCustomizado(ProcessaDados):
    def processar(self, *args, **kwargs):
        # Comportamento específico de processamento
        print("Processando de forma customizada com args:", args, "e kwargs:", kwargs)

# Uso exemplo
base = ProcessaDados()
base.processar(1, 2, chave='valor') 

custom = ProcessaDadosCustomizado()
custom.processar('a', 'b', opcao=True)
