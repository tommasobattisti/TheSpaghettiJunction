# Work connections on Wikidata: a preliminary analysis and report

>**Note**<br>
>Data's last update: Dec, 06 2022

## Introduction and contents
This document is compiled with the purpose of presenting some preliminary analyses for 'The Spaghetti Junction' project.

In particular, this study is a necessary step in order to better comprehend our subject of inquiry from the perspective of data and properties' inner connections within Wikidata. The aim is to draw a clear path that goeas from the particular to the more general context capable of highlighting connections-related lacks on Wikidata and potential contexts of enrichment.

An introductury analysis with a comparison of the connections between novels and films existing in both Wikipedia and Wikidata is followed by a "case study"-based evidence of the results achievable if Wikdata had more connections by using it combined with external sources. Finally, a broader inquiry shows what is the potential reach of the project by demonstrating how completely different entities (both creative and non creative works) are connected by means of the same properties, inducing us to think about the project's future perspectives and the possible benefits it would bring to Wikidata.

In this regard, the sections composing the document are:
  1. [Wikipedia categories vs. Wikidata](##wikipedia-categories-vs-wikidata) The first section highlights the results of the comparison between what can be extracted by querying Wikidata in terms of films based on novels and the data that can be found in the Wikipedia categories aimed at describing the same phenomenon. The purpose of this analysis is to estimate potential divergencies in terms of representation and amount of available data. 
  
  2. [The case of Italian literature and international cinema and television](#The-case-of-Italian-literature-and-international-cinema-and-television) The second section focuses on a specific case study: Italian literature and international cinema and television. The possibility of quantifying links on Wikidata about literary works by Italian authors and derivative audiovisual works is compared with the amount of data that can be retrieved by combining Wikidata potential with an external source (in this particular case, IMDb).
  
  3. [Written and audiovisual works linking](#Written-and-audiovisual-works-linking) Given the results of the previous sections, the third one starts to extend the point of view by moving the focus on the relations between written and audiovisual works in general. 
  
  4. [Retrieving connections between generic works](#Retrieving-connections-between-generic-works) In this final section, the context is even more enrlarged. In fact, while still dealing with the reletionship bewteen works and derivative works, the analysis take into account entities without considering their nature. Not only written or audiovisual works are retrieved here, but any kind of work derived from another work and vice versa.

The last two sections contain alsotables useful to better appriciate and compare how different propertie of our interest are used for entities linking.
_____________________________

## 1. Wikipedia categories vs. Wikidata

The results shown in this section come from the queries contained into [this notebook](https://github.com/tommasobattisti/TheSpaghettiJunction/blob/main/sparqlQueries/wikiVsWiki.ipynb) and refer to the sections 1.2, 2.2 and 2.3. The Wikipedia categories have been analyzed by means of the [categories.py](https://github.com/tommasobattisti/TheSpaghettiJunction/blob/main/categories/categories.py) file, which can be run directly via an IDE or by running `python 3 categories.py -c "Films based on novels" -j` from terminal.

This first section focuses on comparing the number of films **based on** novels that can be found by parsing the different Wikipedia categories and the ones obtained by querying Wikidata. Note that this specific analysis is just the starting point for highlighting a lack of connections in Wikidata that is reflected in a definitely bigger context.

Wikipedia categories have been retrieved by focusing on the “based on” relation between **novels** and **films**. Therefore, also on Wikidata the property used to filter the results is `P144` ("based on"), while the films are everything being an instance of `Q11424` ("film") or one of its subclasses (recursively).

We were able to find (section 1.2 or by running categories.py) that the Wikipedia pages related to films contained into the categories of our interest are **12972**.

In general, films based on novels that can be found on Wikidata (section 2.2) are approximatively **4968**.

However, as it can be seen by running the categories.py file - which also makes multiple queries to Wikidata - it is possible to see that only the **33,27%** (**4316**) of the initial **12972** works have a linked entity on Wikidata, which bear in turn another general connection of type “based on” (`P144`).

In summary, it is of great importance the fact that approximatively the 67% of works connections between films and novels covered by Wikipedia are not covered by Wikidata. In order to be clear, it has to be underlined the fact that the analysis focuses on the English Wikipedia only. Therefore, the results can be still thought as incomplete.

## 2. The case of Italian literature and international cinema and television

The results shown in this section come from the queries contained into [this notebook](https://github.com/tommasobattisti/TheSpaghettiJunction/blob/main/sparqlQueries/ItalianLiterature.ipynb).

By restricting the context to the influence of Italian literature in international cinema and television related productions, it is possible to better grasp the magnitude of Wikidata's lack of connections between artistic works.
In particular, the aim of this section is to compare what can be found using Wikidata only, and what it is possible to retrieve by extending the search by means of external sources (in this case, IMDb).

### 2.1 Authors, works, and derivative works on Wikidata only

### Definitions

Italian authors are defined as people that live or lived in Italy or in any historical country that, nowadays, has been definitely replaced by `Q38` (Italy), and that have created at least one work.

A work is, in this case, any literary work defined as an instance of either `Q47461344` (written work) or `Q7725634` (literary work) or any of its subclasses.

Moreover, a derivative work is everything with at least one of the following characteristics:

- Being influenced by (`P737`) a work
- Being based on (`P144`) a work
- Being inspired by (`P941`) a work
- Having a work as reference (`P8371`)
- Being derived from (`P4969`)
- Being inspired by a person's work (`P1877`)

### Results

The following table highlights the number of authors of a literary work, where the latter has, in turn, at least one derivative work linked on Wikidata (data are taken form the above linked notebook, section 2.1):

| Authors | Works derived from authors’ literary works |
| --- | --- |
| 184 | 747 |

However, it is worthy of attention that the derivative works can be of any kind.

For the purpose of this section, another query is aimed at focusing only on derivative works that are instances of film (`Q11424`), television product (`Q15416`), or any of their subclasses. The results are reported here (data are taken form the above linked notebook, section 2.2):

| Authors | Films and tv products derived from authors’ works |
| --- | --- |
| 122 | 289 |

So, films and television products that derive from Italian authors’ written works in Wikidata are 289. 

### Authors and derivative works by mixing sources (Wikidata and IMDb)

As shown in [Battisti and Daquino, 2022](https://doi.org/10.6092/issn.2532-8816/14514), by combining the results of a SPARQL query aimed at retrieving Italian authors having an identifier on IMDb, with information about the audio-visual product they are related to on IMDb, it has been proved that the extracted Italian authors have contributed to 2061 works present on IMDb.

The SPARQL query and the Python code used to query Wikidata and IMDb API can be found on [figshare](https://figshare.com/articles/software/Python_code_for_IMDb_API/17008273/1). Moreover, since the reported results dated back to the time in which the analysis has been performed, the same query is reported also in the above linked notebook in section 3.1.

It is important to mention the fact that data have been pre-processed and only the ones that were referred to specific derivative works (**cinematographic films**, **television films**, **tv series**, and **tv miniseries**) have been kept for the analysis. The final number of authors was, therefore, ******154******. To get an idea of the starting number of authors it is possible to look at the dataset published on [figshare](https://figshare.com/articles/dataset/Initial_dataset/16782781). By filtering it by authors’ id, it is possible to see that, after the extraction of data from IMDb, the starting number of authors was **167**.

By manually checking the type of contribution for every product on IMDb (as explained in the paper), we can say with certainty that at least **1388** are the works on IMDb derived from the work of an Italian literary author (while the other contributions consisted in being directly involved in the writing of the screenplay).

| Paper’s starting number | Maintained authors | Films and tv products derived from authors’ works |
| --- | --- | --- |
| 167 | 154 | 1388 |

### Discussion

First, the query to Wikidata used to retrieve initial information about the authors includes only Italian authors with this characteristics:

- Having the citizenship related to Italy (`Q38`) or Kingdom of Italy (`Q172579`)
- Being classified as novelist (`Q6625963`) or poet (`Q49757`)

These specifications are way more restrictive than the ones used for the queries in the [previous section](https://www.notion.so/Bozza-README-dce0f5746b81436fb5f0bde379959c7a). Thus, the paper’s query is able to get only a portion of the authors that the query in section 2.2 could have retrieved if it would have been composed by the same triple paths.

In fact, as shown in section 3.2 of the mentioned notebook, by copying the query used for the papers and replacing the most restrictive parts (the ones cited above) with the ones used for the other queries (listed [here](#Definitions)), we obtain a bigger number of results.

| Paper’s initial authors | Authors (section 3.1) | Authors (section 3.2) |
| --- | --- | --- |
| 167 | 234 | 549 |

Thus, if the 154 maintained authors derived from a query that is now able to produce 234 results and that, at the time of the paper’s analysis produced 167 results after the extraction of data from IMDb, we can imagine that the number of “maintainable” authors derivable from the query producing 549 results would be even higher. As a direct consequence, if 1388 derivative works have been retrieved starting from 167 authors, what could we expect with 549 as the starting number?

In this case we won’t reproduce the whole process extracting data from IMDb for the 549 writers. Thus, our final conclusions will be drawn on the paper’s data.

|  | Wikidata only (m.p.q)(n.pp) | Wikidata and IMDb (l.p.q)(pp) | Wikidata and IMDb (m.p.q)(n.pp) |
| --- | --- | --- | --- |
| Authors | 122 | 154 | 549 |
| Derivative works (audiovisual) | 289 | 1388 | ? |

Where ***m.p.q.*** stands for “more powerful query”, ***l.p.q*** stands for “less powerful query” and ***n.pp*** and ***pp*** stands for not pre-processed and pre-processed respectively.

It is possible to see that even with a more complex and powerful query, the derivative works extracted from Wikidata alone are, approximatively, **only the** **20%** of the ones retrievable by mixing sources.

Nonetheless, it is important to specify once more that:

- The 1388 derivative works are the result of a precise pre-processing aimed at including only specific kind of works (e.g., excluding products such as short movies, etc.), while the 289 derivative works can include any kind of tv product and film in general.
- The query that obtains the larger number of derivative works is also the more restrictive in terms of characteristics an author has to have in order to be included in the final results.

## 3. Written and audiovisual works linking

Works and their derivatives are not confined in the realm of literature and films. Given the results of the two previous sections, this one is focused on enlarging the prospectives for what concerns derivative works in particular.

Moreover, the relationship between works and their derivatives is not always determined by the “based on” property. As we have [seen before](#Definitions), it is the occurrence of a manifold set of properties to lead to the definition of a work as “derivative work”. That is why, in this section, as well as in the one that will follow, the enlargement of the subject of inquiry goes hand in hand with a report on the usage of these properties.

The section aims at better understanding the State of the Art of Wikidata connections showing the influence of written works in the audiovisual sector. This analysis, if compared with the results discussed in the previous sections of the document, conveys a first insight of the potential range that could be reached by our enhancement proposal.

The results shown in this section come from the queries contained into [this notebook](https://github.com/tommasobattisti/TheSpaghettiJunction/blob/main/sparqlQueries/writtenAndAudiovisualWorks.ipynb).

### 3.1 Focus on written works and derivative films

For this section, **********works********** have been defined as instances of the classes `Q47461344` (written work), `Q7725634` (literary work), or any of the latter’s subclasses. Derivative works have been defined as instances of `Q11424` (film) or any of its subclasses.

For each query in the **section 2** of the notebook (where the reported data come from), a different property has been used to connect **********works********** to their ********************************derivative works********************************. The table below shows the different use of these properties:

| SUBJ | PROPERTY | OBJ | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 5 |
| derivative work | P144 based on | work | 11324 |
| derivative work | P941 inspired by | work | 191 |
| derivative work | P8371 references work | work | 39 |
| work | P4969 derivative work | derivative work | 101 |
| derivative work | P1877 after a work by | person (the author of a written work) | 5286 |

Since many derivative works are connected to works by means of different properties, all the results’ URIs have been added to a set to determine the exact number of derivative works touched by the previously described triple paths (a single query to take track of everything caused time-out problems, so we had to split the process in more queries).

|  | DISTINCT DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 11585 |

### 3.2 Focus on written works and audiovisual derivative works

For this section, **********works********** have been defined as instances of the classes `Q47461344` (written work), `Q7725634` (literary work), or any of the latter’s subclasses. Derivative works have been defined as instances of `Q2431196` (audiovisual works) or any of its subclasses.

For each query in the **section 1** of the notebook (where the reported data come from), a different property has been used to connect **********works********** to their ********************************derivative works********************************. The table below shows the different use of these properties:

| SUBJ | PROPERTY | OBJ | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 11 |
| derivative work | P144 based on | work | 14956 |
| derivative work | P941 inspired by | work | 265 |
| derivative work | P8371 references work | work | 89 |
| work | P4969 derivative work | derivative work | 288 |
| derivative work | P1877 after a work by | person (the author of a written work) | 5882 |

Since many derivative works are connected to works by means of different properties, all the results’ URIs have been added to a set to determine the exact number of derivative works touched by the previously described triple paths (a single query to take track of everything caused time-out problems, so we had to split the process in more queries).

|  | DISTINCT DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 16510 |

## 4 Retrieving connections between generic works

This last section report data related to the connection of what we can define as generic works. The focus is no more restricted to the context of written and audiovisual works and everything that is connected by the previously used properties counts as a result. This means that both creative and non-creative works are included.

In this last section tables also report the number of works to which the derivative works are connected.

Data gathered for this section come from [this notebook](https://github.com/tommasobattisti/TheSpaghettiJunction/blob/main/sparqlQueries/generalWorksRelations.ipynb).

### 4.1 Focusing on what has an author or a creator

The following table presents the results extracted by the queries in the previously linked notebook in section 2. More specifically in every subsection ending with a 4 (e.g., 2.1.4, 2.2.4, 2.3.4, etc.).

Works and derivative works are both defined on the basis of the previously used properties, on the presence of an author (`P50`) or a creator (`P170`) for the work, or on the presence of the opera in an author’s list of works (`P1455`) or relevant works (`P800`).

| SUBJ | PROPERTY | OBJ | WORK/ PERSON COUNT | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 187 | 176 |
| derivative work | P144 based on | work | 7591 | 10148 |
| derivative work | P941 inspired by | work | 900 | 964 |
| derivative work | P8371 references work | work | 498 | 188 |
| work | P4969 derivative work | derivative work | 4440 | 5790 |
| derivative work | P1877 after a work by | person | 1409 | 4546 |

The following data reports the number of distinct derivative works found by using all the properties in the same query. The query can be found in section 1.4.

|  | DISTINCT DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 18546 |

### 4.2 Works with no restriction

The only things that works and derivative works should have to be included in the following table are the properties we used to analyze their connections. Data are gathered from the section 2 of the previously linked notebook. More specifically, the queries used can be found in the subsections ending with a 1 (e.g. 2.1.1, 2.2.1, 2.3.1, etc.).

| SUBJ | PROPERTY | OBJ | WORK/ PERSON COUNT | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 10625 | 10324 |
| derivative work | P144 based on | work | 35144 | 53218 |
| derivative work | P941 inspired by | work | 5541 | 5392 |
| derivative work | P8371 references work | work | 1254 | 597 |
| work | P4969 derivative work | derivative work | 9404 | 16163 |
| derivative work | P1877 after a work by | person | 4851 | 12259 |

The following data reports the number of distinct derivative works found by using all the properties in the same query. The query can be found in section 1.1.

|  | DISTINCT DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 87498 |
