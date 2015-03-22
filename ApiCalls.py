try:
    import cjson
    parse_json = cjson.decode
except ImportError:
    import json
    parse_json = json.loads

from bandsintown import RequestException
try:
    import bandsintown
    bandsintown.app_id = "pyconcert"
except ImportError:
    pass

import urllib

with open("config.json") as config_file:
    config = parse_json(config_file.read())
SK_API_KEY = config["SK_API_KEY"]

class Event(object):
    def __init__(self, artists, venue, city,
                 country, date, time, ticket_url):
        self.artists = artists
        self.venue = venue
        self.city = city
        self.country = country
        self.date = date
        self.time = time
        self.ticket_url = ticket_url

    def __str__(self):
        return "Event by {artists} in {venue} ({city}, {country}).".format(artists=", ".join(self.artists),
                                                                          venue=self.venue,
                                                                          city=self.city,
                                                                          country=self.country)

    def __repr__(self):
        return self.__str__()

def _chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def _get_songkick_location(location):
    location, country = location.split(",")
    location = location.strip()
    country = country.strip()
    api_call = "http://api.songkick.com/api/3.0/search/locations.json?query={}&apikey={}".format(location, SK_API_KEY)
    resp = parse_json(urllib.urlopen(api_call).read())
    for location in resp['resultsPage']['results']['location']:
        if location['metroArea']["country"]["displayName"] == country:
            sk_id = location['metroArea']['id']
            break
    return "sk:{}".format(sk_id)

def _get_songkick_events(artist, location):
    api_call = "http://api.songkick.com/api/3.0/events.json?apikey={}&artist_name={}&location={}".format(SK_API_KEY, artist, location)
    resp = parse_json(urllib.urlopen(api_call).read())
    if resp["resultsPage"]["status"] != "ok":
        print resp
        return []

    ret = []
    for event in resp['resultsPage']['results'].get("event", []):
        artists = [artist['displayName'] for artist in event['performance']]
        venue = event['venue']['displayName']
        city = event['venue']['metroArea']['displayName']
        country = event['venue']['metroArea']['country']['displayName']
        date = event['start']['date']
        time = event['start']['time']
        result_event = Event(artists,
                             venue,
                             city,
                             country,
                             date,
                             time,
                             event['uri'])
        ret.append(result_event)
    return ret

def events_for_artists_bandsintown(artists, location):
    all_events = []
    for artists_chunk in _chunks(list(artists), 50):
        try:
            events = bandsintown.Event.search(location=location, artists=artists_chunk)
            all_events.extend(events)
        except RequestException as e:
            print "Request failed: ", e
    return all_events

def events_for_artists_songkick(artists, location):
    all_events = []
    sk_loc = _get_songkick_location(location)
    for artist in artists:
        try:
            events = _get_songkick_events(artist, sk_loc)
            all_events.extend(events)
        except RequestException as e:
            print "Request failed: ", e
    return all_events
