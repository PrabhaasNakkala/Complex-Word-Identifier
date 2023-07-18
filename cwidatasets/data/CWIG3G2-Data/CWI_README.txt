CWI datasets for English, German, and Spanish
==============================================

Distributed by the LT group at Universität Hamburg, Germany, October 2017.
contact email: yimam@informatik.uni-hamburg.de
web: http://lt.informatik.uni-hamburg.de


Introduction
------------

Complex word Identification (CWI) is a sub-task of lexical simplification (LS), which identifies difficult words or phrases in a text. There are very few CWI datasets available, and mostly limited to English language. To alleviate this problem, we have collected CWI datasets for English, German, and Spanish.

Data set collection procedures
------------------------------

We collected complex word and phrase annotations (sequences of words, up to maximum 50 characters) using the Amazon Mechanical Turk (MTurk) crowdsourcing platform, from native and non-native English, German, and Spanish speakers.  We collect annotations using MTurk, on a paragraph-level HIT (Human Intelligence Task), which is 5-10 sentences long.

The English datasets consists of three genres:

* Professionally written news
* News written by amateurs (WikiNews)
* Wikipedia articles

The German and Spanish datasets are compiled from German Wikipedia and Spanish Wikipedia articles.

Files
-----
The zip file contains this README file and three sub folders, namely English, German, and Spanish.
Under each sub folder, there are both training and development annotation files.
The test files are currently held back, as we are preparing a shared task on multilingual CWI.

For English, there are the following files:

## development and training dataset the news genre, with annotations
English_News_Train.tsv (6515 lines, 1500943 bytes)
English_News_Dev.tsv (824 lines  186306 bytes)

## development and training dataset for news genre, all the sentences in a HIT with out the actual annotations
English_News_HITs_Train.tsv (180lines, 153004 bytes)
English_News_HITs_Dev.tsv (23lines, 19225 bytes)

## development and training dataset the Wikinews genre, with annotations
English_WikiNews_Train.tsv (99 lines, 89136 bytes)
English_WikiNews_Dev.tsv (476 lines, 102916 bytes)

## development and training dataset for Wikinews genre, all the sentences in a HIT with out the actual annotations
English_WikiNews_HITs_Train.tsv (3878 lines, 864816 bytes)
English_WikiNews_HITs_Dev.tsv (13 lines, 11525 bytes)

## development and training dataset the Wikipedia genre, with annotations
English_Wikipedia_Train.tsv (2903 lines, 673747 bytes)
English_Wikipedia_Dev.tsv (369 lines, 79832 bytes)

## development and training dataset for Wikipedia genre, all the sentences in a HIT with out the actual annotations
English_Wikipedia_HITs_Train.tsv (81 lines, 63281 bytes)
English_Wikipedia_HITs_Dev.tsv (10 lines, 8014 bytes)

For German, there are the following files
## development and training dataset, with annotations
German_Train.tsv (2629 lines, 618781 bytes)
German_Dev.tsv (325 lines, 70478 bytes)

## development and training dataset, all the sentences in a HIT with out the actual annotations
German_HITs_Train.tsv (85 lines, 91609 bytes)
German_HITs_Dev.tsv (11 lines, 11937 bytes)

For Spanish, there are the following files
## development and training dataset, with annotations
Spanish_Train.tsv (5601 lines, 2954656 bytes)
Spanish_Dev.tsv (701 lines, 312785 bytes)

## development and training dataset, all the sentences in a HIT with out the actual annotations
Spanish_HITs_Train.tsv (141 lines, 166885 bytes)
Spanish_HITs_Dev.tsv (18 lines, 19161 bytes)


Data formats
------------

These datasets contain information about complex phrases annotated with some statistics. Each line represents a sentence with one complex phrase (CP) annotation and relevant information, each separated by a TAB character.

* First column shows the HIT ID of the sentence. All sentences with the same ID belong to the same HIT.
* Second column shows the actual sentence where there exists a complex phrase annotation.
* The third and fourth columns display the start and end offsets of the complex phrase annotation in this sentence.
* The fifth column represents the actual complex phrase annotation.
* The sixth, seventh, and eighth columns show the number of native annotators, the number of non-native annotators and the total number of annotators who have marked this complex phrase.

Examples
--------

ID1     Both China and the Philippines flexed their muscles on Wednesday.      31      37      flexed                            2      7    9

ID1     Both China and the Philippines flexed their muscles on Wednesday.      31       51     flexed their muscles   4    2   6

Here, we can see that the phrase "flexed" is marked as complex phrase by 2 native and 7 non-native English speakers where as the phrase "flexed their muscles" is marked by 4 native and 2 non native English speakers.

Download
--------

The datasets are available from
https://www.inf.uni-hamburg.de/en/inst/ab/lt/resources/data/complex-word-identification-dataset.html

License
-------
The data is distributed under CC-BY 4.0 license, see https://creativecommons.org/licenses/by/4.0/ for details

Publications
------------
Please cite one of these publications, if you use the data in your research:

* Seid Muhie Yimam, Sanja Štajner, Martin Riedl, and Chris Biemann (2017): CWIG3G2 - Complex Word Identification Task across Three Text Genres and Two User Groups. In Proceedings of The 8th International Joint Conference on Natural Language Processing (IJCNLP 2017). Taipei, Taiwan [For English data in different genres]
* Seid Muhie Yimam, Sanja Štajner, Martin Riedl, and Chris Biemann (2017): Multilingual and Cross-Lingual Complex Word Identification. In Proceedings of The 2017 International Conference on Recent Advances in Natural Language Processing (RANLP). Varna, Bulgaria [for multilingual data]
