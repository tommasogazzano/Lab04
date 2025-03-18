import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self._time = None
        self._wrong = None
        self._mode = None
        self._sentence = None
        self._txtIn = None
        self._spell = None
        self._langSelector = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        self._langSelector = ft.Dropdown(label="Select language", hint_text="Seleziona una Lingua", options=[ft.dropdown.Option("english"),
                                                                                                     ft.dropdown.Option("spanish"),
                                                                                                     ft.dropdown.Option("italian")],
                                         on_change=self.__controller.handleSelezione)


        def handleCheck(e):
            self._sentence.value = f"{self._txtIn.value}!"
            self.page.update()

        self._txtIn = ft.TextField(label="Add your sentence here", disabled = False)
        self._spell = ft.Button(text = "Spell Check", on_click=self.__controller.handleCheck, color="blue")
        self._mode = ft.Dropdown(label = "Select Mode", options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"),
                                                                 ft.dropdown.Option("Dichotomic")])
        self._sentence = ft.Text()
        self._wrong = ft.Text()
        self._time = ft.Text()

        row1 = ft.Row(controls = [self._mode, self._txtIn, self._spell])

        self.page.add(self._langSelector, row1, self._sentence, self._wrong, self._time)

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
