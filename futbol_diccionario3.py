jugadores = [{"Nombre":"Vidal","Equipo":"Colo Colo","Representante":"Fernando Felicevich"},
{"Nombre":"Palacios","Equipo":"Colo Colo","Representante": None},
{"Nombre":"Falcon", "Equipo":"Colo Colo","Representante":"Gerardo Arias"},
{"Nombre":"Aranguiz","Equipo":"U de Chile","Representante":"Andre"}
]

for jugador in jugadores:
    print(jugador["Nombre"],jugador["Equipo"], jugador["Representante"],sep="-")