import tkinter as tk
import weibo 


USER_CONFIG = None

def read_config():
    global USER_CONFIG
    # 复用之前函数
    USER_CONFIG = weibo.get_config()
    return USER_CONFIG


checkbox_info = {}
checkbox_info["filter"] = "filter控制爬取范围，值为1代表爬取全部原创微博，值为0代表爬取全部微博（原创+转发）。"
checkbox_info["remove_html_tag"] = "remove_html_tag控制是否移除抓取到的weibo正文和评论中的html tag，值为1代表移除，值为0代表不移除"
checkbox_info["original_pic_download"] = "original_pic_download控制是否下载原创微博中的图片，值为1代表下载，值为0代表不下载"
checkbox_info["retweet_pic_download"] = "retweet_pic_download控制是否下载转发微博中的图片，值为1代表下载，值为0代表不下载"
checkbox_info["original_video_download"] = "original_video_download控制是否下载原创微博中的视频和原创微博Live Photo中的视频，值为1代表下载，值为0代表不下载"
checkbox_info["retweet_video_download"] = "retweet_video_download控制是否下载转发微博中的视频和转发微博Live Photo中的视频，值为1代表下载，值为0代表不下载"
checkbox_info["download_comment"] = "download_comment控制是否下载每条微博下的一级评论（不包括对评论的评论），仅当write_mode中有sqlite时有效，可取值为0和1"
checkbox_info["download_repost"] = ""
checkbox_info["result_dir_name"] = ""

def main():
    # create a tkinter window
    root = tk.Tk()
    root.title("Config编辑器")

    global USER_CONFIG
    read_config()
    # print(USER_CONFIG)

    # create a function to be called on checkbox click
    def checkbox_clicked():
        if checkbox_var.get() == 1:
            print("Checkbox is checked")
        else:
            print("Checkbox is not checked")

    row_num = 0






    # create a checkbox with default value set to True
    checkbox_var = tk.BooleanVar()
    checkbox_var.set(True)
    checkbox = tk.Checkbutton(root, text="Checkbox", variable=checkbox_var, command=checkbox_clicked)
    checkbox.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # create a label and text input field with default value set to "default text"
    label1 = tk.Label(root, text="Text Input:")
    label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    text_input_var = tk.StringVar()
    text_input_var.set("default text")
    text_input = tk.Entry(root, textvariable=text_input_var)
    text_input.grid(row=1, column=1, padx=10, pady=10)

    # create a label and value input field
    label2 = tk.Label(root, text="Value Input:")
    label2.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    value_input_var = tk.StringVar()
    value_input = tk.Entry(root, textvariable=value_input_var)
    value_input.grid(row=2, column=1, padx=10, pady=10)


    # create a listbox to display an array
    text = """会被搜索的user id列表:\n这里只供确认，修改请自行打开config.json"""
    label3 = tk.Label(root, text=text, anchor="w", justify="left")
    label3.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    array = ["apple", "banana", "cherry"]
    listbox = tk.Listbox(root, height=5, width=20)
    for item in array:
        listbox.insert(tk.END, item)
    listbox.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="w")


    # add padding to the bottom of the window
    bottom_frame = tk.Frame(root)
    bottom_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=(0, 50))




    # schedule the execution of my_function() in 1 seconds
    root.after(1000, read_config)

    # start the tkinter event loop
    root.mainloop()




if __name__ == "__main__":
    main()