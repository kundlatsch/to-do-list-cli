import argparse
from gerenciador import GerenciadorDeTarefas

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas CLI em Python!")

    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

    # Adicionar uma nova tarefa
    parser_adicionar = subparsers.add_parser("adicionar", help="Adicionar uma nova tarefa")
    parser_adicionar.add_argument("titulo", type=str, help="Título da tarefa")
    parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")
    parser_adicionar.add_argument("data_vencimento", type=str, help="Data de vencimento no formato DD/MM/AA")

    # Listar tarefas
    parser_listar = subparsers.add_parser("listar", help="Listar todas as tarefas")
    parser_listar.add_argument("--status", choices=["Pendente", "Concluída"], help="Filtrar por status da tarefa")

    # Editar tarefa
    parser_editar = subparsers.add_parser("editar", help="Editar uma tarefa")
    parser_editar.add_argument("indice", type=int, help="Índice da tarefa a ser atualizada")
    parser_editar.add_argument("--titulo", type=str, help="Novo título da tarefa")
    parser_editar.add_argument("--descricao", type=str, help="Nova descrição da tarefa")
    parser_editar.add_argument("--data_vencimento", type=str, help="Nova data de vencimento no formato DD/MM/AA")

    # Remover tarefa
    parser_remover = subparsers.add_parser("remover", help="Remover uma tarefa")
    parser_remover.add_argument("indice", type=int, help="Índice da tarefa a ser removida")

    # Marcar tarefa como concluída
    parser_marcar_concluida = subparsers.add_parser("concluir", help="Concluir uma tarefa")
    parser_marcar_concluida.add_argument("indice", type=int, help="Índice da tarefa a ser removida")

    # Processar argumentos

    args = parser.parse_args()
    gerenciador = GerenciadorDeTarefas()
    
    if args.comando == "adicionar":
        gerenciador.adicionar_tarefa(args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "listar":
        gerenciador.listar_tarefas(args.status)
    elif args.comando == "editar":
        gerenciador.editar_tarefa(args.indice - 1, args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "remover":
        gerenciador.remover_tarefa(args.indice - 1)
    elif args.comando == "concluir":
        gerenciador.marcar_concluida(args.indice - 1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()