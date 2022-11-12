from io import StringIO
import pandas as pd
from SPARQLWrapper import CSV, POST, POSTDIRECTLY, SELECT, SPARQLWrapper

# Wikidata has a specific User-Agent policy reachable at https://www.wikidata.org/wiki/Wikidata:Project_chat/Archive/2019/07#problems_with_query_API
# and https://meta.wikimedia.org/wiki/User-Agent_policy
#Therefore, we add the possibilty to specify the user agent

def query_wikidata(endpoint, query, user_agent=False, post=False):
    if user_agent:
        sparql = SPARQLWrapper(endpoint, agent= user_agent)  
    else:
         sparql = SPARQLWrapper(endpoint)
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