import folium

# Cria um mapa centrado em Ananindeua
mapa = folium.Map(location=[-1.3737, -48.3692], zoom_start=12)

# Adiciona blocos de rua em Ananindeua
blocos = [
    {"nome": "Bloco Brasileirinho", "localizacao": [-1.36501, -48.4015]},
    {"nome": "Bloco Gaiola das Loucas", "localizacao": [-1.34514, -48.39625]},
    {"nome": "Bloco Periquito da vovó", "localizacao": [-1.35348, -48.38825]},
    {"nome": "Concetração dos blocos (Abacatão)", "localizacao": [-1.35015, -48.40845]}
]

# Adiciona marcadores para cada bloco
for bloco in blocos:
    folium.Marker(
        location=bloco["localizacao"],
        popup=f'{bloco["nome"]} - Carnaval 2025',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(mapa)

# Salva o mapa em um arquivo HTML
mapa.save("blocos_ananindeua.html")

print("Mapa gerado com sucesso! Abra o arquivo 'blocos_ananindeua.html' no navegador.")
