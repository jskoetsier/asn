# plugs/asn.py
#
#

""" ASN lookup via peeringdb """

__status__ = "seen"

from gozerbot.commands import cmnds
from gozerbot.examples import examples
from gozerbot.plughelp import plughelp
from gozerbot.tests import tests
from pprint import pprint
import peeringdb

pdb = peeringdb.PeeringDB()

# add help

plughelp.add('asn', 'lookup ASN via peeringdb')

def handle_asn(bot, ievent):
    try: what = ievent.args[0]
    except IndexError: ievent.missing("<asn>"); return
    try:
         asnumber_in = int(what)
         net = pdb.all('net', asn=asnumber_in)[0]
         network_nice = pprint(net)
    except Exception, ex: ievent.reply("Invalid ASN: %s" % asnumber_in) ; return
    ievent.reply ('%s is %s') % (asnumber_in, network_nice)
         
           
cmnds.add('asn', handle_asn, 'USER')
examples.add('asn', 'Lookup as number on peeringdb', 'asn 8315')
tests.add('asn 8315')


