# The Spaghetti Junction


## 1. Overview

**Username**: emmedaquino

**Project title**: The Spaghetti junction. Linking literature and cinema in Wikidata

**Entity receiving funds**: University of Bologna

## 2. Research proposal

### 2.1 Description

Literature enthusiasts and movie geeks spend significant efforts in linking Wikipedia pages under [categories](https://en.wikipedia.org/wiki/Category:Lists_of_films_based_on_books), in dedicated [pages](https://en.wikipedia.org/wiki/List_of_films_based_on_film_books), or editing sections (e.g. *Adaptations*). Some [WikiProjects](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Film/Films_based_on_books/Worklist) and [task forces](https://wiki.alquds.edu/?query=Wikipedia:WikiProject_Film) have defined priorities and contributed to enrich Wikipedia with links between works. Unfortunately, only ~33% of such links between movies and literary works exist in Wikidata (WD) (see our [preliminary analysis](https://github.com/tommasobattisti/TheSpaghettiJunction.git)). 

Nonetheless, having such links between QIDs and/or emerging entities (i.e. not yet in Wikidata) would significantly impact quantitative **transmedia and multi-modal research**. An open graph connecting a wide variety of media types would open up new avenues of research for scholars interested in media studies.

Entity linking is a challenging task, encompassing knowledge extraction from multilingual texts, entity disambiguation, counter-fact checking, and candidate ranking. WD users have requested support for related tasks (e.g. [1](https://meta.wikimedia.org/wiki/Community_Wishlist_Survey_2022/Wikidata/Import_references_from_wikipedia), [2](https://meta.wikimedia.org/wiki/Community_Wishlist_Survey_2021/Bots_and_gadgets/Importing_data_from_IMDb)). To date, several datasets leveraging the WD knowledge graph and Wikipedia exist to cope with similar tasks ([Möller et al. 2021](https://arxiv.org/pdf/2112.01989.pdf)). Popular approaches make use of language models, graph embeddings and other statistical methods, which can be fine-tuned and re-assessed. However, such approaches may fail if the target graph is incomplete, thus requiring data integration, and reliable results depend on authoritative sources for counter-fact checking. To date, links between movies and literary works are available in proprietary databases (with reliability limitations and restrictions on reuse) such as the Internet Movie Database, where novelists are mentioned as participants but not the work that inspired the movie (if any).

In this project, we propose a holistic approach (based on the aforementioned literature) to identify, disambiguate, and rank candidate links between literary works and derivative movies extracted from Wikipedia pages, categories, and online web sources (e.g. VIAF, OpenLibrary) and confirmed by experts (e.g. in [Rotten Tomatoes](https://en.wikipedia.org/wiki/Rotten_Tomatoes) and [Metacritic](https://en.wikipedia.org/wiki/Metacritic)). We enrich Wikidata with links between existing items (extracted with high confidence) and we generate a Linked Open Dataset with links to emerging items. Links can be reviewed via interface by WD editors, who can explore the Spaghetti graph and assess links to be used when creating a new entity. To evaluate our work, we realise a prototype on Italian literature and international movies and TV series.

### 2.2 Budget

*Approximate amount requested in USD: 40.000$ (1EUR → 1.06USD)*

**Budget Description:  UNIBO is the only beneficiary**

- Salary or stipend: 19.200 EUR for a 1-year fellowship; up to 9.600 EUR for a 6-month fellowship
- Open Access Publishing costs: 0 EUR, we can benefit of some agreement with publishers and gold OA journals
- Conference and travel expenses: 2000 EUR
- Institutional overhead: 4000 EUR
- Equipment: 1 laptop (3000 EUR)

### 2.3 Impact

We contribute in filling gaps on topics of potential impact (*[2030 Wikimedia Strategic Direction](https://meta.wikimedia.org/wiki/Strategy/Wikimedia_movement/2018-20/Recommendations)*), namely:

- **Align Wikipedia and Wikidata**. We publish trusted links between QIDs, to improve WD users’ experience
- **Recommend new links.** We offer to developers, researchers and WD editors a LOD source (under CC0 license) including links between works not yet in WD (identified with appropriate IDs). A web interface allows them to look for a work, retrieve and assess candidate links, as well as a pop-up widget suggests links when editing WD items.
- **Create scalable, reusable methods**. We inform Wiki communities on how to reuse and scale up our methods to create links between works of any kind and any nationality.

### 2.4 Dissemination

We plan to publish up to 3 articles in open access journals and conference proceedings. Among the conferences and workshops of interest, we identified the Wiki Workshop (Web Conference 2024), Wikidata Workshop (ISWC 2024), WikidataCon 2024, and AIUCD 2024. Journals of interest include Digital Scholarship in the Humanities, Umanistica Digitale, Journal On Computing and Cultural Heritage and journals on media studies to be identified. Results will be presented in seminars/hack days.

### 2.5 Past contributions

- M. Daquino, Assistant professor at UNIBO. Grant Wikicite: Wikipedia Citations in Wikidata, several articles leveraging Wikidata ([Scholar](https://scholar.google.it/citations?user=HomzePYAAAAJ&hl=it): CLEF, ARTchives).
- D. Metilli, research fellow at UCL. Grant WiGeDi, former Wikipedia/Wikidata administrator and Wikipedian in Residence, research papers based on Wikidata ([Scholar](https://scholar.google.com/citations?user=SFvyNLIAAAAJ&hl=en&oi=ao))

## 3. Feedback

- Who we are in touch within the Wiki communities
- advertisement of the proposal in the community (mailing lists, contact people in WikiProjects, social media platforms, blog posts, participation in community events)
- endorsement?
