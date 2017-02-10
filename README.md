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
Topic 1:  0.040*"languag" + 0.013*"use" + 0.012*"or" + 0.012*"are" + 0.010*"word" + 0.008*"name" + 0.008*"titl" + 0.008*"by" + 0.007*"from" + 0.006*"an"  
Topic 2:  0.014*"use" + 0.013*"or" + 0.012*"music" + 0.011*"by" + 0.010*"are" + 0.007*"an" + 0.007*"from" + 0.006*"file" + 0.006*"instrument" + 0.005*"color"  
Topic 3:  0.018*"com" + 0.017*"titl" + 0.017*"cite" + 0.013*"web" + 0.013*"date" + 0.013*"news" + 0.012*"music" + 0.012*"name" + 0.011*"publish" + ''0.009*"album"  
Topic 4:  0.011*"or" + 0.009*"by" + 0.009*"are" + 0.009*"book" + 0.007*"titl" + 0.007*"an" + 0.007*"publish" + 0.007*"this" + 0.006*"cite" + 0.006*"from"  
Topic 5:  0.013*"name" + 0.013*"titl" + 0.012*"cite" + 0.012*"star" + 0.012*"date" + 0.010*"earth" + 0.010*"day" + 0.009*"from" + 0.009*"by" + 0.009*"first"  
Topic 6:  0.017*"his" + 0.013*"by" + 0.013*"book" + 0.010*"name" + 0.010*"from" + 0.008*"p" + 0.007*"first" + 0.007*"titl" + 0.007*"year" + 0.006*"publish"  
Topic 7:  0.014*"name" + 0.010*"are" + 0.010*"titl" + 0.010*"cite" + 0.010*"island" + 0.009*"from" + 0.008*"year" + 0.008*"journal" + 0.008*"by" + 0.006*"river"  
Topic 8:  0.013*"com" + 0.011*"web" + 0.011*"name" + 0.010*"titl" + 0.010*"cite" + 0.009*"date" + 0.008*"use" + 0.008*"by" + 0.008*"game" + 0.007*"publish"  
Topic 9:  0.017*"his" + 0.012*"titl" + 0.011*"name" + 0.011*"publish" + 0.011*"cite" + 0.011*"book" + 0.010*"by" + 0.009*"univers" + 0.009*"first" + 0.008*"work"  
Topic 10:  0.026*"film" + 0.012*"com" + 0.012*"titl" + 0.011*"name" + 0.010*"cite" + 0.010*"his" + 0.009*"by" + 0.008*"date" + 0.008*"web" + 0.007*"award"  
Topic 11:  0.012*"use" + 0.009*"by" + 0.009*"system" + 0.009*"code" + 0.008*"are" + 0.008*"or" + 0.008*"comput" + 0.007*"web" + 0.006*"titl" + 0.006*"program"  
Topic 12:  0.011*"or" + 0.010*"by" + 0.008*"are" + 0.008*"game" + 0.007*"econom" + 0.006*"titl" + 0.006*"an" + 0.006*"cite" + 0.006*"from" + 0.006*"com"  
Topic 13:  0.013*"state" + 0.012*"by" + 0.009*"parti" + 0.007*"unit" + 0.007*"elect" + 0.007*"titl" + 0.007*"govern" + 0.007*"from" + 0.006*"polit" + '0.006*"name"  
Topic 14:  0.016*"web" + 0.015*"cite" + 0.015*"titl" + 0.012*"name" + 0.011*"publish" + 0.011*"date" + 0.010*"countri" + 0.009*"by" + 0.009*"com" + 0.008*"has"  
Topic 15:  0.017*"war" + 0.013*"forc" + 0.011*"were" + 0.011*"by" + 0.010*"name" + 0.010*"armi" + 0.010*"militari" + 0.008*"p" + 0.007*"from" + 0.007*"battl"  
Topic 16:  0.043*"math" + 0.017*"x" + 0.016*"sub" + 0.010*"are" + 0.009*"by" + 0.009*"sup" + 0.008*"number" + 0.008*"mathemat" + 0.008*"an" + 0.008*"f"  
Topic 17:  0.014*"titl" + 0.013*"citi" + 0.012*"web" + 0.012*"cite" + 0.011*"com" + 0.009*"name" + 0.008*"publish" + 0.007*"by" + 0.007*"date" + 0.007*"first"  
Topic 18:  0.117*"align" + 0.079*"right" + 0.070*"style" + 0.042*"text" + 0.030*"center" + 0.021*"background" + 0.018*"sort" + 0.017*"data" + 0.016*"valu" + 0.013*"small"  
Topic 19:  0.049*"b" + 0.045*"d" + 0.018*"player" + 0.017*"politician" + 0.013*"footbal" + 0.013*"author" + 0.012*"singer" + 0.011*"actor" + 0.010*"day" + 0.010*"french"  
Topic 20:  0.018*"journal" + 0.013*"titl" + 0.012*"cite" + 0.012*"name" + 0.010*"sub" + 0.010*"page" + 0.010*"are" + 0.009*"volum" + 0.008*"by" + 0.007*"use"  
```


#### Short texts similiarity:
##### Text 1:

###### Raw text:
The Federal Reserve Act created a system of private and public entities. There were to be at least eight and no more than twelve private regional Federal Reserve banks. Twelve were established, and each had various branches, a board of directors, and district boundaries. The Federal Reserve Board, consisting of seven members, was created as the governing body of the Fed. Each member is appointed by the President of the U.S and confirmed by the U.S. Senate. In 1935, the Board was renamed and restructured. Also created as part of the Federal Reserve System was a 12-member Federal Advisory Committee and a single new United States currency, the Federal Reserve Note. The Federal Reserve Act created a national currency and a monetary system that could respond effectively to the stresses in the banking system and create a stable financial system. With the goal of creating a national monetary system and financial stability, the Federal Reserve Act also provided many other functions and financial services for the economy, such as check clearing and collection for all members of the Federal Reserve.

###### Topic similiarity:


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


