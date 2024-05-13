from flet import Page, app, Text, AppBar, colors, View, ListView, TextButton, ButtonStyle
from parser import get_currency_data


async def main(page: Page):
    page.window_height = 800
    page.window_width = 450
    page.bgcolor = "black"

    async def route_change(route):
        route.page.views.clear()
        route.page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Валюта"), bgcolor=colors.BLACK, color="White"),
                    lv,
                ], bgcolor="black"
            )
        )
        page.update()

    lv = ListView(expand_loose=False, expand=True, spacing=10)
    currency_data = await get_currency_data()
    for currency in currency_data:
        lv.controls.append(
            TextButton(text=f"{currency['Единиц']} {currency['Валюта']} - {currency['Курс']} руб.", height=60,
                       style=ButtonStyle(color="white"), adaptive=True))

    async def view_pop(view):
        view.page.views.pop()
        top_view = page.views[-1]
        view.page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


app(target=main)
