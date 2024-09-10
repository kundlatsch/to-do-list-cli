from tarefa import Tarefa
from persistencia import carregar_tarefas, salvar_tarefas

class GerenciadorDeTarefas:

    def __init__(self, nome_arquivo="tarefas.pkl"):
        self.nome_arquivo = nome_arquivo
        self.tarefas = carregar_tarefas(nome_arquivo)
    
    def adicionar_tarefa(self, titulo, descricao, data_vencimento):
        nova_tarefa = Tarefa(titulo, descricao, data_vencimento)
        self.tarefas.append(nova_tarefa)
        print(f"Tarefa {titulo} adicionada com sucesso!")
        self.salvar()
    
    def listar_tarefas(self, status=None):

        if not self.tarefas:
            print("Nenhuma tarefa encontrada!")
            return
        
        for i, tarefa in enumerate(self.tarefas):
            if status is None or tarefa.status == status:
                print(f"\nTarefa {i+1}:\n{tarefa.detalhes()}")
        print("\nFim da Lista de tarefas.")
    
    def editar_tarefa(self, indice, titulo=None, descricao=None, data_vencimento=None):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            if titulo:
                tarefa.editar_titulo(titulo)
            if descricao:
                tarefa.editar_descricao(descricao)
            if data_vencimento:
                tarefa.editar_data_vencimento(data_vencimento)
            print(f"Tarefa {indice+1} editada com sucesso!")
            self.salvar()
        else:
            print("Índice inválido.")
    
    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa_removida = self.tarefas.pop(indice)
            print(f"Tarefa {indice+1} removida com sucesso!")
            self.salvar()
        else:
            print("Índice inválido.")

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            tarefa.marcar_concluida()
            print(f"Tarefa {indice+1} marcada como concluída!")
            self.salvar()
        else:
            print("Índice inválido.")

    def salvar(self):
        salvar_tarefas(self.tarefas, self.nome_arquivo)