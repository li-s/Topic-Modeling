# Topic Modeling by Latent Dirichlet Allocation


Topic modeling views documents as a collection of various topics. It is not only used for exploring hidden semantic structures in new textual data, but for also complementing supervised machine learning in constructing and checking the accuracy of existing classification models.

In this repository, I chose to utilise Latent Dirichlet Allocation(LDA) for topic modeling. I trained LDA on a subset of the English wikipedia corpus, and found the top 20 topics of the texts found below. Furthurmore, I used the trained LDA to predict topic distributions on 3 seletected texts within the corpus(short_texts.txt), of which the result can be found below.

Through this process, I have written some other codes, such as comparing two matrixes using cosine similarity, or making and then compressing a .xml file.

## Implementation Details

1. Convert xml.bz2 file(wiki) to text file, and extract all text bodies. The first 10,000 texts are selected and saved(extracted_texts.txt). (See `xml1.py`)
2. Remove common and unique words, and non-english syllybus. (See `prune.py`)
3. Create and saves the dictionary(the_dictionary.dict). (See `prune.py`)
4. Create sparse vectors representing the token frequency in each text (text_vectors.txt). (See `prune.py`)
5. Train the Latend Dirichlet Analysis model. (See `lda.py`)
6. Predict topic distribution given a text. (See `lda_comparison.py`)

## Results

#### Top 20 topics of 10,000 texts in the english Wikipedia:
```
Topic 1: 0.008*"book" + 0.008*"name" + 0.007*"an" + 0.007*"titl" + 0.007*"cite" + 0.006*"journal" + 0.006*"univers" + 0.006*"publish" + 0.006*"this" + 0.005*"from"  

Topic 2: 0.012*"war" + 0.010*"name" + 0.010*"forc" + 0.007*"armi" + 0.007*"from" + 0.007*"air" + 0.007*"p" + 0.007*"militari" + 0.006*"first" + 0.006*"titl"  

Topic 3: 0.018*"name" + 0.017*"journal" + 0.015*"titl" + 0.015*"cite" + 0.010*"year" + 0.010*"page" + 0.008*"from" + 0.007*"volum" + 0.007*"publish" + 0.007*"date"  

Topic 4: 0.014*"state" + 0.010*"titl" + 0.010*"cite" + 0.008*"unit" + 0.008*"parti" + 0.008*"name" + 0.008*"nation" + 0.007*"date" + 0.007*"govern" + 0.007*"publish"  

Topic 5: 0.013*"use" + 0.010*"comput" + 0.009*"system" + 0.009*"web" + 0.008*"code" + 0.008*"titl" + 0.008*"com" + 0.008*"name" + 0.007*"cite" + 0.007*"an"  

Topic 6: 0.030*"math" + 0.012*"sub" + 0.008*"an" + 0.008*"sup" + 0.008*"this" + 0.007*"titl" + 0.006*"number" + 0.006*"f" + 0.006*"mathemat" + 0.006*"first"  

Topic 7: 0.036*"languag" + 0.012*"use" + 0.009*"from" + 0.008*"word" + 0.007*"name" + 0.006*"titl" + 0.005*"other" + 0.005*"also" + 0.005*"an" + 0.005*"which"  

Topic 8: 0.020*"player" + 0.019*"politician" + 0.016*"footbal" + 0.015*"day" + 0.014*"author" + 0.014*"singer" + 0.012*"actor" + 0.011*"french" + 0.010*"born" + 0.009*"songwrit"  

Topic 9: 0.029*"music" + 0.009*"use" + 0.009*"instrument" + 0.008*"from" + 0.007*"play" + 0.006*"danc" + 0.006*"an" + 0.006*"compos" + 0.005*"which" + 0.005*"string"  

Topic 10: 0.026*"style" + 0.018*"color" + 0.017*"small" + 0.017*"background" + 0.011*"from" + 0.010*"file" + 0.010*"year" + 0.009*"text" + 0.009*"span" + 0.009*"day"  

Topic 11: 0.009*"use" + 0.008*"engin" + 0.007*"com" + 0.007*"titl" + 0.007*"cite" + 0.006*"compani" + 0.006*"an" + 0.006*"product" + 0.006*"from" + 0.006*"econom"  

Topic 12: 0.013*"web" + 0.013*"titl" + 0.012*"cite" + 0.011*"name" + 0.010*"citi" + 0.009*"publish" + 0.008*"from" + 0.008*"com" + 0.008*"date" + 0.007*"state"  

Topic 13: 0.018*"web" + 0.018*"titl" + 0.017*"game" + 0.017*"cite" + 0.013*"com" + 0.012*"date" + 0.011*"publish" + 0.011*"name" + 0.008*"univers" + 0.008*"leagu"  

Topic 14: 0.018*"his" + 0.011*"name" + 0.009*"p" + 0.009*"from" + 0.009*"had" + 0.007*"year" + 0.007*"book" + 0.007*"king" + 0.007*"first" + 0.007*"titl"  

Topic 15: 0.023*"film" + 0.016*"com" + 0.016*"titl" + 0.014*"cite" + 0.012*"name" + 0.012*"date" + 0.012*"web" + 0.010*"news" + 0.009*"publish" + 0.008*"his"  

Topic 16: 0.018*"journal" + 0.014*"titl" + 0.014*"name" + 0.013*"sub" + 0.013*"cite" + 0.010*"page" + 0.009*"volum" + 0.008*"use" + 0.008*"date" + 0.008*"sup"  

Topic 17: 0.014*"com" + 0.013*"titl" + 0.011*"album" + 0.011*"cite" + 0.010*"music" + 0.010*"record" + 0.009*"web" + 0.009*"name" + 0.009*"date" + 0.008*"first"  

Topic 18: 0.027*"his" + 0.014*"book" + 0.010*"name" + 0.010*"publish" + 0.009*"first" + 0.009*"categori" + 0.009*"titl" + 0.009*"work" + 0.008*"from" + 0.008*"year"  

Topic 19:
0.017*"book" + 0.011*"church" + 0.009*"titl" + 0.009*"name" + 0.009*"from" + 0.008*"publish" + 0.008*"first" + 0.008*"god" + 0.007*"cite" + 0.006*"year"  

Topic 20: 0.106*"align" + 0.071*"right" + 0.046*"style" + 0.032*"text" + 0.024*"center" + 0.013*"footbal" + 0.011*"left" + 0.010*"width" + 0.010*"world" + 0.009*"name"  
```


