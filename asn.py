import json
import requests
from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp
from gozerbot.tests import tests

# add help

plughelp.add('asn', 'lookup ASN via peeringdb')

def doreq(asnumber_in):
    url = "http://peeringdb.com/api/net?asn=" + asnumber_in
    resp = requests.get(url=url)
    pdb_json = json.loads(resp.text)
    network_name = pdb_json['data'][0]['name']
    return

def handle_asn(bot, ievent):
    asnumber_in = ""
    try: what = ievent.args[0]
    except IndexError: ievent.missing("<asn>"); return
    try:
         asnumber_in = what
         url = "http://peeringdb.com/api/net?asn=" + asnumber_in
         resp = requests.get(url=url)
         pdb_json = json.loads(resp.text)
         network_name = pdb_json['data'][0]['name']
         resultstring = "AS Number: %s has name: %s" % (asnumber_in, network_name)
         ievent.reply(resultstring)
    except Exception, ex: ievent.reply("Invalid ASN or unknown in peeringdb") ; return


cmnds.add('asn', handle_asn, 'USER')
examples.add('asn', 'Lookup as number on peeringdb', 'asn 8315')
tests.add('asn 8315')

### In elkaar gerost door phreak ergens in 2020.
