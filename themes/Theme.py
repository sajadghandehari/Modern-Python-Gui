def setting_page_theme(self, baseColor, color_B, toolBoxhover, color_D,
                                textColor, groupBoxtitle, lineEdit, 
                                lineEditFocus, border):

    # setting page

    self.setStyleSheet(f"background-color:{baseColor};")


    # self.tabWidget.setStyleSheet(f"background-color:{color_B};")
    # self.groupBox_2.setStyleSheet(f"background-color:{color_B};")
    # self.groupBox.setStyleSheet(
    #     f"background-color:{color_B};font: 87 9pt 'Roboto Black';")

    self.toolBox.setStyleSheet(f"""
        QToolBox {{
            background-color: {color_B};  
            border-radius: 5px;  
        }}
        QToolBox::tab {{
            background-color: {color_B};  
            color: {textColor};    
            border: 1px solid {border};  
            border-radius: 3px;  
        }}
        QToolBox::tab:hover {{
            background-color: {toolBoxhover};  
            color: #ffffff;  
        }}
    """)
    
    self.tbSimulationSetting.setStyleSheet(f"""
        QToolBox {{
            background-color: {color_B};  
            border-radius: 5px;  
        }}
        QToolBox::tab {{
            background-color: {color_B};  
            color: {textColor};    
            border: 1px solid {border};  
            border-radius: 3px;  
        }}
        QToolBox::tab:hover {{
            background-color: {toolBoxhover};  
            color: #ffffff;  
        }}
    """)


    for groupBoxIndex in range(1,4):
        groupBox = getattr(self, f"groupBox{groupBoxIndex}")
        groupBox.setStyleSheet(f"""
            QGroupBox {{
                color: {textColor}; 
                border: 2px solid {border}; 
                border-radius: 10px; 
            }}
            QLabel {{
                color: {textColor}; 
            }}
            QGroupBox::title {{
                background-color: {groupBoxtitle};
                color: {textColor}; 
                border: 2px solid {border}; 
                border-radius: 5px;
            }}
            QLineEdit {{
                background-color: {lineEdit};
                border: 1px solid {border}; 
                border-radius: 3px; 
            }}
            QLineEdit:focus {{
                border-color: {lineEditFocus}; 
            }}
            QDateTimeEdit {{
                background-color: {lineEdit};
            }}
            QComboBox {{
                background-color: {lineEdit};
                border: 1px solid {border}; 
                border-radius: 3px; 
            }}
            QComboBox::drop-down {{
                background-color: {border}; 
                border: 1px solid {border}; 
                color: {lineEdit};
                padding: 2px; 
                width: 10px; 
            }}

        """)


