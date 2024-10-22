import flet as ft


# general settings + style

DELTA_WIDHT: int = 80
DELTA_HEIGHT: int = 160

card_style: dict = {
        "width": 160,
    "height": 180,
    "bgcolor": "#FFFFFF",
    "border_radius": 5,
    "animate": ft.Animation(420, "easeInOutBack"),
    "data": False,
    "clip_behavior": ft.ClipBehavior.HARD_EDGE,
    "shadow": ft.BoxShadow(
        spread_radius = 1,
        blur_radius=10,
        color = ft.colors.with_opacity(0.21, "black"),
        offset = ft.Offset(2, 2),
    ),
    "scale": ft.transform.Scale(1.6),
}

def create_data_points(time: str, status: str, bar: str):
    
    
    return ft.Container(
        height= 40 if bar == "short" else 60,
        border = ft.border.only(
            left = ft.BorderSide(2, ft.colors.with_opacity(0.31, "black")) if status != "Ready for delivery" else ft.border.BorderSide(2, "blue")
        ),
        padding = ft.padding.only(left = 35),
        content=ft.Column(
            alignment="start",
            horizontal_alignment="start",
            spacing=0,
            controls=[
                ft.Text(time, size = 10, color = "black", opacity=0.81),
                ft.Text(status, size = 14, color = "black", weight="w500"),
            ]
        )
    )
    



# button class 
class Button(ft.Container):
    def __init__(self) -> None:
        super().__init__(
            **card_style,
            on_click=self.open,
            on_animation_end=self.post_open,
        )


        self.details: dict[str, dict[str, str]] = {
            "start": {"time": "12.40 am", "status": "Shipped to hub", "bar": "short"},
            "middle": {"time": "03:44 pm", "status": "Packaging boxes", "bar": "long"},
            "end": {"time": "9:00 pm", "status": "Ready for delivery", "bar": "short"},
        }




        self.logo = ft.Image(
            src = "Logo_NIKE.svg.png",
            width=90, 
            height=75
        )


        self.status = ft.Text('ready for delivery'.upper(), 
                              size=10, color="black")
        
        self.status_ball = ft.Container(
            width = 6, height= 6,
            shape=ft.BoxShape("circle"),
            bgcolor = "blue"

        )

        self.status_row = ft.Row(
            controls=[self.status_ball, self.status],
            vertical_alignment="center",
            alignment="center",
            spacing=5,
            opacity=1,
            animate_opacity=ft.Animation(100),
        )

        self.info = ft.Column(
            opacity=0,
            animate_opacity = ft.Animation(30),
            controls=[
                create_data_points(
                    item["time"], item["status"], item["bar"]
                )
                for item in self.details.values()
            ],
        )        

        self.content = ft.Column(
            alignment= "start",
            horizontal_alignment= "center",
            controls=[
                ft.Divider(height=5, color = "transparent"),
                ft.Row(controls = [self.logo], alignment="center"),
                ft.Text("JUST DO IT", size = 21, color= "black",  font_family="Open Sans"),
                ft.Divider(height=5, color = "transparent"),
                self.status_row, self.info,
            ],
        )


    def execute_status_logic(self, event):
        self.status_row.visible = False if event.control.data else True
        self.status_row.opacity = 0 if event.control.data else 1

        self.status_row.update()


    def execute_info_logic(self, event):
        self.info.visible = True if event.control.data else False
        self.info.opacity = 1 if event.control.data else 0
        self.info.update()


    def post_open(self, event):
        if event.control.data:
            self.execute_info_logic(event)
            self.execute_status_logic(event)

            

        else:
            self.execute_info_logic(event)
            self.execute_status_logic(event)
            
            

        


    def open(self, event):

        self.info.opacity = 0 if event.control.data else self.info.opacity
        self.info.update()

        self.status_row.opacity = 0     

        self.width += DELTA_WIDHT if not event.control.data else -DELTA_WIDHT

        self.height += DELTA_HEIGHT if not event.control.data else -DELTA_HEIGHT

        self.data = not event.control.data

        self.update()



def main (page: ft.Page) -> None: 
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#E1E6ED"

    button: ft.Container = Button()

    page.add(button)
    page.update()







if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")