#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
import time
import math
import argparse
import requests
import random
import re
import os

PLIMIT = 500 # max: 500

APIURL = f'https://en.wikipedia.org/w/api.php?'
PARAMS1 = f'action=query&list=categorymembers&cmtitle='
PARAMS2 = f'&maxlag=5&format=json&cmlimit={PLIMIT}'
DATAURL = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql?query='

parser = argparse.ArgumentParser(description='Search Wikipedia Categories')
parser.add_argument('-c', '--category', dest='category', help='check category',
    default='Films based on novels')   #to retrieve films based on Italian novels in general just put "Films based on Italian novels" as category default
parser.add_argument('-j', '--json', dest='json', help='load from JSON',
    action='store_true', default=False)
args = parser.parse_args()

def red(string):
    return '\x1b[91m{}\x1b[0m'.format(string) if os.isatty(sys.stdout.fileno()) else string

def yellow(string):
    return '\x1b[93m{}\x1b[0m'.format(string) if os.isatty(sys.stdout.fileno()) else string

def orange(string):
    return '\x1b[38;5;208;48;238m{}\x1b[0m'.format(string) if os.isatty(sys.stdout.fileno()) else string

def pink(string):
    return '\x1b[95m{}\x1b[0m'.format(string) if os.isatty(sys.stdout.fileno()) else string

def gray(string):
    return '\x1b[37m{}\x1b[0m'.format(string) if os.isatty(sys.stdout.fileno()) else string
        
def green(string):
    return '\x1b[92m{}\x1b[0m'.format(string) if os.isatty(sys.stdout.fileno()) else string

def blue(string):
    return '\x1b[96m{}\x1b[0m'.format(string) if os.isatty(sys.stdout.fileno()) else string

def trunc(string, length=40, suffix='...'):
    if not string or len(string) <= length:
        return string
    while len(string) > length:
        string = ' '.join(re.split('/|\s', string[:length-len(suffix)])[0:-1]).rstrip(',')
    return f'{string}{suffix}'

def sleep(seconds=5):
    time.sleep(seconds)

def sleepPrint(minTime=20, maxTime=40, extra=''):
    seconds = random.randrange(minTime, maxTime)
    if extra and int(extra) > 1:
        sys.stdout.write('{}          \r'.format(extra))
    else:
        sys.stdout.write('            \r')
    sys.stdout.flush()
    time.sleep(seconds)

def wdRequest(cat, extra='', results=None, checked={}):
    print(f'   {yellow(cat.replace("_", " "))}{" (continue)" if extra else ""}')
    try:
        cat = cat.replace(" ", "_")
        reqUrl = f'{APIURL}{PARAMS1}Category:{cat}{PARAMS2}{extra}'
        #print(reqUrl)
        headers = {'User-Agent': 'MushroomTest/0.1 +http://wikidata.org/wiki/User:Mushroom'}
        response = requests.get(reqUrl, headers=headers)
        jresp = {'error': {'info': 'Generic error'}}
        jresp = json.loads(response.text)
        #print(jresp)
        if not results:
            results = jresp['query']['categorymembers']
        else:
            results += jresp['query']['categorymembers']
        if 'continue' in jresp:
            #sleep(.02)
            wdRequest(
                cat,
                extra=f'&cmcontinue={jresp["continue"]["cmcontinue"]}',
                results=results,
                checked=checked
            )
        else:
            pages = [x['title'] for x in results if x['ns'] == 0]
            checked[cat.replace("_", " ")] = {'tot': len(pages), 'pages': pages}
            for result in results:
                if result['title'] not in checked.keys():
                    if result['ns'] == 14:
                        #sleep(.02)
                        with open(f'{args.category.replace(" ", "_")}.json', 'w') as outfile:
                            json.dump(checked, outfile, ensure_ascii=False)
                        wdRequest(
                            result['title'].split('Category:')[1],
                            extra='',
                            results=None,
                            checked=checked
                        )
    except Exception as e:
        print(red(f'\n   ERROR: {cat.replace("_", " ")}\n   {e}'))
        sleepPrint(minTime=5, maxTime=10)
    return checked

def dataRequest(query):
    try:
        reqUrl = f'{DATAURL}{requests.utils.quote(query)}&format=json'
        #print(reqUrl)
        headers = {'User-Agent': 'MushroomTest/0.1 +http://wikidata.org/wiki/User:Mushroom'}
        response = requests.get(reqUrl, headers=headers)
    except Exception as e:
        print('        • {}\n'.format(e))
    else:
        try:
            #print(response.text)
            jresp = json.loads(response.text)
            return jresp
        except Exception as e:
            print(red('\n   {}\n'.format(e)))

try:
    if args.category:
        print()
        if not args.json:
            checked = wdRequest(args.category)
        else:
            try:
                with open(f'{args.category.replace(" ", "_")}.json') as infile:
                    print(yellow(f'   {args.category}'))
                    checked = json.load(infile)
            except FileNotFoundError:
                print(red('   JSON file not found\n'))
                sys.exit()

        pageSet = set([])
        notFilms = {}

        for c in checked.keys():
            for page in checked[c]['pages']:
                if '(' in page and 'film' not in page:
                    disambig = page.split('(')[1]
                    disambig = re.sub(r"\d+", "", disambig) 
                    disambig = disambig.replace('  ', ' ')
                    disambig = disambig.strip(')').strip()
                
                    if disambig in notFilms:
                        notFilms[disambig] += 1
                    else:
                        notFilms[disambig] = 1
                else:
                    pageSet.add(page)

        print()
        totCat = len(checked.keys())
        totWork = len(pageSet)
        print(f'   {totWork} work{"s" if totWork > 1 else ""} in {totCat} categor{"ies" if totCat > 1 else "y"}')

        urls = []
        
        for t in sorted(list(pageSet)):
            title = t.replace(' ', '_')
            url = f'https://en.wikipedia.org/wiki/{title}'
            urls.append(f'<{url}>')

        print()
        
        notFilms = dict(sorted(notFilms.items(), key=lambda item: item[1], reverse=True))
        notFilmList = ', '.join([f'{notFilms[notFilm]} {notFilm}' for notFilm in notFilms.keys()])
        
        print(f'   Excluding: {notFilmList}\n')
        
        qmin = 0
        qmax = 30
        
        totLink = 0
        reqCount = 1
        reqMax = math.ceil(len(urls)/qmax)

        while True:
            urlChunk = [x.replace('"', "%22") for x in urls[qmin:qmax]]
        
            query = f'PREFIX schema: <http://schema.org/> \
                PREFIX wikibase: <http://wikiba.se/ontology#> \
                PREFIX wd: <http://www.wikidata.org/entity/> \
                PREFIX wdt: <http://www.wikidata.org/prop/direct/> \
                \
                SELECT (COUNT(?qid) AS ?count) WHERE {{ \
                    ?url schema:about ?qid . \
                    ?qid wdt:P144 ?other . \
                    VALUES ?url {{\
                        {" ".join(urlChunk)} \
                    }} \
                }}'
            
            try:
                sys.stdout.write(f'   Querying Wikidata... {reqCount}/{reqMax}     \r')
                totLink += int(dataRequest(query)['results']['bindings'][0]['count']['value'])
                reqCount += 1
            except TypeError:
                raise
                print(red(query))
            #sleep(.02)
            
            if qmax > len(urls):
                break
            else:
                qmin +=30
                qmax +=30
        
        totPercent = (totLink/totWork)*100
        print(f'   {totLink} works ({totPercent:.2f}%) have link in Wikidata')

    print()
except KeyboardInterrupt:
    print('\n')
    sys.exit()