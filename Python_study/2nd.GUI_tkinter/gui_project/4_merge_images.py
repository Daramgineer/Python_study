import os
from tkinter import* #__all__에 없는건 import안함
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image
import tkinter.messagebox as msgbox

root = Tk()
root.title('JW GUI')
root.geometry('800x680')

#파일추가
def add_file():
    #initialdir : 저장소 최초 오픈위치
    files = filedialog.askopenfilenames(title='이미지 파일을 선택하세요', filetypes=(('PNG 파일', '*.PNG'), ('모든 파일', '*.*')), initialdir=r'/Users/jw_cha/Code Develop/Python_study/Python_study/Python_study/Game/pygame_project/images')
    #사용자가 선택한 파일목록
    for file in files:
        list_file.insert(END, file)

#파일삭제
def del_file():
   #list_file.curselection() #선택파일 index 특정
    for index in reversed(list_file.curselection()): #reversed:순서를 거꾸로 바꿔서 다른곳에 저장, reverse:순서를 바꿔서 바로저장
        list_file.delete(index)

#저장경로(폴더선택)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

#이미지 통합
def merge_image(): #세로로 나열하도록 통합
    images = [Image.open(x) for x in list_file.get(0, END)]
    #size -> size[0] : width, size[1] : height
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images달

    widths, heights = zip(*(x.size for x in images)) #*붙이면 각 첫번쨰, 두번쨰 성분들 묶어서 전달

    #최대넓이 전체높이 구하기
    max_width, total_height = max(widths), sum(heights) #가로 최대, 세로 총합

    #스케치북 준비
    result_img = Image.new('RGB', (max_width, total_height), (255, 255, 255))
    y_offset=0 #이미지 세로 간격

    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1) / len(images) * 100 #실제 %정보 계산
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), 'JW Photo.jpg')
    result_img.save(dest_path)
    msgbox.showinfo('알림', '작업이 완료되었습니다.')

#시작
def start():
    if list_file.size() == 0:
        msgbox.showwarning('경고', '이미지 파일을 추가하세요')
        return
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning('경고', '저장 경로를 추가하세요')
        return
    #이미지 통합 작업
    merge_image()

#파일 프레임 (파일 추가,선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='파일추가', command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text='선택삭제', command=del_file)
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

btn_dest_path = Button(path_frame, text='찾아보기', width=10, command=browse_dest_path)
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
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill='x', padx=5, pady=5)

#실행프레임
frame_run = Frame(root)
frame_run.pack(fill='x', padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text='닫기', width=12, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5) #생성순서가 오른쪽부터 진행됨

btn_start = Button(frame_run, padx=5, pady=5, text='시작', width=12, command=start)
btn_start.pack(side='right', padx=5, pady=5)

root.resizable(False, False)
root.mainloop()