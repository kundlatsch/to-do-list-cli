from datetime import datetime

class Tarefa:

    def __init__(self, titulo, descricao, data_vencimento, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        self.status = status

    def __repr__(self):
        return  f"Tarefa(titulo='{self.titulo}', descricao='{self.descricao}', " \
                f"data_vencimento='{self.data_vencimento.strftime('%d/%m/%Y')}', status='{self.status}')"
    
    def marcar_concluida(self):
        self.status = "Concluída"

    def esta_atrasada(self):
        return datetime.now() > self.data_vencimento and self.status == "Pendente"
    
    def editar_titulo(self, titulo):
        self.titulo = titulo

    def editar_descricao(self, descricao):
        self.descricao = descricao

    def editar_data_vencimento(self, data):
        self.data_vencimento = datetime.strptime(data, "%d/%m/%Y")
    
    def detalhes(self):
        status = "Atrasada" if self.esta_atrasada() else self.status
        return (f"Título: {self.titulo}\n"
                f"Descrição: {self.descricao}\n"
                f"Data de Vencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\n"
                f"Status: {self.status}")

