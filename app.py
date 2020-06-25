import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.Text(('Enter something on Row 2'), key='-TEXT-')],
          [sg.Button('7', size=(5, 1), key='_BUTTON_7_'), sg.Button('8', size=(5, 1), key='_BUTTON_8_'),
           sg.Button('9', size=(5, 1), key='_BUTTON_9_'),
           sg.Button(' + ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_SUM_')],
          [sg.Button('4', size=(5, 1), key='_BUTTON_4_'), sg.Button('5', size=(5, 1), key='_BUTTON_5_'),
           sg.Button('6', size=(5, 1), key='_BUTTON_6_'),
           sg.Button(' - ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_SUB_')],
          [sg.Button('1', size=(5, 1), key='_BUTTON_1_'), sg.Button('2', size=(5, 1), key='_BUTTON_2_'),
           sg.Button('3', size=(5, 1), key='_BUTTON_3_'),
           sg.Button(' x ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_M_')],
          [sg.Button(' ⌫  ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_DEL_'),
           sg.Button('0', size=(5, 1), key='_BUTTON_0_'),
           sg.Button('=', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_RESULT_'),
           sg.Button(' ÷ ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_DIV_')]
          ]

window = sg.Window('Calculadora', layout)

window['-TEXT-'].update('My new text value')

while True:
    event, values = window.read()
    if event == '_BUTTON_1_':
        print(event);
    if event == '_BUTTON_2_':
        print(event);
    if event == '_BUTTON_3_':
        print(event);
    if event == '_BUTTON_4_':
        print(event);
    if event == '_BUTTON_5_':
        print(event);
    if event == '_BUTTON_6_':
        print(event);
    if event == '_BUTTON_7_':
        print(event);
    if event == '_BUTTON_8_':
        print(event);
    if event == '_BUTTON_9_':
        print(event);
    if event == '_BUTTON_0_':
        print(event);
    if event == '_BUTTON_SUM_':
        print(event);
    if event == '_BUTTON_SUB_':
        print(event);
    if event == '_BUTTON_M_':
        print(event);
    if event == '_BUTTON_DIV_':
        print(event);
    if event == '_BUTTON_DEL_':
        print(event);
    if event == '_BUTTON_RESULT_':
        print(event);
    if event == sg.WIN_CLOSED:
        break
