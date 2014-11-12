ScraPoi
=======
ScraPoi is a simple web crawler based in [ScraPy](http://scrapy.org/) for extract points of interest information from any country in the world. The results are presented in a website with a map and a list of poi with their descriptions.

The points of interest data is extracted from MiNube UK site [http://www.minube.co.uk/](http://www.minube.co.uk/) a travel website with pois and descriptions for each country in the world.

Installation
------------
For installing this project you only need to clone it and set up a Python 2.7 virtual enviroment with necessary libraries described in requirements.txt, for this you need to execute:

`pip install -r requirements.txt`

Usage
-----
After install the requirements you can execute `scrapy` command. The country to be crawled can be passed as parameter like this: 

`scrapy crawl minube -a country="ireland"`

The result of this execution is a simple html file called `index.html` with a presentation of crawled data: title, map and list of pois.  

Notes
-----
For `country` parameter is important to use the same country name as minube website, otherwise a 404 error may be raised in crawling process. Generally this names matches with english names of the countries: spain, ireland, uruguay, germany, cuba, italy, turkey, greece, bulgaria...
