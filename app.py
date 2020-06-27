import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.In(enable_events=True, do_not_clear=False, key='_IN_', size=(30, 3))],
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

window = sg.Window('Calculadora', layout, return_keyboard_events=True)

while True:
    event, values = window.read()

    num = float(values['_IN_']);

    if event == '_BUTTON_1_':
        print(num)
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
        n1 = num;
        op = "soma";
        window['_IN_'].update(value=[0])
    if event == '_BUTTON_SUB_':
        n1 = num;
        op = "sub";
        window['_IN_'].update(value=[0])
    if event == '_BUTTON_M_':
        n1 = num;
        op = "mult";
        window['_IN_'].update(value=[0])
    if event == '_BUTTON_DIV_':
        n1 = num;
        op = "div";
        window['_IN_'].update(value=[0])
    if event == '_BUTTON_DEL_':
        print(event);
    if event == '_BUTTON_RESULT_':
        n2 = num;
        if op == 'soma':
            soma = n1+n2
            window['_IN_'].update(value=[soma]);
        if op == 'sub':
            sub = n1-n2
            window['_IN_'].update(value=[sub]);
        if op == 'mult':
            mult = n1*n2
            window['_IN_'].update(value=[mult]);
        if op == 'div':
            div = n1/n2
            window['_IN_'].update(value=[div]);
    if event == sg.WIN_CLOSED:
        break;
