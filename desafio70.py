def buscar_permissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]
    except KeyError:
        return "acesso_restrito"
    except IndexError:
        return "acesso_restrito"

perfis = {
    "admin": ["ler","editar","excluir"],
    "usuario": ["ler", "editar"]
}

print(buscar_permissao(perfis, "admin",1))