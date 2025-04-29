import UI


class Model:
    def __init__(self):
        self._grafo = UI.controller.buildGraph()
        self._aereoporti = self.model.DAO.getAereoporti()
        self._idMapAereoporti = {}