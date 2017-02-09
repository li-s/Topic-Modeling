# Topic Modeling by Latent Dirichlet Allocation

In this repository, I experimented with the english Wikipedia, namely doing a matrix comparison between two different texts through the cosine similarity method, and, performing a Latent Dirichlet Allocation(LDA) on 10,000 evenly spaced texts within the 

## Implementation Details
1. xml1.py -> convert xml.bz2 file(wiki) to text file, and extract all text bodies
2. prune.py -> remove common and unique words


###LDA:
3. lda.py -> does the lda

(or additionally,)  
3. convert_for_lda.py -> represents tokens in the necessary format  
4. quick_sort -> align ID(most right collum) in increasing order  
5. furthur convert_for_lda.py -> represents tokens in the necessary format  
6. lda.py -> does the lda


###Matrix comparisons:
-Sparce vectors:  
3. sparce_vectors.py

-Matrix format:  
3. matrix_convert.py  
4. matrix_compare.py


###Make a bz2 file with only text bodies:
3. make_xml.py -> make xml file with text bodies
4. compress.py -> compresses the file


## Results

### Top 20 topics of 10,000 texts in the english Wikipedia:
[(0,  
  '0.040*"languag" + 0.013*"use" + 0.012*"or" + 0.012*"are" + 0.010*"word" + '  
  '0.008*"name" + 0.008*"titl" + 0.008*"by" + 0.007*"from" + 0.006*"an"'),  
 (1,  
  '0.014*"use" + 0.013*"or" + 0.012*"music" + 0.011*"by" + 0.010*"are" + '  
  '0.007*"an" + 0.007*"from" + 0.006*"file" + 0.006*"instrument" + '  
  '0.005*"color"'),  
 (2,  
  '0.018*"com" + 0.017*"titl" + 0.017*"cite" + 0.013*"web" + 0.013*"date" + '  
  '0.013*"news" + 0.012*"music" + 0.012*"name" + 0.011*"publish" + '  
  '0.009*"album"'),  
 (3,  
  '0.011*"or" + 0.009*"by" + 0.009*"are" + 0.009*"book" + 0.007*"titl" + '  
  '0.007*"an" + 0.007*"publish" + 0.007*"this" + 0.006*"cite" + 0.006*"from"'),  
 (4,  
  '0.013*"name" + 0.013*"titl" + 0.012*"cite" + 0.012*"star" + 0.012*"date" + '  
  '0.010*"earth" + 0.010*"day" + 0.009*"from" + 0.009*"by" + 0.009*"first"'),  
 (5,  
  '0.017*"his" + 0.013*"by" + 0.013*"book" + 0.010*"name" + 0.010*"from" + '  
  '0.008*"p" + 0.007*"first" + 0.007*"titl" + 0.007*"year" + 0.006*"publish"'),  
 (6,  
  '0.014*"name" + 0.010*"are" + 0.010*"titl" + 0.010*"cite" + 0.010*"island" + '  
  '0.009*"from" + 0.008*"year" + 0.008*"journal" + 0.008*"by" + 0.006*"river"'),  
 (7,  
  '0.013*"com" + 0.011*"web" + 0.011*"name" + 0.010*"titl" + 0.010*"cite" + '  
  '0.009*"date" + 0.008*"use" + 0.008*"by" + 0.008*"game" + 0.007*"publish"'),  
 (8,  
  '0.017*"his" + 0.012*"titl" + 0.011*"name" + 0.011*"publish" + 0.011*"cite" '  
  '+ 0.011*"book" + 0.010*"by" + 0.009*"univers" + 0.009*"first" + '  
  '0.008*"work"'),  
 (9,  
  '0.026*"film" + 0.012*"com" + 0.012*"titl" + 0.011*"name" + 0.010*"cite" + '  
  '0.010*"his" + 0.009*"by" + 0.008*"date" + 0.008*"web" + 0.007*"award"'),  
 (10,  
  '0.012*"use" + 0.009*"by" + 0.009*"system" + 0.009*"code" + 0.008*"are" + '  
  '0.008*"or" + 0.008*"comput" + 0.007*"web" + 0.006*"titl" + 0.006*"program"'),  
 (11,  
  '0.011*"or" + 0.010*"by" + 0.008*"are" + 0.008*"game" + 0.007*"econom" + '  
  '0.006*"titl" + 0.006*"an" + 0.006*"cite" + 0.006*"from" + 0.006*"com"'),  
 (12,  
  '0.013*"state" + 0.012*"by" + 0.009*"parti" + 0.007*"unit" + 0.007*"elect" + '  
  '0.007*"titl" + 0.007*"govern" + 0.007*"from" + 0.006*"polit" + '  
  '0.006*"name"'),  
 (13,  
  '0.016*"web" + 0.015*"cite" + 0.015*"titl" + 0.012*"name" + 0.011*"publish" '  
  '+ 0.011*"date" + 0.010*"countri" + 0.009*"by" + 0.009*"com" + 0.008*"has"'),  
 (14,  
  '0.017*"war" + 0.013*"forc" + 0.011*"were" + 0.011*"by" + 0.010*"name" + '  
  '0.010*"armi" + 0.010*"militari" + 0.008*"p" + 0.007*"from" + 0.007*"battl"'),  
 (15,  
  '0.043*"math" + 0.017*"x" + 0.016*"sub" + 0.010*"are" + 0.009*"by" + '  
  '0.009*"sup" + 0.008*"number" + 0.008*"mathemat" + 0.008*"an" + 0.008*"f"'),  
 (16,  
  '0.014*"titl" + 0.013*"citi" + 0.012*"web" + 0.012*"cite" + 0.011*"com" + '  
  '0.009*"name" + 0.008*"publish" + 0.007*"by" + 0.007*"date" + 0.007*"first"'),  
 (17,  
  '0.117*"align" + 0.079*"right" + 0.070*"style" + 0.042*"text" + '  
  '0.030*"center" + 0.021*"background" + 0.018*"sort" + 0.017*"data" + '  
  '0.016*"valu" + 0.013*"small"'),  
 (18,  
  '0.049*"b" + 0.045*"d" + 0.018*"player" + 0.017*"politician" + '  
  '0.013*"footbal" + 0.013*"author" + 0.012*"singer" + 0.011*"actor" + '  
  '0.010*"day" + 0.010*"french"'),  
 (19,  
  '0.018*"journal" + 0.013*"titl" + 0.012*"cite" + 0.012*"name" + 0.010*"sub" '  
  '+ 0.010*"page" + 0.010*"are" + 0.009*"volum" + 0.008*"by" + 0.007*"use"')]  

