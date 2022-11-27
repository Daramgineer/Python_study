from tkinter import*
import tkinter.ttk as ttk

root = Tk()
root.title('JW GUI')
root.geometry('800x680')

#파일 프레임 (파일 추가,선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='파일추가')
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text='선택삭제')
btn_del_file.pack(side="right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#저장경로 프레임
path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4) #ipady : 높이변경

btn_dest_path = Button(path_frame, text='찾아보기', width=10)
btn_dest_path.pack(side='right', padx=5, pady=5)

#옵션 프레임
frame_option = LabelFrame(root, text='옵션')
frame_option.pack(padx=5, pady=5, ipady=5)

#1. 가로넓이 옵션
#가로넓이 레이블
lbl_width = Label(frame_option, text='가로넓이', width=8)
lbl_width.pack(side='left', padx=5, pady=5)

#가로넓이 콤보
opt_width = ['원본유지', '1024', '800', '640']
cmb_width = ttk.Combobox(frame_option, state='readonly', values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side='left', padx=5, pady=5)

#2. 간격옵션
#간격옵션 레이블
lbl_space = Label(frame_option, text='간격', width=8)
lbl_space.pack(side='left', padx=5, pady=5)

#간격옵션 콤보
opt_space = ['없음', '좁게', '보통', '넓게']
cmb_space= ttk.Combobox(frame_option, state='readonly', values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side='left', padx=5, pady=5)

#3. 파일 포맷 옵션
#파일포맷옵션 레이블
lbl_format = Label(frame_option, text='포맷', width=8)
lbl_format.pack(side='left', padx=5, pady=5)

#파일포맷옵션 콤보
opt_format = ['PNG', 'JPG', 'BMP']
cmb_format= ttk.Combobox(frame_option, state='readonly', values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side='left', padx=5, pady=5)

#진행상황 progress bar
frame_progress = LabelFrame(root, text='진행상황')
frame_progress.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_ber = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_ber.pack(fill='x', padx=5, pady=5)

#실행프레임
frame_run = Frame(root)
frame_run.pack(fill='x', padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text='닫기', width=12, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5) #생성순서가 오른쪽부터 진행됨

btn_start = Button(frame_run, padx=5, pady=5, text='시작', width=12)
btn_start.pack(side='right', padx=5, pady=5)

root.resizable(False, False)
root.mainloop()