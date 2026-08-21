from sqlalchemy import create_engine

engine = create_engine("sqlite:///universidad.db", echo=False)
#el echo es para ver que hace internamente la db y lo imprime por consola
