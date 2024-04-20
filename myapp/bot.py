from langchain_openai import OpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import sqlite3

def fn_bot(question):
    conn = sqlite3.connect("db.sqlite3")
    with conn:
        db = SQLDatabase.from_uri("sqlite:///db.sqlite3")
        llm = OpenAI(temperature=0, api_key="") #setup openai api key and update here
        db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
        result=db_chain.run(question)
        # print(result)
    conn.close()
    return result




