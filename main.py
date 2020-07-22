""" =============================BIG MARKER API Connection Script======================="""
""" This Module is designed to retrieve information from the Big Marker Webinar platform """
""" So you can move it to your own CRM, """
import bmconn as bm

BM_API_KEY = "c15e450a5757c2e65ff8"

bm1 = bm.Bmconn(BM_API_KEY)

print(bm1.api_key)

data = bm1.get_conferences()

for conf in data:
    print(conf['title'])
    print(conf['id'])
    asist = bm1.get_atendees(conf['id'])

asist = bm1.get_atendees("a7eef6bef481")