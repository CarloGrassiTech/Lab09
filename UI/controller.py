import flet as ft
import networkx as nx
from database.DAO import DAO
class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_hello(self, e):
        if self._view.txt_result != None:
            self._view.txt_result.clean()
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il valore medio minimo")
            return
        self.buildGraph()

        self._view.txt_result.controls.append(ft.Text(f"Il grafico ha vertici: {len(self._model._grafo.nodes)} \n archi: {len(self._model._grafo.edges)} \n Elenco archi : \n"))
        for v in self._model._grafo.edges:
            self._view.txt_result.controls.append(ft.Text(f"{v}"))
        self._view.update_page()


    def buildGraph(self):
        self._model._grafo.add_nodes_from(self._model._aereoporti)
        self._model.mapAereoporti()

        for a in self._model._grafo.nodes:
            edges = self.getallEdges(a)
            media = self.media(edges)
            print(f"{media} media e inserimento utente {self._view.txt_name.value}")
            if int(self._view.txt_name.value) < media:
                self.add_All_edges(edges)


    def getallEdges(self, aereoporto):
        temp = []
        for v in DAO.getVoli(aereoporto):
            temp.append(v)
        return temp

    def media(self, voli):
        temp = 0
        if len(voli)==0:
            return temp
        for i in voli:
            temp+= i.DISTANCE
        return temp/len(voli)

    def add_All_edges(self, edges):
        for v in edges:
            self._model._grafo.add_edge(self._model._idMapAereoporti[v.ORIGIN_AIRPORT_ID], self._model._idMapAereoporti[v.DESTINATION_AIRPORT_ID], weight=v.DISTANCE)