### Top 20 topics of short texts from the 10,000 texts:
[(0,  
  '0.024*"may" + 0.024*"refer" + 0.024*"count" + 0.024*"duke" + 0.024*"born" + '  
  '0.024*"pope" + 0.024*"great" + 0.024*"emperor" + 0.024*"surnam" + '  
  '0.024*"linguist"'),  
 (1,  
  '0.024*"may" + 0.024*"refer" + 0.024*"duke" + 0.024*"count" + 0.024*"roman" '  
  '+ 0.024*"emperor" + 0.024*"born" + 0.024*"great" + 0.024*"pope" + '  
  '0.024*"surnam"'),  
 (2,  
  '0.186*"footbal" + 0.095*"may" + 0.095*"refer" + 0.095*"former" + '  
  '0.095*"name" + 0.095*"stage" + 0.095*"artist" + 0.095*"born" + 0.005*"duke" '  
  '+ 0.005*"count"'),  
 (3,  
  '0.024*"may" + 0.024*"refer" + 0.024*"count" + 0.024*"duke" + 0.024*"roman" '  
  '+ 0.024*"great" + 0.024*"holi" + 0.024*"born" + 0.024*"emperor" + '  
  '0.024*"pope"'),  
 (4,  
  '0.024*"may" + 0.024*"refer" + 0.024*"duke" + 0.024*"count" + 0.024*"roman" '  
  '+ 0.024*"great" + 0.024*"emperor" + 0.024*"surnam" + 0.024*"born" + '  
  '0.024*"holi"'),  
 (5,  
  '0.204*"pope" + 0.104*"refer" + 0.104*"may" + 0.104*"die" + '  
  '0.104*"patriarch" + 0.104*"emperor" + 0.104*"roman" + 0.005*"count" + '  
  '0.005*"duke" + 0.005*"born"'),  
 (6,  
  '0.024*"may" + 0.024*"refer" + 0.024*"duke" + 0.024*"count" + 0.024*"born" + '  
  '0.024*"great" + 0.024*"roman" + 0.024*"emperor" + 0.024*"pope" + '  
  '0.024*"holi"'),  
 (7,  
  '0.024*"may" + 0.024*"refer" + 0.024*"count" + 0.024*"duke" + 0.024*"born" + '  
  '0.024*"emperor" + 0.024*"pope" + 0.024*"great" + 0.024*"roman" + '  
  '0.024*"holi"'),  
 (8,  
  '0.024*"refer" + 0.024*"may" + 0.024*"count" + 0.024*"duke" + 0.024*"roman" '  
  '+ 0.024*"born" + 0.024*"pope" + 0.024*"footbal" + 0.024*"great" + '  
  '0.024*"holi"'),  
 (9,  
  '0.024*"may" + 0.024*"refer" + 0.024*"count" + 0.024*"duke" + 0.024*"pope" + '  
  '0.024*"born" + 0.024*"roman" + 0.024*"great" + 0.024*"emperor" + '  
  '0.024*"holi"'),  
 (10,  
  '0.024*"may" + 0.024*"refer" + 0.024*"duke" + 0.024*"count" + 0.024*"pope" + '  
  '0.024*"roman" + 0.024*"great" + 0.024*"emperor" + 0.024*"holi" + '  
  '0.024*"footbal"'),  
 (11,  
  '0.024*"refer" + 0.024*"may" + 0.024*"count" + 0.024*"duke" + 0.024*"great" '  
  '+ 0.024*"roman" + 0.024*"emperor" + 0.024*"born" + 0.024*"pope" + '  
  '0.024*"artist"'),  
 (12,  
  '0.152*"born" + 0.152*"surnam" + 0.102*"philosoph" + 0.052*"peopl" + '  
  '0.052*"theologian" + 0.052*"includ" + 0.052*"historian" + 0.052*"notabl" + '  
  '0.052*"sociologist" + 0.052*"sometim"'),  
 (13,  
  '0.146*"danish" + 0.146*"astronom" + 0.146*"linguist" + 0.075*"radio" + '  
  '0.075*"southern" + 0.075*"person" + 0.075*"observatori" + 0.075*"refer" + '  
  '0.075*"may" + 0.004*"duke"'),  
 (14,  
  '0.024*"refer" + 0.024*"may" + 0.024*"count" + 0.024*"duke" + 0.024*"great" '  
  '+ 0.024*"roman" + 0.024*"holi" + 0.024*"born" + 0.024*"emperor" + '  
  '0.024*"pope"'),  
 (15,  
  '0.240*"count" + 0.240*"duke" + 0.145*"may" + 0.145*"refer" + 0.050*"from" + '  
  '0.050*"fat" + 0.050*"great" + 0.002*"c" + 0.002*"princ" + 0.002*"call"'),  
 (16,  
  '0.024*"refer" + 0.024*"may" + 0.024*"duke" + 0.024*"count" + 0.024*"born" + '  
  '0.024*"emperor" + 0.024*"great" + 0.024*"roman" + 0.024*"surnam" + '  
  '0.024*"artist"'),  
 (17,  
  '0.024*"refer" + 0.024*"may" + 0.024*"duke" + 0.024*"count" + 0.024*"great" '  
  '+ 0.024*"emperor" + 0.024*"pope" + 0.024*"roman" + 0.024*"born" + '  
  '0.024*"surnam"'),  
 (18,  
  '0.190*"roman" + 0.190*"emperor" + 0.190*"holi" + 0.065*"also" + 0.065*"see" '  
  '+ 0.065*"disambigu" + 0.065*"refer" + 0.065*"may" + 0.003*"count" + '  
  '0.003*"duke"'),  
 (19,  
  '0.024*"refer" + 0.024*"may" + 0.024*"count" + 0.024*"duke" + 0.024*"great" '  
  '+ 0.024*"born" + 0.024*"emperor" + 0.024*"pope" + 0.024*"roman" + '  
  '0.024*"holi"')]  


### Miscellaneous
1. [Understanding the basics of Git and GitHub](http://stackoverflow.com/questions/11816424/understanding-the-basics-of-git-and-github)
2. [Resolving a merge conflict using the command line](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/)
3. [Git documentation](https://git-scm.com/documentation)
4. [Markdown basics for README.md](https://guides.github.com/features/mastering-markdown/)

