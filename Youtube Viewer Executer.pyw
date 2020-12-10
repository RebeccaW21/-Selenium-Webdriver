import os, tkinter as tk, ctypes, subprocess

command = 'python "! ! Youtube Viewer.pyw"'
proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


# ctypes.windll.shcore.SetProcessDpiAwareness(1)

# def ytvieweraction():
	# os.chdir(r"D:\SL\Others\Siao Lung's Courses\! Creating Websites\! Selenium Webdriver")
	# # ytviewerbtn['text'] = '\t'*3
	# exec(open(r"! ! Youtube Viewer.pyw").read())

# ytviewerwindow = tk.Tk()
# ytviewerbtn = tk.Button(ytviewerwindow, text='Youtube Viewer', font=['Arial', 30], command=ytvieweraction)
# ytviewerbtn.pack()
# ytviewerwindow.title('Youtube Viewer')
# ytviewerwindow.mainloop()