#### Short texts similiarity:
##### Text 1:

###### Raw text:
>The Federal Reserve Act created a system of private and public entities. There were to be at least eight and no more than twelve private regional Federal Reserve banks. Twelve were established, and each had various branches, a board of directors, and district boundaries. The Federal Reserve Board, consisting of seven members, was created as the governing body of the Fed. Each member is appointed by the President of the U.S and confirmed by the U.S. Senate. In 1935, the Board was renamed and restructured. Also created as part of the Federal Reserve System was a 12-member Federal Advisory Committee and a single new United States currency, the Federal Reserve Note. The Federal Reserve Act created a national currency and a monetary system that could respond effectively to the stresses in the banking system and create a stable financial system. With the goal of creating a national monetary system and financial stability, the Federal Reserve Act also provided many other functions and financial services for the economy, such as check clearing and collection for all members of the Federal Reserve.

###### Topic similiarity:
Most similiar to topic 5: 0.013*"use" + 0.010*"comput" + 0.009*"system" + 0.009*"web" + 0.008*"code" + 0.008*"titl" + 0.008*"com" + 0.008*"name" + 0.007*"cite" + 0.007*"an"

With 44.985092367981577% confidence



## Miscellaneous
+ `convert_for_lda.py`: represents tokens in the necessary format  
+ `quick_sort.py`: align ID(most right collum) in increasing order  
+ `furthur convert_for_lda.py`: represents tokens in the necessary format
+ `sparce_vectors.py`: sparse vector representation
+ `matrix_convert.py, matrix_compare.py`: matrix representation
+ `make_xml.py`: make xml file with text bodies
+ `compress.py`: compresses the file
+ [Understanding the basics of Git and GitHub](http://stackoverflow.com/questions/11816424/understanding-the-basics-of-git-and-github)
+ [Resolving a merge conflict using the command line](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/)
+ [Git documentation](https://git-scm.com/documentation)
4. [Markdown basics for README.md](https://guides.github.com/features/mastering-markdown/)


