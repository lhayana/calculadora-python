import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [[sg.In(enable_events=True, do_not_clear=False, key='_IN_', size=(30, 3))],
          [sg.Button('7', size=(5, 1)), sg.Button('8', size=(5, 1)),
           sg.Button('9', size=(5, 1)),
           sg.Button(' + ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_SUM_')],
          [sg.Button('4', size=(5, 1)), sg.Button('5', size=(5, 1)),
           sg.Button('6', size=(5, 1)),
           sg.Button(' - ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_SUB_')],
          [sg.Button('1', size=(5, 1)), sg.Button('2', size=(5, 1)),
           sg.Button('3', size=(5, 1)),
           sg.Button(' x ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_M_')],
          [sg.Button(' ⌫  ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_DEL_'),
           sg.Button('0', size=(5, 1)),
           sg.Button('=', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_RESULT_'),
           sg.Button(' ÷ ', button_color=('black', 'orange'), size=(5, 1), key='_BUTTON_DIV_')]
          ]

window = sg.Window('Calculadora', layout, return_keyboard_events=True)

while True:
    event, values = window.read()

    #num = float(values['_IN_']);

    if event == '_BUTTON_DEL_':  # clear keys if clear button
        keys_entered = '';
    elif event in '1234567890':
        keys_entered = values['_IN_']  # get what's been entered so far
        keys_entered += event
        print(keys_entered)
        window['_IN_'].update(value=[keys_entered])

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
