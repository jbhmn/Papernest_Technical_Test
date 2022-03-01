from math import sqrt
import requests


DIST_MAX=1000 #city-level precision
providers={20801:'Orange',20810:'SFR',20815:'Free',20820:'Bouygues'}


'''
Converting an address to X, Y geographic coordinates, return exact address found and geographic coordinates
'''
def to_coordinates(address):
    url = f'https://api-adresse.data.gouv.fr/search/?q={address}'
    urlfile = requests.get(url)
    data= urlfile.json()
    found_address = data['features'][0]['properties']['label']    
    x = data['features'][0]['properties']['x']
    y = data['features'][0]['properties']['y']
    return(found_address,x,y)



'''
Getting network coverage for given x and y coordinates
'''

def network_coverage_by_x_y(x,y):

    dist={}
    net_coverage={}
    for i in providers.keys():
        dist[i]=DIST_MAX

    with open('2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv','r') as read_obj:
        read_obj.readline()
        while True:
            #reading the file line by line
            line = read_obj.readline()
            if not line:
                break
            row=line.strip().split(";")

            if int(row[0]) in providers.keys():
                try:
                    d=sqrt(((int(row[1])-x)**2)+((int(row[2])-y)**2))
                    if d<dist[int(row[0])]:
                        dist[int(row[0])]=d
                        net_coverage[providers[int(row[0])]]={"2G":bool(int(row[3])),"3G":bool(int(row[4])),"4G":bool(int(row[5]))}

                except ValueError:        
                    #If the row is not in the correct format, we'll just ignore it
                    pass

    return(net_coverage)


'''
Getting network coverage for a given address
'''
def network_coverage_by_address(address):
    if address==None:
        return("No address provided")
    try:
        found_address,x,y=to_coordinates(address)
    except (IndexError, KeyError):
        return("invalid adress")
    except requests.exceptions.ConnectionError:
        return("impossible to connect")
    return(found_address,network_coverage_by_x_y(x,y))

