import flet as ft
import networkx as nx

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handle_hello(self, e):
        self._view.clear()
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il valore medio minimo")
            return



        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def buildGraph(self):
        self._model._grafo.add_all_nodes(self._model.aereoporti)
        for i in self._model.aereoporti:
            self._model._idAereoporti[i.AIRPORT] = i

        for a in self._model._grafo.nodes:
            edges = self.getallEdges(a)
            media = self.media(edges)
            if int(self._view.txt_name.value) < media:
                self._model._grafo.add_All_edges(edges)


    def getallEdges(self, aereoporto):
        temp = []
        for v in self.UI.DAO.getVoli():
            if v.ORIGIN_AIRPORT_ID == aereoporto or v.DESTINATION_AIRPORT_ID == aereoporto:
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
            self._model._grafo.add_edge(self._model._idAereoporti[v.ORIGIN_AIRPORT_ID], self._model._idAereoporti[v.DESTINATION_AIRPORT_ID], weight=v.DISTANCE)