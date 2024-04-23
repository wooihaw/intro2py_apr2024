import easygui as gui

# File open dialog box
infile = gui.fileopenbox(msg='Select file to open', title='Open file', default='*.txt')
if infile:
    with open(infile, encoding='utf-8') as file:
        mytext = file.readlines()
        # Text box to display multiple lines of editable text
        gui.textbox(msg='Showing contents of text file', title='Text file reader', text=mytext)

choices = ('Red', 'Green', 'Blue')
# Button box for selection with buttons
ans1 = gui.buttonbox(msg='Select your choice', title='Button box', choices=choices, default_choice='Red')
# Message box to display a message
gui.msgbox(msg='You have selected ' + ans1, title='Your selection')

# Choice box for selection from list
ans2 = gui.choicebox(msg='Select your choice', title='Choice Box', choices=choices, preselect=1)
gui.msgbox(msg='You have selected ' + ans2, title='Your selection')

# Enter box for entry of single line text
mytext2 = gui.enterbox(msg='Please enter some text', title='Enter text')
if mytext2:
    gui.msgbox(msg=mytext2, title='Your text')

    # Yes/No box for selecting 'yes' or 'no'
    ans3 = gui.ynbox(msg='Do you want to save your text?')
    if ans3:
        # File save dialog box
        file = gui.filesavebox(default='mytext.txt', filetypes='*.txt')
        if file == None:
            exit()
        with open(file, 'w') as savefile:
            savefile.writelines(mytext2)
