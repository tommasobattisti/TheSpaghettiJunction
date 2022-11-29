# Work connections on Wikidata: a preliminary analysis and report

>**Note**<br>
>Data's last update: Nov, 29 2022

## Introduction 
This document is compiled with the purpose of presenting preliminary analysis regarding 'The Spaghetti Junction' project. In particular, a prior study is necessary in order to comprehend data and properties' inner connections within Wikidata. The aim is to investigate resources and determine how they can be used to fulfill research questions so that the project would be suitable for opening up the work to wider future perspectives.
In this regard, the two primary sections that compose the document are specifically listed below:
  1. The first section considers the comparison between the results extracted from queries in Wikidata and the corresponding categories in Wikipedia. The purpose of this analysis is to estimate potential divergencies in terms of representation and amount of available data to process. 
  2. The second section focuses on a specific case study: the preliminary research in this regard concern the possibility of quantifying links on Wikidata about literary works by Italian authors and the audiovisual works that derive from them.

More specifically, a detailed table of contents is provided in the following section.

## Content
- [Work connections without works' class restriction](#Work-connections-without-works'-class-restriction)
- [Works connections with works' class restrictions](#Works-connections-with-works'-class-restrictions)
- [The case of Italian literature and international cinema and television](#The-case-of-Italian-literature-and-international-cinema-and-television)
  - [Authors, works, and derivative works on Wikidata only](#Authors-works-and-derivative-works-on-Wikidata-only)
  - [Authors and derivative works by mixing sources (Wikidata and IMDb)](#Authors-and-derivative-works-by-mixing-sources-(Wikidata-and-IMDb))
  - [Final comparison and conclusion](#Conclusion)

## Work connections without works' class restriction
The results shown in this section are contained in [this notebook](https://github.com/tommasobattisti/ilos/blob/main/sparqlQueries/finalQueriesGeneral.ipynb).

In this section, under both the label "work" and “derivative work” any kind of work or format can be found. Moreover, the variable "creator" used in the queries does not include only people (intended as single individuals), but also bands or other group-based organisations.

### With no definition of "work" and "derivativeWork" in the queries

The table presents the results of the queries in which works and derivative works are defined only in terms of the relation occurring between them (made explicit by means of the specified properties).

| SUBJ | PROPERTY | OBJ | WORK/ PERSON COUNT | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 10523 | 10249 |
| derivative work | P144 based on | work | 34834 | 52736 |
| derivative work | P941 inspired by | work | 5448 | 5285 |
| derivative work | P8371 references work | work | 1250 | 591 |
| work | P4969 derivative work | derivative work | 9265 | 15959 |
| derivative work | P1877 after a work by | person | 4830 | 12188 |

|  | DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 86683 |

### With explicit definition of "work" only

The table presents the results of the queries in which **only works** are defined in terms of "anything having an author or a creator" by means of `P170` (creator) and `P50` (author) properties.

| SUBJ | PROPERTY | OBJ | WORK/ PERSON COUNT | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 438 | 739 |
| derivative work | P144 based on | work | 18822 | 32141 |
| derivative work | P941 inspired by | work | 1601 | 1766 |
| derivative work | P8371 references work | work | 605 | 364 |
| work | P4969 derivative work | derivative work | 9265 | 15959 |
| derivative work | P1877 after a work by | person | 3898 | 10900 |

|  | DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 44386 |

### With explicit definition of "derivativeWork" only

The table presents the results of the queries in which **only derivative works** are defined in terms of "anything having an author or a creator" by means of `P170` (creator) and `P50` (author) properties.

| SUBJ | PROPERTY | OBJ | WORK/ PERSON COUNT | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 526 | 325 |
| derivative work | P144 based on | work | 9461 | 12684 |
| derivative work | P941 inspired by | work | 2281 | 2145 |
| derivative work | P8371 references work | work | 901 | 248 |
| work | P4969 derivative work | derivative work | 4376 | 5709 |
| derivative work | P1877 after a work by | person | 1685 | 5103 |

|  | DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 2366 |

### With explicit definition of both "work" and "derivativeWork"

The table presents the results of the queries in which **both works and derivative works** are defined in terms of "anything having an author or a creator" by means of `P170` (creator) and `P50` (author) properties.

| SUBJ | PROPERTY | OBJ | WORK/ PERSON COUNT | DERIVATIVE WORK COUNT |
| --- | --- | --- | --- | --- |
| derivative work | P737 influenced by | work | 185 | 172 |
| derivative work | P144 based on | work | 7494 | 10025 |
| derivative work | P941 inspired by | work | 892 | 956 |
| derivative work | P8371 references work | work | 494 | 184 |
| work | P4969 derivative work | derivative work | 3850 | 5084 |
| derivative work | P1877 after a work by | person | 1401 | 4531 |

|  | DERIVATIVE WORKS |
| --- | --- |
| ALL PROPERTIES UNION | 18347 |

---

## Works connections with works' class restrictions
The results shown in this section are contained in [this notebook](https://github.com/tommasobattisti/ilos/blob/main/sparqlQueries/finalQueriesLiteratureandFilms.ipynb).

In order to define the literary works, the following classes have been used:
- `Q47461344`: written work
- `Q7725634`: literary work
- `Q57`: book
- `Q3331189`: edition

For what concerns the derivative works, it has been decided to focus on works having a director. This allowed to retrieve entities ranging from films to theatre performances and plays, including also Tv series and other entities of similar classes. For this purpose, only the presence of the property `P57`(director) has been used to filter the derivative works.

>**Note**<br>
>No restriction dealing with works' provenance have been applied.


### With the explicit definition of "work" only

| DERIVATIVE WORKS |
| --- |
| 25819 |

### With the explicit definition of "derivativeWork" only

| DERIVATIVE WORKS |
| --- |
| 19654 |

### With both definitions

| DERIVATIVE WORKS |
| --- |
| 13612 |
__________


## The case of Italian literature and international cinema and television
The results shown in this section are contained in [this notebook](https://github.com/tommasobattisti/ilos/blob/main/sparqlQueries/finalQueriesItalianLiterature.ipynb). In particular, the queries used can be found in the `writers_works_and_derivatives` and `derivatives_type` notebook's section.

By restricting the context to the influence of italian literature in international cinema and television related productions, it is possible to better grasp the magnitude of wikidata's lack of connection between artistic works.
In particular, the aim of this section is to compare what can be found using wikidata only, and what is possible to retrieve by extending the search by means of external sources (in this case, IMDb).

### Authors, works, and derivative works on Wikidata only
#### Definitions
Italian authors are people that live or lived in Italy or any historical country that, nowadays, has been definitely replaces by `Q38` (Italy), that have created at least one literary work, and that are described, in a non exlusie way, with at least one of these classes:
- `Q36180` (writer)
- `Q6625963` (novelist
- `Q49757` (poet)
- `Q12144794` (prosaist)
- `Q28389` (screenwriter)

A work is, in this case, any literary work defined as either one of the following:
- `Q47461344` (written work)
- `Q7725634` 8literary work)
- `Q571` (book)
- `Q3331189`(edition)

A derivative work is everything with at least one of the following charcateristics:
- Being influenced by (`P737`) a work
- Being based on (`P144`) a work
- Being inspired by (`P941`) a work
- Having a work as reference (`P8371`)
- Being derived from (`P4969`)
- Being inspired by a person's work (`P1877`)

#### Results
The following table highlights the number of authors of a literary work, where the latter has, in turn, at least one derivative work linked on Wikidata:

| ENTITY | COUNT |
| --- | --- |
| authors | 122 |
| works | 1269 |
| derivative works | 456 |

However, it is worthy of attention that the derivative works can be of any kind. More precisely, the following table shows the count of derivative works by type:

| Class label |	Count |
|  ---  | --- |  
| film	| 143 |
| literary work	| 53  |
| theatrical production |	49  |
| dramatico-musical work	| 42  |
| operatic production |	22  |
| painting	| 18  |
| miniseries  |	14  |
| television film |	12  |
| television series |	12  |
| teleplay  |	12  |
| musical work/composition	| 10 |
| animated feature film | 8 |
| version, edition, or translation  | 6 |
| video game  | 5 |
| Others |	84 |

So, cinema and television related derivative works are 201, including films, miniseries, television films, television series, teleplay, and animated feature films. By supposing, for simplicity, that all the 84 other works are of our interest (you can check the notebok to see that actually only a few of them are significant for our topic of inquiry), we would have 285 derivative works of interest.

### Authors and derivative works by mixing sources (Wikidata and IMDb)
As shown in [Battisti and Daquino, 2022](https://doi.org/10.6092/issn.2532-8816/14514), by combining the results of a SPARQL query aimed at retrieving italian authors having an identifier on IMDb, with information about the adio-visual product they are related to on IMDb, it has been prooved that the extracted italian authors have contributed to 2061 works on IMDb.

By manually cheching the type of contribution for every product on IMDb, we can say with certainty that at least **1388** are the works on IMDb derived from the work of an italian literary author.

The SPARQL query and the Python code used to query Wikidata and IMDb API can be found on [figshare](https://figshare.com/articles/software/Python_code_for_IMDb_API/17008273/1).

#### Some clarification
First, the query to Wikidata used to retrieve initial informatio about the authors includes only italian authors with this chracteristics:
- Having the citizenship related to Italy (`Q38`) or Kingdom of Italy (`Q172579`)
- Being classified as novelist (`Q6625963`) or poet (`Q49757`)
This specidfications are way more restrictive than the ones used for the queries in the [previous section](#Authors-works-and-derivative-works-on-Wikidata-only), and therefore are able to get only a portion of the authors that the previos query could have retrieved if it would have stopped at this point. 

Furthermore, IMDb does not provide any explicit link to the work a film or a tv series is derived from. Moreover, from the initial information retrieved, the dataset used in the paper contains only information related to **cinematografic films**, **television films**, **tv series**, and **tv miniseries**.

### Final comparison and conclusion
The results of the inquiry made on Wikidata only include derivative works or different kind. By considering not only audiovisual derivative works, however, their number is still less than a half of the audiovisual derivative works retrieved by using mixed sources. In addition to that, this difference assumes even more relevance if it is considered that in the latter case, author's occupations possible values, as well as the age in which they could have lived, are way more restrictive.
