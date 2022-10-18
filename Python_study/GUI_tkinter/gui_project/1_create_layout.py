from tkinter import*

root = Tk()
root.title('JW GUI')

#파일 프레임 (파일 추가,선택 삭제)
file_frame = Frame(root)
file_frame.pack()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='파일추가')
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text='선택삭제')
btn_del_file.pack(side="right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack()

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


root.resizable(False, False)
root.mainloop()