import yaml
from unicodedata import normalize #sudo pip install unidecode

def manipulateCommunity(community):
    return normalize('NFKD', community.lower().strip()).encode('ASCII','ignore').decode('ASCII')

community_list = yaml.load(open('community.yaml'), Loader=yaml.FullLoader)


community = 'bruno'
community = manipulateCommunity(community)

if community in community_list['community']:
    print ('Community found!')
else:
    aux_community_list = []
    aux_community = community[0:(int(len(community)/2))]

    while len(aux_community_list) == 0:
        for c in community_list['community']:
            if c.find(aux_community) > -1 and c not in aux_community_list:
                aux_community_list.append(c)
        
        aux_community = aux_community[0:(int(len(aux_community)/2))]

    print ('Community not found!\ntry: %s'  %aux_community_list)



