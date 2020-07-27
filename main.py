""" =============================BIG MARKER API Connection Script======================="""
""" This Module is designed to retrieve information from the Big Marker Webinar platform """
""" So you can move it to your own CRM, """

import bmconn as bm

BM_API_KEY = ""

bm1 = bm.Bmconn(BM_API_KEY)

print(bm1.api_key)

data = bm1.get_conferences()
listado = bm1.search_conferences()

for conf in listado:
    print("Title: ",conf['title'])
    print("id: ",conf['id'])
    print("copy_webinar_id:", conf['copy_webinar_id'])
    asist = bm1.get_atendees(conf['id'])
    if asist is not None:
        for attendee in asist:
            if attendee['email'] is not None and attendee['first_name'] and attendee['last_name']:
                print(attendee['email'] + ", " + attendee['first_name'] + ", "+ attendee['last_name']+", dur:"+ attendee['engaged_duration'])
           

    #asist2 = bm1.get_atendees(conf['copy_webinar_id'])

#asist = bm1.get_atendees("bb47785703bc")


#print(listado)
