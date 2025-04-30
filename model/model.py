import networkx as nx

from  UI.controller import Controller
from database.DAO import DAO


class Model:
    def __init__(self):
        self._aereoporti = DAO.getAereoporti()
        self._grafo = nx.Graph()
        self._idMapAereoporti = {}

    def mapAereoporti(self):
        for i in self._aereoporti:
            self._idMapAereoporti[i.ID] = i