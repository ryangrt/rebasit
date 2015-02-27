mongoo
=======

goo to bind mongodb to CPU power



Processing upgrade

mongoo: FOSS?

source-connection/collection, query, args

start w con/col list (*args) -- source is first
use **kw for query

mongoo(
    user:passwd@hostipaddr:port/rawdata/raw_scrapes, 
	user:passwd@host:port/dev_stage/parsed, 
	scrapus2, 
	invalid=False, 
	timestamp__gte=before, 
	extra=123)

calls raw_scrape.process(scrapus2, extra)

def process(self, dest, ex):
    self #instance of raw_scrapes
    dest #parsed con/col
    ex #whatever, dict of flags etc

shell:

mongoo.py -c 'mongo(user:passwd@hostipaddr:port/raw_scrapes user:passwd@host:port/parsed, user:passwd@host:port/scrapus2,invalid=False timestamp__gte=before, extra=123)'
