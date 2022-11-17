# Work connections on Wikidata: a preliminary analysis and report

## Content
- [Work connections without works' class restriction](#Work-connections-without-works'-class-restriction)
- [Works connections with works' class restrictions](#Works-connections-with-works'-class-restrictions)
- [The case of Italian literature](#The-case-of-Italian-literature)
  - [Authors, works, and derivative works on Wikidata only](#Authors-works-and-derivative-works-on-Wikidata-only)

## Work connections without works' class restriction
The results shown in this section are contained in [this notebook](https://github.com/tommasobattisti/ilos/blob/main/sparqlQueries/finalQueriesGeneral.ipynb).

>**Note**<br>
>Under both the label "work" and “derivative work” any kind of work or format can be found. Moreover, the variable "creator" used in the queries does not include only people (intended as single individuals), but also bands or other group-based organisations.

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


## The case of Italian literature
The results shown in this section are contained in [this notebook](https://github.com/tommasobattisti/ilos/blob/main/sparqlQueries/finalQueriesItalianLiterature.ipynb). In particular, the queries used can be found in the `writers_works_and_derivatives` and `derivatives_type` notebook's section.

By restricting the context to italian literature, it is possible to better grasp the magnitude of wikidata's lack of connection between artistic works.
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
| author | 122 |
| work | 1269 |
| derivative work | 456 |





