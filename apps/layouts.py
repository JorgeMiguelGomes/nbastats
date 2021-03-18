import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_bootstrap_components as dbc

graph = html.Div([
    dcc.Graph(id='graph')
    ])

def table(columns):
    PAGE_SIZE = 10
    table = html.Div([
        dash_table.DataTable(
            id='datatable-paging',
            columns=[
                {'id': c, 'name': c, "deletable": True, "selectable": True} for c in columns
            ],
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current=0,
            page_size=PAGE_SIZE,
        )
        ])
    return table

def content():
    CONTENT_STYLE = {
    'margin-left': '15%',
    }

    content = html.Div([
    dcc.Tabs(id="tabs", value='graph', children=[
        dcc.Tab(label='Graph', value='graph'),
        dcc.Tab(label='Table', value='table'),
    ]),
    html.Div(id='tabs-content')
    ],
    style=CONTENT_STYLE
    )
    return content

def sidebar(columns):
    SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '15%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
    }

    TEXT_STYLE = {
        'textAlign': 'center',
        'color': '#191970'
    }
    sidebar = html.Div(
    [
        html.H2('Parameters', style=TEXT_STYLE),
        html.Hr(),
        html.P("Select Team"),
        html.Div([dcc.Dropdown(
                id='select-team'
            )],
        style={'width': '90%', 'display': 'inline-block'}),

        html.P("X-axis Line"),
        html.Div([
                dcc.Dropdown(
                    id='yaxis-column',
                    options=[{'label': i, 'value': i} for i in columns],
                    value='PPG'
                )],
                style={'width': '90%', 'display': 'inline-block'}),
        html.P("Pie Value"),
        html.Div([dcc.Dropdown(
                id='value-pie'
            )],
        style={'width': '90%', 'display': 'inline-block'}),
    ],
    style=SIDEBAR_STYLE,
    )

    return sidebar


navbar = dbc.NavbarSimple(
       children=
    [
        dbc.NavItem(dbc.NavLink('Home', href='/')),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Regular", href="#"),
                dbc.DropdownMenuItem('Playoffs', href='/playoffs'),
            ],
            nav=True,
            in_navbar=True,
            label="Season",
        ),
    ],
    color="grey",
    style={'background-color': '#f8f9fa'}
)
