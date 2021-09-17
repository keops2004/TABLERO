import dash_bootstrap_components as dbc
def Navbar():
    navbar = dbc.NavbarSimple(
             children = [
                   dbc.NavItem(dbc.NavLink('INICIO', href='/index')),
                   dbc.DropdownMenu(
                       children = [
                             dbc.DropdownMenuItem('Pagina 1', href = '#'),
                             dbc.DropdownMenuItem('Pagina 2', href = '#'),
                             dbc.DropdownMenuItem('Pagina 3', href = '#'),
                       ],
                       nav = True,
                       in_navbar = True,
                       label = 'Indice',
                    ),
              ],
              brand = 'SISTEMA DETECCION PLACAS VEHICULARES',
              color = 'primary',
              dark = True,
    )
    return navbar

