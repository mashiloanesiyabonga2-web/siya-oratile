import flet as ft
import random
import asyncio
import os

def main(page: ft.Page):
    # --- SETTINGS ---
    page.title = "Siya & Oratile ❤️"
    
    page.window.icon = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48cGF0aCBkPSJNNTAgODUgQzUwIDg1IDEwIDU1IDEwIDMwIEMxMCAxNSAyNSAxMCAzNSAxMCBDNDUgMTAgNTAgMjAgNTAgMjAgQzUwIDIwIDU1IDEwIDY1IDEwIEM3NSAxMCA5MCAxNSA5MCAzMCBDOTAgNTUgNTAgODUgNTAgODUgWiIgZmlsbD0iI2Q2MzM4NCIvPjx0ZXh0IHg9IjUwIiB5PSI0OCIgZm9udC1zaXplPSIyNCIgZm9udC1mYW1pbHk9IkFyaWFsIiBmb250LXdlaWdodD0iYm9sZCIgZmlsbD0id2hpdGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiPk9NPC90ZXh0Pjwvc3ZnPg=="
    
    page.bgcolor = "#f4f4f9" 
    page.padding = 0
    page.spacing = 0

    # --- CATEGORY DATA ---
    categories = {
        "Reasons I Love You": {
            "icon": ft.Icons.FAVORITE,
            "color": "#ff3366",
            "messages": [
                "I love the way your eyes light up when you talk about things you love.",
                "You have the cutest laugh, and I would do anything to hear it.",
                "My favorite place in the whole world is right next to you.",
                "I love how safe and warm I feel when I'm with you.",
                "You're my favorite hello and my hardest goodbye."
            ]
        },
        "Our Playlist": {
            "icon": ft.Icons.MUSIC_NOTE,
            "color": "#ffb703",
            "messages": [
                "I made this playlist just for you. Press play and think of me! 💕",
                "https://open.spotify.com/playlist/67phQVtCiyzLW0zwLB4Jy2?si=b79b80dcf9844b0a"
            ]
        },
        "When You Miss Me": {
            "icon": ft.Icons.MAIL,
            "color": "#219ebc",
            "messages": [
                "If you're reading this, just know I'm probably thinking about you right now.",
                "Here's a virtual forehead kiss for you 😘",
                "I wish I could wrap my arms around you right this second.",
                "You're my favorite notification, my favorite thought, my favorite everything."
            ]
        },
        "Why You're Special": {
            "icon": ft.Icons.STAR,
            "color": "#8338ec",
            "messages": [
                "You are my safe space. With you, I can completely be myself.",
                "You have a way of making the whole world slow down when you smile at me.",
                "You inspire me to be a better man every single day.",
                "You understand me in ways no one else ever has."
            ]
        }
    }

    # --- RAINING HEARTS BACKGROUND ---
    def create_heart():
        return ft.Stack(
            [
                ft.Icon(ft.Icons.FAVORITE, color="#ffb3c6", size=50),
                ft.Container(
                    content=ft.Text("SIYA\nLOVES\nYOU", size=7, color="white", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD, font_family="Arial"),
                    alignment=ft.Alignment.CENTER, width=50, height=50,
                )
            ],
            width=50, height=50,
        )

    heart_layer = ft.Stack(expand=True)
    
    async def drop_and_remove_heart(heart):
        await asyncio.sleep(0.05)
        heart.top = page.height + 100 if page.height else 800
        page.update()
        await asyncio.sleep(3.2) 
        if heart in heart_layer.controls:
            heart_layer.controls.remove(heart)
            page.update()

    async def rain_hearts():
        while True:
            heart = create_heart()
            heart.animate_position = ft.Animation(3000, ft.AnimationCurve.LINEAR)
            heart.top = -80
            heart.left = random.randint(0, max(1, int(page.width - 50) if page.width else 1200))
            
            heart_layer.controls.append(heart)
            page.update()
            page.run_task(drop_and_remove_heart, heart)
            
            await asyncio.sleep(random.uniform(0.04, 0.12))

    page.run_task(rain_hearts)

    # --- DIALOG POP-UP FUNCTION ---
    def open_category_dialog(e, cat_name):
        cat_data = categories[cat_name]
        message_controls = []
        
        for msg in cat_data["messages"]:
            if msg.startswith("http"):
                message_controls.append(
                    ft.TextButton(
                        content=ft.Text("🎵 Open Spotify Playlist 🎵", color="#1DB954", weight=ft.FontWeight.BOLD),
                        url=msg
                    )
                )
            else:
                message_controls.append(
                    ft.Text(msg, size=16, color="#444444")
                )

        dialog = ft.AlertDialog(
            title=ft.Text(cat_name, color=cat_data["color"], weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column(message_controls, spacing=15, scroll=ft.ScrollMode.AUTO),
                width=400,
                height=250
            ),
            actions=[
                ft.TextButton("Close", on_click=lambda e: close_dialog(dialog))
            ]
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

    # --- NAVIGATION LOGIC ---
    home_view = ft.Column(spacing=0, expand=True, scroll=ft.ScrollMode.AUTO)
    about_view = ft.Column(spacing=0, expand=True, scroll=ft.ScrollMode.AUTO, visible=False)
    catalog_view = ft.Column(spacing=0, expand=True, scroll=ft.ScrollMode.AUTO, visible=False)

    def show_home(e):
        about_view.visible = False
        catalog_view.visible = False
        home_view.visible = True
        page.update()

    def show_about(e):
        home_view.visible = False
        catalog_view.visible = False
        about_view.visible = True
        page.update()

    def show_catalog(e):
        home_view.visible = False
        about_view.visible = False
        catalog_view.visible = True
        page.update()

    # --- HEADER ---
    def create_header():
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("Siya ❤️ Oratile", size=24, weight=ft.FontWeight.BOLD, color="#1e1e24"),
                    ft.Row(
                        controls=[
                            ft.TextButton("Home", on_click=show_home, style=ft.ButtonStyle(color="#ff3366")),
                            ft.TextButton("About", on_click=show_about, style=ft.ButtonStyle(color="#555555")),
                            ft.TextButton("Snowball's Catalog", on_click=show_catalog, style=ft.ButtonStyle(color="#555555")),
                        ],
                        spacing=10
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=ft.Padding(left=50, top=20, right=50, bottom=20),
            bgcolor=ft.Colors.with_opacity(0.95, "#ffffff"),
            shadow=ft.BoxShadow(blur_radius=10, color="#0d000000")
        )

    # --- BUILD HOME VIEW ---
    home_view.controls.append(create_header())
    
    home_view.controls.append(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Keeping My Heart in\nTouch with Yours.", size=42, weight=ft.FontWeight.BOLD, color="#ffffff", font_family="Arial"),
                    ft.Text("A modern approach to loving you every single day.", size=16, color="#cccccc"),
                    ft.Row(
                        controls=[
                            ft.Button(content=ft.Text("Read Our Story", color="#333333", weight=ft.FontWeight.BOLD), bgcolor="#ffffff", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)), on_click=show_about),
                            ft.Button(content=ft.Text("Contact Me", color="#ffffff", weight=ft.FontWeight.BOLD), bgcolor="#ff3366", style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)))
                        ],
                        spacing=15
                    )
                ],
                spacing=20
            ),
            bgcolor=ft.Colors.with_opacity(0.95, "#1e1e24"), 
            padding=ft.Padding(left=50, top=80, right=50, bottom=80),
            alignment=ft.Alignment.TOP_LEFT
        )
    )

    home_view.controls.append(
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("We found our creative\nspace that is open for\nyou.", size=28, weight=ft.FontWeight.BOLD, color="#1e1e24", expand=1),
                    ft.Text("Every day with you is a gift. Take your time exploring this little space I made for you, Oratile.", size=15, color="#666666", expand=1)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=ft.Padding(left=50, top=60, right=50, bottom=60),
            bgcolor=ft.Colors.with_opacity(0.95, "#ffffff")
        )
    )

    cards_row = ft.Row(wrap=True, spacing=20, run_spacing=20, alignment=ft.MainAxisAlignment.CENTER)
    for name, data in categories.items():
        card = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(content=ft.Icon(data["icon"], color="#ffffff", size=24), bgcolor=data["color"], padding=12, border_radius=50),
                    ft.Text(name, size=18, weight=ft.FontWeight.BOLD, color="#1e1e24"),
                    ft.Text("Click to open", size=13, color="#888888"),
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.START
            ),
            bgcolor="#ffffff",
            padding=25,
            border_radius=10,
            width=260,
            shadow=ft.BoxShadow(blur_radius=15, color="#0d000000"),
            on_click=lambda e, n=name: open_category_dialog(e, n),
            ink=True
        )
        cards_row.controls.append(card)

    home_view.controls.append(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Explore Our World", size=24, weight=ft.FontWeight.BOLD, color="#1e1e24", text_align=ft.TextAlign.CENTER),
                    ft.Container(height=20),
                    cards_row
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.Padding(left=50, top=60, right=50, bottom=60),
            bgcolor=ft.Colors.with_opacity(0.95, "#f8f9fa")
        )
    )

    # Footer
    footer = ft.Container(
        content=ft.Row(
            controls=[
                ft.Column([ft.Text("Siya's Corner", color="#ffffff", weight=ft.FontWeight.BOLD, size=18)]),
                ft.Column([ft.Text("Made for", color="#ffffff", weight=ft.FontWeight.BOLD, size=14), ft.Text("Oratile", color="#ff3366", size=12)]),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor=ft.Colors.with_opacity(0.95, "#1e1e24"),
        padding=ft.Padding(left=50, top=40, right=50, bottom=40)
    )
    home_view.controls.append(footer)


    # --- BUILD ABOUT VIEW ---
    about_view.controls.append(create_header())
    about_view.controls.append(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("My Everything", size=38, weight=ft.FontWeight.BOLD, color="#ff3366", font_family="Arial"),
                    ft.Container(height=10),
                    ft.Text(
                        "Oratile, I just want you to know how deeply and completely I love you. You are the most beautiful woman I have ever met, both inside and out. Your beauty radiates in everything you do, in your smile, and in the way you light up a room just by walking into it. I am so incredibly lucky to call you mine. You make my heart feel full and my life so much brighter. I love everything about you—your laugh, your mind, your heart. You are my absolute everything, and I will love you endlessly.", 
                        size=20, color="#444444", text_align=ft.TextAlign.CENTER
                    ),
                    ft.Container(height=40),
                    ft.Icon(ft.Icons.FAVORITE, color="#ff3366", size=60),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.Padding(left=100, top=80, right=100, bottom=80),
            bgcolor=ft.Colors.with_opacity(0.95, "#ffffff"),
            expand=True
        )
    )
    about_view.controls.append(footer)

    # --- BUILD CATALOG VIEW ---
    catalog_view.controls.append(create_header())
    
    gallery_grid = ft.Row(wrap=True, spacing=20, run_spacing=20, alignment=ft.MainAxisAlignment.CENTER)
    
    img_folder = "images"
    valid_exts = (".jpg", ".jpeg", ".png", ".JPG", ".PNG", ".JPEG")
    
    if os.path.exists(img_folder):
        image_files = [f for f in os.listdir(img_folder) if f.endswith(valid_exts)]
        
        def sort_key(filename):
            try:
                return int(filename.split('.')[0])
            except ValueError:
                return filename
        
        image_files.sort(key=sort_key)
        
        for filename in image_files:
            gallery_grid.controls.append(
                ft.Container(
                    content=ft.Image(
                        src=filename, 
                        width=250, 
                        height=300, 
                        fit="cover", 
                        border_radius=15
                    ),
                    width=250,
                    height=300,
                    shadow=ft.BoxShadow(blur_radius=15, color="#0d000000"),
                    border_radius=15,
                    bgcolor="#f0f0f0"
                )
            )

    catalog_view.controls.append(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Snowball's Catalog ❄️📸", size=38, weight=ft.FontWeight.BOLD, color="#ff3366", font_family="Arial"),
                    ft.Container(height=10),
                    ft.Text("A collection of my favorite pictures of you.", size=18, color="#666666"),
                    ft.Container(height=40),
                    gallery_grid
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=ft.Padding(left=50, top=60, right=50, bottom=80),
            bgcolor=ft.Colors.with_opacity(0.95, "#f4f4f9"),
            expand=True
        )
    )
    catalog_view.controls.append(footer)


    # --- PUT IT ALL TOGETHER ---
    page.add(
        ft.Stack(
            [
                heart_layer, 
                home_view,
                about_view,
                catalog_view
            ],
            expand=True
        )
    )

if __name__ == "__main__":
    # Runs as a website. Render provides the PORT; locally it falls back to 8550.
    port = int(os.environ.get("PORT", 8550))
    on_server = "PORT" in os.environ
    ft.run(
        main,
        assets_dir="images",
        view=ft.AppView.WEB_BROWSER,
        host="0.0.0.0" if on_server else None,
        port=port,
    )