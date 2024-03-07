import requests
import json
from string import Template



def request_get(url):
    return json.loads(requests.get(url).text)

response = request_get("https://pokeapi.co/api/v2/pokemon")["results"][:20]

print(response)


html_template = Template('''<!DOCTYPE html>
                            <html>
                            <head>
                            <title>Título de la Página</title>
                            </head>
                            <body>

                            <h1>pokedex</h1>

                            $body

                            </body>
                            </html>
                         
                         
                         
                         ''')


content_template = Template("<h4>$name</h4> <img src='$url'>")

content = ''
for  pokemon in response:
    pokemon_data = request_get(pokemon["url"])
    sprites_url = pokemon_data["sprites"]["front_default"]
    pokemon_name = pokemon["name"]
    content += content_template.substitute(name=pokemon_name, url=sprites_url)

html = html_template.substitute(body=content)  
    



with open('output.html', 'w') as f:
    f.write(html)

print("HTML generado y guardado en output.html")

    





