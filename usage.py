import dash_tiptap
import dash
from dash import html, Input, Output
import json
import re

app = dash.Dash(__name__)

mentions = [
    {'id': '1', 'label': 'Govarthanan N'},
    {'id': '2', 'label': 'Neelakandan R'},
    {'id': '3', 'label': 'Jayanthi P'},
    {'id': '4', 'label': 'Kavya V'},
    {'id': '5', 'label': 'Sneha G'},
    {'id': '6', 'label': 'Manju LG'},
    {'id': '7', 'label': 'Ramesh K'},
    {'id': '8', 'label': 'Abilash P'},
    {'id': '9', 'label': 'CJ'},
    {'id': '10', 'label': 'Gova'},
    {'id': '11', 'label': 'Rajiv S'},
]

# Create a dictionary for quick lookup
mention_lookup = {item['label']: item['id'] for item in mentions}

app.layout = html.Div([
    html.H1("Dash Tiptap Mention Component Demo"),
    html.Div([
        html.Div([
            html.H3("Editor"),
            dash_tiptap.DashTiptap(
                id='input',
                value='<p>Type and mention someone using @ symbol</p>',
                mentions=mentions
            ),
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top', 'margin-right': '2%'}),
        
        html.Div([
            html.H3("Mentions Tracker"),
            html.Div(id='mentions-list', style={
                'border': '1px solid #ccc',
                'padding': '15px',
                'border-radius': '5px',
                'background-color': '#f9f9f9',
                'height': '250px',
                'overflow-y': 'auto'
            }),
        ], style={'width': '48%', 'display': 'inline-block', 'vertical-align': 'top'}),
    ], style={'display': 'flex', 'gap': '20px', 'margin-bottom': '30px'}),
    
    html.H3("Mention Statistics"),
    html.Div([
        html.Div([
            html.H4("Total Mentions: "),
            html.Span(id='mention-count', style={'font-size': '24px', 'font-weight': 'bold', 'color': '#1f77b4'})
        ], style={'display': 'inline-block', 'margin-right': '30px'}),
        
        html.Div([
            html.H4("Most Mentioned: "),
            html.Span(id='most-mentioned', style={'font-size': '18px', 'font-weight': 'bold', 'color': '#ff7f0e'})
        ], style={'display': 'inline-block'}),
    ]),
    
    html.Div(id='raw-html', style={'margin-top': '30px', 'padding': '15px', 'background-color': '#f0f0f0', 'border-radius': '5px'})
])

@app.callback(
    [Output('mentions-list', 'children'),
     Output('mention-count', 'children'),
     Output('most-mentioned', 'children'),
     Output('raw-html', 'children')],
    [Input('input', 'value')]
)
def update_mentions_display(html_content):
    if not html_content:
        return [html.P("No mentions yet")], 0, "N/A", f"HTML: {html_content}"
    
    # Extract mentioned names using regex
    # Matches patterns like <a ... data-label="Name" ...>
    pattern = r'data-label="([^"]*)"'
    matches = re.findall(pattern, html_content)
    
    # Create list of mentions with counts
    mention_counts = {}
    for match in matches:
        mention_counts[match] = mention_counts.get(match, 0) + 1
    
    # Build mentions list display
    if mention_counts:
        mentions_items = [
            html.Div([
                html.Span(f"@{name} ", style={'font-weight': 'bold', 'color': '#1f77b4'}),
                html.Span(f"mentioned {count} time(s)", style={'color': '#666'})
            ], style={'padding': '8px', 'border-bottom': '1px solid #e0e0e0'})
            for name, count in sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)
        ]
    else:
        mentions_items = [html.P("No mentions yet", style={'color': '#999'})]
    
    # Calculate total mentions
    total_mentions = sum(mention_counts.values())
    
    # Find most mentioned person
    most_mentioned = max(mention_counts.items(), key=lambda x: x[1])[0] if mention_counts else "N/A"
    
    # Display raw HTML
    raw_html_display = html.Div([
        html.H4("Rendered HTML:"),
        html.Pre(html_content, style={'background-color': '#fff', 'padding': '10px', 'border-radius': '3px', 'overflow-x': 'auto'})
    ])
    
    return mentions_items, total_mentions, most_mentioned, raw_html_display

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8050, debug=True)