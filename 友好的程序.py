import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Unclosable Window")
    root.geometry("600x450")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    # 正确的密码
    correct_password = "123456"

    def check_password():
        entered_password = entry.get()
        if entered_password == correct_password:
            # 清除所有部件
            for widget in root.winfo_children():
                widget.destroy()
            label = tk.Label(root, text="密码正确", bg="lightgreen", width=30, height=2)
            label.pack()
            # 2秒后退出
            root.after(2000, root.destroy)
        else:
            label = tk.Label(root, text="密码错误，请重新输入", bg="lightcoral", width=30, height=2)
            label.pack()

    def disable_event():
        pass

    root.protocol("WM_DELETE_WINDOW", disable_event)
    #创建提示文字
    label = tk.Label(root, text="输入密码，否则永远别想退出", font=('华文中宋',30),fg='red', width=30, height=2)
    label.pack()
    # 创建一个输入框
    entry = tk.Entry(root, show="*",bd=5,width=30)
    entry.pack()

    label = tk.Label(root, text="")
    label.pack()
    # 创建一个按钮
    button = tk.Button(root, text="确认", command=check_password)
    button.pack()


    root.mainloop()


if __name__ == "__main__":
    main()
