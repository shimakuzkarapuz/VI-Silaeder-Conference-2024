import flet as ft
from timetable import get_timetable
import flet.map as map
from satels import satel_list, choose_satels

def main(page: ft.Page):
    page.title = "Satellite datatable"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    marker_layer_ref = ft.Ref[map.MarkerLayer]()
    satel_map = map.Map(
            expand=8,
            configuration=map.MapConfiguration(
                initial_center=map.MapLatitudeLongitude(15, 10),
                initial_zoom=4.2,
                interaction_configuration=map.MapInteractionConfiguration(
                    flags=map.MapInteractiveFlag.ALL
                )
            ),
                layers=[
                    map.TileLayer(
                        url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                        on_image_error=lambda e: print("TileLayer Error"),

                    ),
                    map.MarkerLayer(
                        ref=marker_layer_ref,
                        markers= []

                    )
                ]
    )

    textes = []
    for i in satel_list:
        textes.append(ft.Checkbox(label=i, value=False))
    def view_satellites(e):
        marker_layer_ref.current.markers = []
        input_for_choose = []
        for i in textes:
            if i.value == True:
                input_for_choose.append(i.label)
        # print(input_for_choose)
        input_for_choose = choose_satels(input_for_choose)
        print(input_for_choose)
        for i in range(len(input_for_choose)):
            marker_layer_ref.current.markers.append(
                map.Marker(
                    content=ft.Icon(
                        ft.icons.SATELLITE_ALT, color=ft.cupertino_colors.SYSTEM_PURPLE, tooltip=input_for_choose[i][0]
                    ),
                    coordinates=map.MapLatitudeLongitude(input_for_choose[i][1][1], input_for_choose[i][1][0])
                )
            )
        page.update()
    view = ft.TextButton("View selected satellites", on_click=view_satellites)
    column_checkbox = ft.Column(textes + [view], expand=1)
    tab2 = ft.Row(
            [satel_map,
            column_checkbox], expand=True
        )
    def navigate(e):
        print(e)
        if e.data == '0':
            page.controls = [tab1, navigation]
        else:
            page.controls = [tab2, navigation]
        page.update()
    navigation = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.SCHEDULE, label="Timetable"),
            ft.NavigationBarDestination(icon=ft.icons.MAP, label="Satellite map")
        ],
        on_change=navigate
    )
    datatable = ft.DataTable(
                        columns=[
                            ft.DataColumn(ft.Text("Satellite name")),
                            ft.DataColumn(ft.Text("Rise time")),
                            ft.DataColumn(ft.Text("Max-elevation time")),
                            ft.DataColumn(ft.Text("Fall time")),
                            ft.DataColumn(ft.Text("Culmination azimyth")),
                            ft.DataColumn(ft.Text("Culmination elevation"))
                        ]
                )
                
    
    def update_timetable(event):
        new_timetable = get_timetable()
        rows = []
        for i in new_timetable:

            row = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(i[0])),
                        ft.DataCell(ft.Text(i[1].strftime('%d.%m.%Y-%H:%M:%S'))),
                        ft.DataCell(ft.Text(i[2].strftime('%d.%m.%Y-%H:%M:%S'))),
                        ft.DataCell(ft.Text(i[3].strftime('%d.%m.%Y-%H:%M:%S'))),
                        ft.DataCell(ft.Text(f"{i[4]:.2f}")),
                        ft.DataCell(ft.Text(f"{i[5]:.2f}"))

                    ],
                )
            rows.append(row)
        datatable.rows = rows
        page.update()
        

    reorganise = ft.TextButton("Update timetable", on_click=update_timetable, expand=1)
    
    scrolltable = ft.Column([datatable], expand=4, scroll=True)
    tab1 = ft.Row([scrolltable,  reorganise],
                expand=1,
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment = ft.CrossAxisAlignment.START        
        )

    page.add(
        tab1,
        navigation
            #     [
            #         ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
            #         txt_number,
            #         ft.IconButton(ft.icons.ADD, on_click=plus_click),
            #     ],
        
    )


ft.app(main)