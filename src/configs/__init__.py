import os

class Config:
    @property
    def GRAPH_INDEX_DIR(self):
        GRAPH_INDEX_DIR = os.environ.get("GRAPH_INDEX_DIR")
        assert GRAPH_INDEX_DIR != '', "GRAPH_INDEX_DIR environment variable must be set"
        return GRAPH_INDEX_DIR

    @property
    def BM25_INDEX_DIR(self):
        BM25_INDEX_DIR = os.environ.get("BM25_INDEX_DIR")
        assert BM25_INDEX_DIR != '', "BM25_INDEX_DIR environment variable must be set"
        return BM25_INDEX_DIR

config = Config()