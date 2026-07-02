from dotenv import load_dotenv
from database.Connector import DataBase
from database.repositories.ervas_repository import Erva_Repository
from models.erva import Erva

def main():
    load_dotenv()
    
    def listar_ervas():
        with DataBase() as db:
            erva_repository = Erva_Repository(db)
            ervas = erva_repository.List_Ervas()

            for erva in ervas:
                print(f'ID: {erva.id},       Nome:       {erva.nome}')
            
    def atualizar_erva():
        def update():
            erva = Erva()

            with DataBase() as db:
                erva_repository = Erva_Repository(db)
                erva_repository.update(erva)
        
        while True:
            acao = int(input('''
                            Digite qual opção você deseja:

                            1. Pesquisar pelo Nome da Erva
                            2. Pesquisar pelo ID da Erva
                            3. Listar as Ervas
                            4. Voltar
                            '''
            ))

            match acao:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    print('Você foi direcionado para o Menu Inicial.')
                    return False
        
    def cadastrar_erva():
        nome = input('Qual é o Nome da erva? ')
        composicao = input('Qual é a Composição da erva? ')
        corte = input('Qual é o Tipo de Corte da erva? ')
        qualidade = input('Qual é a Qualidade da erva? ')
        sabor = input('Qual é o Sabor da erva? ')
        nacionalidade = input('Qual é a Nacionalidade da erva? ')

        erva = Erva(
            nome= nome,
            tipo=composicao,
            corte= corte,
            qualidade= qualidade,
            sabor= sabor,
            nacionalidade= nacionalidade
        )

        with DataBase() as db:
            erva_repository = Erva_Repository(db)
            erva_repository.create(erva)

    while True:
        acao = int(input(
            ''' 
            Selecione o que deseja:
            1) Cadastrar Nova Erva
            2) Visualizar Ervas já cadastradas
            3) Editar Ervas
            4) Sair.
            '''
        ))
        
        match acao:
            case 1:
                cadastrar_erva()
            case 2:
                listar_ervas()
            case 3:
                atualizar_erva()
            case 4: 
                return False
        

if __name__ == "__main__":
    main()
