from PolyResearchModules import *

import os, tkinter as tk, ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

lt = 2500

def get_urls(tab, driver):
	driver.switch_to.window(tab)
	return [driver.current_url, tab]

def get_title(tab, driver):
	driver.switch_to.window(tab)
	return [driver.title, tab]

def switch_refresh_youtube(tab, driver):
	driver.switch_to.window(tab)
	driver.refresh()
	time.sleep(5)
	commoncustomization()
	playlistcustomization()
	time.sleep(0.5)

def switch_commoncustomization(tab, driver):
	driver.switch_to.window(tab)
	commoncustomization(0.5)
	time.sleep(0.5)

def commoncustomization(lt=lt):
	# for wait in range(lt):
		# try: ytviewer.execute_script('document.getElementsByClassName(`html5-main-video`)[0].playbackRate = 16'); break
		# except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
		
	# for wait in range(lt):
		# try: ytviewer.execute_script('video = document.querySelector(`video.video-stream.html5-main-video`); video.playbackRate = 16; /*video.style.display=`none`*/'); break
		# except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
	
	ltlist = mmin.dstatial(int, str(frak(lt).limit_denominator()).split('/'))
	if len(ltlist) == 1: ltlist += [1]
	
	iterwait, timewait = int(ltlist[0]), 0.5/ltlist[1]
		
	for wait in range(iterwait):
		try: ytviewer.execute_script('document.querySelector(`button[aria-label="Play (k)"]`).click()'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException):
			try: ytviewer.execute_script('document.querySelector(`button[aria-label="Pause (k)"]`).outerHTML'); break
			except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)
		
	for wait in range(iterwait):
		try: ytviewer.execute_script('video = document.querySelector(`video.video-stream.html5-main-video`); video.playbackRate = 16; /*video.style.display=`none`*/'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)
		
	for antivideo in range(2):
		for wait in range(iterwait):
			try: ytviewer.execute_script('document.querySelector(`video.video-stream.html5-main-video`).outerHTML=``'); break
			except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)
			
		for wait in range(iterwait):
			try: ytviewer.execute_script('document.querySelector(`button[aria-label="Play (k)"]`).click()'); break
			except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException):
				try: ytviewer.execute_script('document.querySelector(`button[aria-label="Pause (k)"]`).outerHTML'); break
				except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)
		
	for wait in range(iterwait):
		try: ytviewer.execute_script('document.querySelector(`ytd-comments`).outerHTML=``'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)
		
	for wait in range(iterwait):
		try: ytviewer.execute_script('document.querySelector(`div#related`).outerHTML=``'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)
		
	for wait in range(iterwait):
		try: ytviewer.execute_script('document.querySelector(`div#masthead-container.ytd-app`).outerHTML=``'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)
		
	for wait in range(iterwait):
		try: ytviewer.execute_script('document.querySelector(`ytd-video-secondary-info-renderer`).outerHTML=``'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(timewait)

def settingscustomization():
	try:
		ytviewer.execute_script('document.querySelector(`button.ytp-settings-button`).click()')
		time.sleep(0.5)
		ytviewer.execute_script('menuitems = document.querySelectorAll(`div.ytp-menuitem`); menuitems[menuitems.length-1].click()')
		# ytviewer.execute_script('menuitems = document.querySelectorAll(`div.ytp-menuitem`)[3].click()')
		time.sleep(0.5)
		ytviewer.execute_script('qualitylist = document.querySelectorAll(`div.ytp-quality-menu .ytp-menuitem`); qualitylist[qualitylist.length-2].click()')
		
	except selenium.common.exceptions.JavascriptException: pass
	
	try: ytviewer.execute_script('document.querySelector(`button[aria-label="Mute (m)"]`).click()')
	except selenium.common.exceptions.JavascriptException: pass
	
	time.sleep(0.5)
	
	try: ytviewer.execute_script('document.querySelector(`button[aria-label="Play (k)"]`).click()')
	except selenium.common.exceptions.JavascriptException: pass

def playlistcustomization():
	for wait in range(lt):
		try: ytviewer.execute_script('document.querySelector(`button[aria-label="Loop playlist"]`).click()'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
		
	for wait in range(lt):
		try: ytviewer.execute_script('document.querySelector(`button[aria-label="Shuffle playlist"]`).click()'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
		
	for wait in range(lt):
		try: ytviewer.execute_script('document.querySelector(`ytd-playlist-panel-renderer`).outerHTML=``'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
		

try: ytviewer.quit()
except NameError: pass
# del ytviewer

# def ytvieweraction():
# if 1:
while 1:
	try: ytviewer.current_url
	except KeyboardInterrupt: raise
	except:
		# chromedriver = r'C:\Program Files (x86)\chromedriver_win32\chromedriver.exe'
		
		chromedriver = r"D:\SL\Others\Siao Lung's Courses\! Creating Websites\! Selenium Webdriver\chromedriver.exe"
		my_own_chrome_options = Options()
		my_own_chrome_options.add_argument("start-minimized")
		my_own_chrome_options.add_argument("--window-size=50,50")
		my_own_chrome_options.add_argument("--headless")
		
		# my_own_chrome_options.add_argument("--window-size=1920,1080")
		# my_own_chrome_options.add_argument("start-maximized")
		# my_own_chrome_options.binary_location(chromedriver)
		
		try:
			ytviewer = webdriver.Chrome(executable_path=chromedriver, service_args=["hide_console"], chrome_options=my_own_chrome_options)
			ytviewer.set_window_position(2500, 2000)
			
		except KeyboardInterrupt: raise
		except: exec(open(r"D:\SL\Others\Siao Lung's Courses\! Creating Websites\! Selenium Webdriver\PolyResearchModules.pyw").read()); ytviewer = webdriver.Chrome(executable_path=chromedriver, service_args=["hide_console"]) #, chrome_options=options)
		
		#ytviewer: 'Youtube Viewer'
		
		ytviewer.execute_script('window.location.href = `https://www.youtube.com/watch?v=SZiWazYKERI`')
		time.sleep(2)
		
		
		
		try:
			# ytviewerwindow.text = 'Preparing 1st Video...'
			# ytviewerwindow.title(ytviewer.text[:-3]+' - Youtube Viewer')
			
			time.sleep(1)

			if '<div id="autoplay" class="style-scope ytd-compact-autoplay-renderer">Autoplay</div>' in ytviewer.execute_script('return document.querySelector(`html`).outerHTML'):
				ytviewer.execute_script('document.querySelector(`paper-toggle-button.ytd-compact-autoplay-renderer`).click()')

			commoncustomization()

			time.sleep(31)
			
			# for n in range(1):
			# for n in range(7):
			# for n in range(15):
			# for n in range(30):
			
			mul = 4
			ntabs = 10*mul
			
			for n in range(np.int64(ntabs)):
				# ytviewerwindow.text = 'Looping %s Playlists Simultaneously...' % ntabs
				# ytviewerwindow.title(ytviewer.text[:-3]+' - Youtube Viewer')
				
				# ytviewer.execute_script('window.open(`https://www.youtube.com/watch?v=yIF3PPsyQOs&list=UUIZ_L4DcRxVOfkXLQ-065xA`)')
				
				# link = 'https://www.youtube.com/playlist?list=UUXnVpgsY9kn0uomakXVzmIA&playnext=1&index=1'
				# link = 'https://www.youtube.com/playlist?list=' + ['UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(1, 52), ['UUVN62YFLZFSPfleSMSLtOlg&playnext=1&index=%s' % np.random.randint(1, 16), 'UUXnVpgsY9kn0uomakXVzmIA&playnext=1&index=1'][n > 21]][n > 12]
				
				# link = 'https://www.youtube.com/watch?v=SZiWazYKERI'
				link = 'https://www.youtube.com/playlist?list=' + ['UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(1, 52), ['UUVN62YFLZFSPfleSMSLtOlg&playnext=1&index=%s' % np.random.randint(1, 16), 'UUXnVpgsY9kn0uomakXVzmIA&playnext=1&index=1'][n > 7*mul]][n > 4*mul]
				
				# link = 'https://www.youtube.com/playlist?list=' + ['UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(1, 52), ['UUVN62YFLZFSPfleSMSLtOlg&playnext=1&index=%s' % np.random.randint(1, 16), 'UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(1, 52)][n > 7]][n > 4]
				# link = 'https://www.youtube.com/playlist?list=' + ['UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(0, 52), ['UUVN62YFLZFSPfleSMSLtOlg&playnext=1&index=%s' % np.random.randint(0, 16), 'UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(0, 52)][n > 10]][n > 6]
				# link = 'https://www.youtube.com/playlist?list=' + ['UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(0, 52), ['UUVN62YFLZFSPfleSMSLtOlg&playnext=1&index=%s' % np.random.randint(0, 16), 'UUIZ_L4DcRxVOfkXLQ-065xA&playnext=1&index=%s' % np.random.randint(0, 52)][n > 6]][n > 3]
				# + '&playnext=1&index=1'
				# link = 'https://www.youtube.com/playlist?list=' + ['UUIZ_L4DcRxVOfkXLQ-065xA', ['UUVN62YFLZFSPfleSMSLtOlg', 'UUXnVpgsY9kn0uomakXVzmIA'][n > 7]][n > 4] + '&playnext=1&index=1'
				
				ytviewer.execute_script('window.open(`%s`)' % link)
				time.sleep(0.5)
				if not n: ytviewer.close(); time.sleep(0.5)
				ytviewer.switch_to.window(ytviewer.window_handles[-1])
				time.sleep(2)

				settingscustomization()

				try: ytviewer.execute_script('document.querySelector(`button[aria-label="Mute (m)"]`).click()')
				except selenium.common.exceptions.JavascriptException: pass
				
				time.sleep(0.5)
				
				try: ytviewer.execute_script('document.querySelector(`button[aria-label="Play (k)"]`).click()')
				except selenium.common.exceptions.JavascriptException: pass

				time.sleep(1)

				commoncustomization()
				playlistcustomization()
				
				
		except KeyboardInterrupt: raise
		
		except:
			ytviewer.quit()
			# del ytviewer
			exec(ef.read(r"Youtube Viewer.pyw"))
			print(format_exc(), file=sys.stderr, end='\n'*3)
	
		

	try: mmin.dstatial(lambda tab: switch_commoncustomization(tab, ytviewer), ytviewer.window_handles)
	except selenium.common.exceptions.WebDriverException: pass

	# if not int(time.strftime('%M', time.localtime(time.time()))) % 5 and int(time.strftime('%S', time.localtime(time.time()))) == 0:
	if not int(time.strftime('%M', time.localtime(time.time()))) % 10 and int(time.strftime('%S', time.localtime(time.time()))) == 0:
		ytviewer.quit()
		# del ytviewer
	
	elif not int(time.strftime('%M', time.localtime(time.time()))) % 1 and int(time.strftime('%S', time.localtime(time.time()))) == 0:
		try: mmin.dstatial(lambda tab: switch_refresh_youtube(tab, ytviewer), ytviewer.window_handles)
		except selenium.common.exceptions.WebDriverException: continue
		
		
# ytvieweraction()

##ytviewerwindow = tk.Tk()
##ytviewerbtn = tk.Button(ytviewerwindow, text='Youtube Viewer', font=['Arial', 30], command=ytvieweraction)
##ytviewerlabel = tk.Label(ytviewerwindow, font=['Arial', 30])
##
##ytviewerbtn.pack()
##ytviewerlabel.pack()
##
##ytviewerwindow.title('Youtube Viewer')
##ytviewerwindow.mainloop()
