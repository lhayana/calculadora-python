import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.In(enable_events=True, do_not_clear=True, key='_IN_', size=(30, 1))],
          [sg.Button('7', size=(5, 1)), sg.Button('8', size=(5, 1)),
           sg.Button('9', size=(5, 1)),
           sg.Button(' + ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_SUM_')],
          [sg.Button('4', size=(5, 1)), sg.Button('5', size=(5, 1)),
           sg.Button('6', size=(5, 1)),
           sg.Button(' - ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_SUB_')],
          [sg.Button('1', size=(5, 1)), sg.Button('2', size=(5, 1)),
           sg.Button('3', size=(5, 1)),
           sg.Button(' x ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_M_')],
          [sg.Button(' CE  ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_DEL_'),
           sg.Button('0', size=(5, 1)),
           sg.Button('=', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_RESULT_'),
           sg.Button(' ÷ ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_DIV_')]
          ]

window = sg.Window('Calculadora', layout, return_keyboard_events=False)
keys_entered = ''

while True:
    event, values = window.read()

    if event == '_BUTTON_DEL_':
        keys_entered = '';
        n1 = 0;
        n2 = 0;
        window['_IN_'].update(value=[0])

    elif event in '1234567890':
        keys_entered += event
        print(keys_entered)
        window['_IN_'].update(value=[keys_entered])

    elif event == '_BUTTON_SUM_':
        n1 = int(keys_entered);
        keys_entered = '';
        op = "soma";
    elif event == '_BUTTON_SUB_':
        n1 = int(keys_entered);
        keys_entered = '';
        op = "sub";
    elif event == '_BUTTON_M_':
        n1 = int(keys_entered);
        keys_entered = '';
        op = "mult";
    elif event == '_BUTTON_DIV_':
        n1 = int(keys_entered);
        keys_entered = '';
        op = "div";

    elif event == '_BUTTON_RESULT_':
        n2 = int(keys_entered);
        if op == 'soma':
            soma = n1+n2
            window['_IN_'].update(value=[soma]);
        elif op == 'sub':
            sub = n1-n2
            window['_IN_'].update(value=[sub]);
        elif op == 'mult':
            mult = n1*n2
            window['_IN_'].update(value=[mult]);
        elif op == 'div':
            div = n1/n2
            window['_IN_'].update(value=[div]);
    if event == sg.WIN_CLOSED:
        break;
