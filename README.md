# doc_similarity

compare document sililarity

### TODOs
1. Construct a dataset consisting of 10000 documents [DONE]
2. Run LDA over the dataset, to get 10~20 topics (see [gensim](https://radimrehurek.com/gensim/wiki.html#latent-dirichlet-allocation))
3. Visualize top words in each topic

### Readings
1. [Understanding the basics of Git and GitHub](http://stackoverflow.com/questions/11816424/understanding-the-basics-of-git-and-github)
2. [Resolving a merge conflict using the command line](https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line/)
3. [Git documentation](https://git-scm.com/documentation)
4. [Markdown basics for README.md](https://guides.github.com/features/mastering-markdown/)

### Directions
1. xml1.py -> convert xml.bz2 file(wiki) to text file, and extract all text bodies
2. prune.py -> remove common and unique words


####LDA:
3. convert_for_lda.py -> represents tokens in the necessary format
4. quick_sort -> align ID(most right collum) in increasing order
5. furthur convert_for_lda.py -> represents tokens in the necessary format
6. lda.py -> does the lda


####Matrix comparisons:
-Sparce vectors:
3. sparce_vectors.py

-Matrix format:
3. matrix_convert.py
4. matrix_compare.py


####Make a bz2 file with only text bodies:
3. make_xml.py -> make xml file with text bodies
4. compress.py -> compresses the file
