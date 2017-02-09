# Topic Modeling by Latent Dirichlet Allocation

[what is topic model? views documents as a mixture of various topics]
Topic models are not only used for exploring hidden semantic structures in new textual data, but for also complementing supervised machine learning in constructing and checking the accuracy of existing classification models.

In this repository, I chose to utilise Latent Dirichlet Allocation(LDA) for topic modeling. I trained LDA on a subset of the English wikipedia corpus, and found the top 20 topics of the texts found below. Furthurmore, I used the trained LDA to predict topic distributions on 3 seletected texts within the corpus(short_texts.txt), of which the result can be found below.

Through this process, I have written some other codes, such as comparing two matrixes using cosine similarity, or making and then compressing a .xml file.

## Implementation Details

1. xml1.py -> convert xml.bz2 file(wiki) to text file, and extract all text bodies [how does the texts selected? total no. and interval ...]
2. prune.py -> remove common and unique words
3. [how is dictionary built]
4. [how to convert a text to a bow vetor? how does the vector represent? sparse .. full ...]
5. lda.py -> does the lda

#### Move to Miscs:

3. convert_for_lda.py -> represents tokens in the necessary format  
4. quick_sort -> align ID(most right collum) in increasing order  
5. furthur convert_for_lda.py -> represents tokens in the necessary format  
6. lda.py -> does the lda
#####Sparce vectors:  
3. sparce_vectors.py
#####Matrix format:  
3. matrix_convert.py  
4. matrix_compare.py



#### Make a bz2 file with only text bodies:

3. make_xml.py -> make xml file with text bodies
4. compress.py -> compresses the file


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


#### Top 20 topics of short texts from the 10,000 texts:
[[(4, 0.11388034488609908), (5, 0.055074928797886273), (7, 0.72690207904542692), (11, 0.07073416980982021), (17, 0.013578074223494177)], 


[(4, 0.063833696251872213), (7, 0.80456719995350756), (11, 0.095537977349093375), (17, 0.029859575911871231)], 

[(5, 0.034055716872079027), (7, 0.088255718340154304), (11, 0.87124917069715058)]]



[' alfonso may refer to alfonso of asturias 791 842 alfonso of aragon 1162 '
 '1196 alfonso count of provence 1174 1209 afonso of portugal 1185 1223 the '
 'fat alfonso count of poitou 1220 1271 jure uxoris alfonso count of toulouse '
 'alfonso of naples 1448 1495 alfonso este 1533 1597 duke of ferrara from 1559 '
 'to 1597 hndis de liste der herrscher namens alfons alfons ',
 
 ' alfonso may refer to alfonso of leon 866 910 surnamed the great afonso of '
 'portugal 1210 1279 alfonso of aragon 1285 1291 alfonso este duke of modena '
 'and reggio 1628 1644 alfonso of kongo 1666 1667 hndis ',
 
 ' anastasius or anastasios may refer to anastasius dicorus 430 518 roman '
 'emperor anastasius of antioch 599 patriarch of antioch pope anastasius died '
 '401 pope of rome hndis ']

## Miscellaneous
1. [Understanding the basics of Git and GitHub](http://stackoverflow.com/questions/11816424/understanding-the-basics-of-git-and-github)
2. [Resolving a merge conflict using the command line](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/)
3. [Git documentation](https://git-scm.com/documentation)
4. [Markdown basics for README.md](https://guides.github.com/features/mastering-markdown/)


