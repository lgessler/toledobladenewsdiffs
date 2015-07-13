from baseparser import BaseParser
from bs4 import BeautifulSoup
import re
import datetime

DATE_FORMAT = '%A, %B %e %Y, %l:%M %p'

def hacky_grep(html, pattern):
    """Used to find a single line in the html.
        
    This should work for the blade, but it could
    break at any moment."""
    for line in html.split('\n'):
        if re.search(pattern, line):
            return line
    return None

class BladeParser(BaseParser):
    SUFFIX = ''
    domains = ['www.toledoblade.com']

    feeder_pat   = '^http://www.toledoblade.com/.*.html'
    feeder_pages = ['http://www.toledoblade.com/']

    def _printableurl(self):
        return re.sub('', '', self.url)

    def _parse(self, html):
        soup = BeautifulSoup(html)

        self.meta = soup.findAll('meta')
        elt = soup.find('h1')
        if elt is None:
            self.real_article = False
            return
        self.title = elt.getText().strip()
        elt = soup.find('div', {'class' : 'storybyline'})
        if elt is None:
            self.byline = ''
        else:
            self.byline = elt.getText().strip()

        # The Blade has a line of javascript in its articles with the date of publish
        js_string = hacky_grep(html, ' *var pub_date =.*Z')
        if js_string is None:
            self.date = ''
        else:
            # Get RHS
            date = js_string[js_string.find('=') + 2:]

            # Remove white space, if any
            date = date.strip()

            # Not sure what the Z on the end means, but I think we can ignore it
            date = date.replace('"','').replace(';','').replace('Z','')

            # We should be left with something like 
            #   '2015-07-11 15:44:32'
            date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

            self.date = date.strftime(DATE_FORMAT)

        div = soup.find('div', {'class':'story-printcontainer'})
        if div is None:
            self.real_article = False
            return
        self.body = '\n'+'\n\n'.join([x.getText().strip() for x in div.findAll('p')])
