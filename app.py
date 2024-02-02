from clean_data import df #นำส่วนการทำ data cleansing ไปไว้ที่ clean_data.py แล้ว import df มาใช้
from dash import Dash, html, callback, Input, Output
import dash_ag_grid as dag

col_name = [{'field': i} for i in df.columns]
col_group = ['Category', 'Beverage', 'Size']
for i in col_name:
    if i.get('field') in col_group:
        i['rowGroup'] = True
        i['hide'] = True
    else:
        i['aggFunc'] = 'avg'
        i['valueFormatter'] = {'function': 'd3.format("(,.2f")(params.value)'}
    
app = Dash(__name__)

app.layout = html.Div([
    dag.AgGrid(
        id='coffee-table',
        columnDefs=col_name,
        rowData=df.to_dict('records'),
        defaultColDef={
            'sortable': True,
            'filter': True
        },
        dashGridOptions={
            'suppressAggFuncInHeader': True #ซ่อน aggFunc ที่ชื่อคอลัมน์เมื่อแสดงผล
        },
        enableEnterpriseModules=True
    ),
    html.Button('Change Data', id='callback-btn', n_clicks=0) #trigger button
])

@callback(
    [Output('coffee-table', 'columnDefs'), Output('coffee-table', 'rowData')],
    Input('callback-btn', 'n_clicks')
)
def callback_data(click):
    if click > 0: #หากต้องการสลับ data ไปมาให้แก้ condition เป็น click % 2 != 0
        #set format data callback
        data_callback = df[['Beverage', 'Sugar', 'Protein', 'Caffeine']]
        data_callback = data_callback[data_callback['Beverage'].str.contains('Tea')].reset_index(drop=True)
        column_def = [{'field': i} for i in data_callback.columns]
        col_num = ['Sugar', 'Protein', 'Caffeine']
        for i in column_def:
            if i.get('field') in col_num:
               i['valueFormatter'] = {'function': 'd3.format("(,.2f")(params.value)'}

        return column_def, data_callback.to_dict('records')
    else:
        return col_name, df.to_dict('records')

if __name__ == '__main__':
    app.run(debug=True)
