from random import choice
from flet import *
h = 750;w=350
class App(UserControl):
  def __init__(self,pg):
    super().__init__()
    # pg.bgcolor = colors.TRANSPARENT
    # pg.window_bgcolor = colors.TRANSPARENT
    # pg.window_title_bar_hidden =True
    # pg.window_frameless = True
    self.pg = pg
    self.animation_style = animation.Animation(500,AnimationCurve.DECELERATE)
    
    
    

    self.init_helper()

  def init_helper(self):
    self.side_bar_column = Column(
        spacing=0,
        controls=[
          Row(
            controls=[
              Container(
                data = 0,
                on_click=lambda e: self.switch_page(e,'page1'),
                expand=True,
                height=40,
                content=Icon(
                  icons.CHAT_BUBBLE,
                  color='blue'
                ),
              ),
            ]
          ),

          
          Row(
            controls=[
              Container(
                on_click=lambda e: self.switch_page(e,'page2'),
                data = 1,
                expand=True,
                height=40,
                content=Icon(
                  icons.BADGE,
                  color='blue'
                ),
              ),
            ]
          ),


          Row(
            controls=[
              Container(
                expand=True,
                height=40,
                data = 2,
                on_click=lambda e: self.switch_page(e,'page3'),
                content=Icon(
                  icons.AUDIO_FILE,
                  color='blue'
                ),
              ),
            ]
          ),

        ]
      )

    self.indicator =Container(
      height=40,
      bgcolor='red',
      offset=transform.Offset(0,0),
      animate_offset=animation.Animation(500,AnimationCurve.DECELERATE)
    )

    self.page1 = Container(
      alignment=alignment.center,
      offset=transform.Offset(0,0),
      animate_offset=self.animation_style,
      bgcolor='blue',
      content=Text('PAGE 1',size=50)
    )

    self.page2 = Container(
      alignment=alignment.center,
      offset=transform.Offset(0,0),
      animate_offset=self.animation_style,
      bgcolor='green',
      content=Text('PAGE 2',size=50)
    )

    self.page3 = Container(
      alignment=alignment.center,
      offset=transform.Offset(0,0),
      animate_offset=self.animation_style,
      bgcolor='orange',
      content=Text('PAGE 3',size=50),
    )

    self.switch_control = {
      'page1':self.page1,
      'page2':self.page2,
      'page3':self.page3,
    }

    self.pg.add(
      Container(
        bgcolor='white',
        expand=True,
        content=Row(
          spacing=0,
          controls=[
            Container(
              width=80,
              # bgcolor='green',
              border=border.only(right=border.BorderSide(width=1,color='#22888888'),),
              content=Column(
                alignment='spaceBetween',
                controls=[
                  
                  Container(
                    height=100,
                    # bgcolor='blue'
                  ),






                  Container(
                    height=500,
                    content=Row(
                      spacing=0,
                      controls=[
                        Container(
                          expand=True,
                          content=self.side_bar_column,

                        ),
                        Container(
                          width=3,
                          content=Column(
                            controls=[
                              self.indicator,
                            ]
                          ),

                        ),
                      ]
                    )
                  ),









                  Container(
                    height=50,
                  ),
                ]
              )
            ),


            Container(
              expand=True,
              content=Stack(
                controls=[
                  self.page1,
                  self.page2,
                  self.page3,

                ]
              )
            ),
          ]
        )

      )
    )


  def switch_page(self,e,point):
    print(point)
    for page in self.switch_control:
      self.switch_control[page].offset.x = 2
      self.switch_control[page].update()

    self.switch_control[point].offset.x = 0
    self.switch_control[point].update()
      
    self.indicator.offset.y = e.control.data
    self.indicator.update()

app(target=App,assets_dir='assets')