import pandas as pd
from pandas.io.json import json_normalize
from SPARQLWrapper import SPARQLWrapper, JSON
from io import StringIO
from SPARQLWrapper import SPARQLWrapper, CSV, SELECT, POST, POSTDIRECTLY


def query_wikidata(endpoint, query, user_agent, post=False):
    """
    Query the endpoint with the given query string and return the results as a pandas Dataframe.
    """
    # create the connection to the endpoint
    # Wikidata enforces now a strict User-Agent policy, we need to specify the agent
    # See here https://www.wikidata.org/wiki/Wikidata:Project_chat/Archive/2019/07#problems_with_query_API
    # https://meta.wikimedia.org/wiki/User-Agent_policy
    sparql = SPARQLWrapper(endpoint, agent= user_agent)  
    
    sparql.setQuery(query)

    if post:
        sparql.setOnlyConneg(True)
        sparql.addCustomHttpHeader("Content-type", "application/sparql-query")
        sparql.addCustomHttpHeader("Accept", "text/csv")
        sparql.setMethod(POST)
        sparql.setRequestMethod(POSTDIRECTLY)

    sparql.setReturnFormat(CSV)
    results = sparql.query().convert()
    _csv = StringIO(results.decode('utf-8'))
    return pd.read_csv(_csv, sep=",")