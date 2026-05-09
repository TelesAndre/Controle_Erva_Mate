from models.erva import Erva

class Erva_Repository:
    def __init__(self, db):
        self._db = db
    
    def create(self, erva: Erva):
        self._db.execute(
            """
            INSERT INTO ervasprovadas(
                nome,
                tipocomposicao,
                tipocorte,
                qualidade,
                sabor,
                nacionalidade
            )
            VALUES(%s,%s,%s,%s,%s,%s)
            """,
            (
                erva.nome,
                erva.tipo,
                erva.corte,
                erva.qualidade,
                erva.sabor,
                erva.nacionalidade
            )
        )
    
    def update(self, erva:Erva):
        pass

    def List_Ervas(self):
        self._db.execute(
            """
            SELECT
            id,
            nome
            FROM
            ervasprovadas
            """
        )
        rows = self._db.fetchall()
        ervas = []
        for row in rows:
            erva = Erva(
                id = row["id"],
                nome= row["nome"]
            )
            ervas.append(erva)

        return ervas