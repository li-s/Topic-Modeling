import xml.etree.cElementTree as etree
import bz2, re
from gensim import utils
from pprint import pprint





def get_namespace(tag):
    """Returns the namespace of tag."""
    m = re.match("^{(.*?)}", tag)
    namespace = m.group(1) if m else ""
    if not namespace.startswith("http://www.mediawiki.org/xml/export-"):
        raise ValueError("%s not recognized as MediaWiki dump namespace"
                         % namespace)
    return namespace
_get_namespace = get_namespace




def extract_pages(f, filter_namespaces=False):
	"""
	Extract pages from a MediaWiki database dump = open file-like object `f`.
	Return an iterable over (str, str, str) which generates (title, content, pageid) triplets.
	"""
	elems = (elem for _, elem in etree.iterparse(f, events=("end",)))

	# We can't rely on the namespace for database dumps, since it's changed
	# it every time a small modification to the format is made. So, determine
	# those from the first element we find, which will be part of the metadata,
	# and construct element paths.
	elem = next(elems)
	namespace = get_namespace(elem.tag)
	ns_mapping = {"ns": namespace}
	page_tag = "{%(ns)s}page" % ns_mapping
	text_path = "./{%(ns)s}revision/{%(ns)s}text" % ns_mapping
	title_path = "./{%(ns)s}title" % ns_mapping
	ns_path = "./{%(ns)s}ns" % ns_mapping
	pageid_path = "./{%(ns)s}id" % ns_mapping

	for elem in elems:
		if elem.tag == page_tag:
			title = elem.find(title_path).text
			text = elem.find(text_path).text

			if filter_namespaces:
				ns = elem.find(ns_path).text
				if ns not in filter_namespaces:
					text = None

			pageid = elem.find(pageid_path).text
			yield title, text or "", pageid     # empty page will yield None


			elem.clear()



#From GitHub
def standard(length, fname, filter_namespaces=('0',), lemmatize=utils.has_pattern()):
	texts = ((text, lemmatize, title, pageid) for title, text, pageid in extract_pages(bz2.BZ2File(fname), filter_namespaces))
	i = 0
	res = []
	for text in texts:
		if i < length:
			if len(text[0]) > 200:
				#pprint(text)
				res.append(text)
				i += 1
		elif i >= length:
			return res

if __name__ == '__main__':
	standard(10, '/home/li/Downloads/enwiki-latest-pages-articles.xml.bz2')
