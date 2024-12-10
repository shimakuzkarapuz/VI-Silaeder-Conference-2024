import flet as ft
import flet.map as map
from satels import satel_list, choose_satels

def main(page: ft.Page):
    page.title = "Satellite map"
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
                    coordinates=map.MapLatitudeLongitude(input_for_choose[i][1][0], input_for_choose[i][1][1])
                )
            )
        page.update()
    view = ft.TextButton("View selected satellites", on_click=view_satellites)
    column_checkbox = ft.Column(textes + [view], expand=1)
    tab2 = ft.Row(
            [satel_map,
            column_checkbox], expand=True
        )
    page.add(
        ft.Row(
            [satel_map,
            column_checkbox], expand=True
        )
    )

ft.app(main)