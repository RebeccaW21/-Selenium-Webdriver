from PolyResearchModules import *

def switchtourl(url, driver):
	tabtitle, i = '', 0
	try:
		while url not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url

	except IndexError: pass

try: driver.current_url
except:
	chromedriver = r"D:\SL\Others\Siao Lung's Courses\! Creating Websites\! Selenium Webdriver\chromedriver.exe"
	my_own_chrome_options = Options()
	my_own_chrome_options.add_argument("start-maximized")
	# my_own_chrome_options.add_argument("--headless")
	# my_own_chrome_options.binary_location(chromedriver)
	
	driver = webdriver.Chrome(executable_path=chromedriver, service_args=["hide_console"], chrome_options=my_own_chrome_options)


def pearsontrimassignlist():
	global driver	
	commandlist = [lambda: driver.switch_to.frame(driver.execute_script('return document.querySelector("iframe#centerIframe")')),
	lambda: driver.execute_script('document.querySelector(`div.xlbootstrap3 div.xlbootstrap3`).outerHTML=``'),
	lambda: driver.execute_script('document.querySelector(`div.xlbootstrap3 div.xlbootstrap3`).outerHTML=``'),
	lambda: driver.execute_script('document.querySelector(`.xlbootstrap3 table`).outerHTML=``'),
	lambda: driver.execute_script('document.querySelector(`.xlbootstrap3 table`).outerHTML=``')]

	try:
		for cl in commandlist:
			try: cl()
			except:
				noelementwin = tk.Tk()
				noelementalert = tk.Label(noelementwin, text='Come on!\nTry one more time!', font=('Arial', '30'))
				noelementalert.pack()
				noelementwin.title('Assignment Trim Error: Try one more time!')
##				noelementwin.mainloop()
				print(format_exc())
				
		assignwscore = [row for row in bsc(driver.execute_script('return document.querySelector(`.xlbootstrap3 .assignement-list-table`).outerHTML')).select('tr') if '>see score<' in str(row)]

		for i in range(len(assignwscore)-3):
			driver.execute_script('document.querySelector(`.xlbootstrap3 .assignement-list-table tbody > tr`).outerHTML=``')

		driver.execute_script('document.body.style.zoom = `150%`;')

		driver.switch_to.default_content()


	except:
		noelementwin = tk.Tk()
		noelementalert = tk.Label(noelementwin, text='Come on!\nTry one more time!', font=('Arial', '30'))
		noelementalert.pack()
		noelementwin.title('Assignment Trim Error: Try one more time!')
##		noelementwin.mainloop()
		print(format_exc())


##	time.sleep(0.5)
##	driver.execute_script('document.body.style.zoom = `100%`;')

##	time.sleep(0.5)
##	driver.execute_script('return document.querySelector(`a[aria-label="Assignments"]`).click()')
##
##	time.sleep(0.5)
##	driver.switch_to.frame(driver.execute_script('return document.querySelector("iframe#centerIframe")'))
##
##	time.sleep(0.5)
##	driver.execute_script(bsc(driver.execute_script('return document.querySelector(".xlbootstrap3 .assignement-list-table tbody").outerHTML')).select('th.assignmentNameColumn[valign="middle"][scope="row"]')[0].select('a')[0]['href'][11:])
##
##	time.sleep(1.5)
##	driver.execute_script([str(cont)[str(cont).find('javascript:doExercise')+11:str(cont).find(');"')+1] for cont in bsc(driver.execute_script('return document.querySelector(".xlbootstrap3 ul.question-details").outerHTML')).select('li') if '0/' in str(cont)][0])
##
##	time.sleep(1)
##	pearsontrim()

def pearsongo():
	global driver	
	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException:
		driver.switch_to.window(driver.window_handles[-1])
		tabtitle, i = driver.current_url, 0

	try:
		while 'login.pearson.com' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url

	except IndexError:
		driver.execute_script('window.open("https://portal.mypearson.com/portal")')
		tabtitle, i = driver.current_url, 0
		while 'pearson.com' not in tabtitle:
			driver.switch_to.window(driver.window_handles[i])
			i += 1
			tabtitle = driver.current_url

	username = driver.find_element_by_css_selector('input[id="username"][name="username"]')
	password = driver.find_element_by_css_selector('input[type="password"]')

	usn, pwd = mma.sum(mmin.dstatial(lambda x: cc.all2a[x], [23, 31, 22, 19, 11, 33, 19, 14, 20, 11, 20, 11])), mma.sum(mmin.dstatial(lambda x: cc.all2a[x], [8, 4, 3, 1, 1, 2, 44, 40]))
	username.send_keys(usn)
	password.send_keys(pwd)

	driver.find_element_by_css_selector('button[type="submit"]').click()
	time.sleep(2)
	driver.find_element_by_css_selector('div[ng-enter="launchCourse($event)"]').click()
	time.sleep(2)
	driver.find_element_by_css_selector('span[title="Assignments"] a[href=""][ng-bind="item.title"]').click()
	time.sleep(3)

	driver.execute_script('document.querySelector(`header`).outerHTML=``')
	driver.execute_script('document.querySelector(`.ov-content-header .container-fluid`).outerHTML=``')
	driver.execute_script('document.querySelector(`div.navbar-default`).outerHTML=``')
	driver.execute_script('document.querySelector(`div.footer`).outerHTML=``')
	driver.execute_script('document.body.style.zoom = `120%`;')

	pearsontrimassignlist()


def symbolabgo():
	global driver	
	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	try:
		while 'symbolab.com/solver' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url

	except IndexError:
		tabtitle, i = '', 0
		driver.execute_script('window.open("https://symbolab.com/solver")')
		while 'symbolab.com' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url


##	try: driver.execute_script('document.querySelector("button.privacy-policy").click()')
##	except selenium.common.exceptions.JavascriptException: pass

	driver.execute_script('document.querySelector(`button.btn.btn-large.btn-custom.search`).click()')
	time.sleep(1)

	driver.execute_script('''

	document.querySelector(`div[class="nl-leftNav print-hide"]`).outerHTML=``
	document.querySelector(`div[class="sidebar-content print-hide"]`).outerHTML=``
	$(`div.nl-content`).css(`margin-left`,`0%`)
	document.querySelector(`div#nl-mainNav`).outerHTML=``;
	document.querySelector(`div#nl-subNav`).outerHTML=``;
	document.querySelector(`div.nl-pageHeader`).outerHTML=``;
	document.querySelector(`section#verify-section`).outerHTML=``;
	document.querySelector(`div.googleAdsenseMiddle`).outerHTML=``;
	document.querySelector(`section[id="Examples"][class="print-hide"]`).outerHTML=``;
	document.querySelector(`section[id="related"]`).outerHTML=``;
	document.querySelector(`div.nl-footer`).outerHTML=``;
	document.querySelector(`div.solution-codepad-header.print-hide`).outerHTML=``;
	document.querySelector(`button.btn-custom.search`).style.display='none';
	document.querySelector(`.mathquill-input.mathquill-editable`).style.width='92%';
	document.querySelector(`svg.nl-saveNoteFave`).outerHTML='';

	''')
	time.sleep(0.5)
	driver.execute_script('document.querySelector(`button.privacy-policy`).click()')


def pearsoninteractive():
	global driver	
	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	while 'media.pearsoncmg.com' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
	driver.execute_script('document.querySelector(`div.content-panel`).style.height=`100%`')


def pearsonex():
	global driver	
	tabtitle, i = '', 0
	try:
		while 'xlitemprod.pearsoncmg.com' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
		driver.close()

	except IndexError: pass

	#tabtitle, i = driver.title, 0
	tabtitle, i = '', 0
	while 'Do Homework' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.title

	driver.switch_to.default_content()
	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[title="Question Viewer"]`);'))
	time.sleep(1)
	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[data-dojo-attach-point="activityFrame"][id="activityFrame"]`);'))
	time.sleep(1)
	try:
		driver.execute_script('document.querySelector(`%s`).click()' % ['td#%s' % cont['id'] for cont in bsc(driver.find_element_by_css_selector('body').get_attribute('outerHTML')).select("td.dijitMenuItemLabel") if '>View an Example<' in str(cont)][0])
		time.sleep(3)
		driver.execute_script('document.querySelector(`%s`).click()' % sorted(['td#%s' % cont['id'] for cont in bsc(driver.find_element_by_css_selector('body').get_attribute('outerHTML')).select("td.dijitMenuItemLabel") if '>Print<' in str(cont)])[-1])

	except IndexError:
		noexwin = tk.Tk()
		noexalert = tk.Label(noexwin, text='There is no example here.\nI think you must watch\nthe f**king bulls**t supposedly easy math video!', font=('Arial', '30'))
		noexalert.pack()
		noexwin.title('F**king Bulls**t Supposedly Easy Math Video!')
##		noexwin.mainloop()

def pearsontrim():
	global driver	
	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	while 'mathxl.com' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url

	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[title="Question Viewer"]`);'))
	time.sleep(0.5)

	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[data-dojo-attach-point="activityFrame"][id="activityFrame"]`);'))
	time.sleep(0.5)

	try: driver.execute_script('document.querySelector(`div.messagePanel[data-dojo-type="dijit.layout.ContentPane"]`).outerHTML = ``;')
	except selenium.common.exceptions.JavascriptException: pass
	time.sleep(0.5)

	try: driver.execute_script('document.querySelector(`div[data-dojo-attach-point="controlPanelContainer"] td.left`).outerHTML = ``;')
	except selenium.common.exceptions.JavascriptException: pass
	time.sleep(0.5)

	try: driver.execute_script('document.querySelector(`div[data-dojo-attach-point="controlPanelContainer"] td.center`).outerHTML = ``;')
	except selenium.common.exceptions.JavascriptException: pass
	time.sleep(0.5)

##	try: driver.execute_script('document.querySelector(`div[data-dojo-attach-point="controlPanelContainer"] td.right div.nextPrevPanel`).outerHTML = ``;')
##	selenium.common.exceptions.JavascriptException: pass
##	time.sleep(0.5)

	try: driver.execute_script('document.querySelector(`div.palettePanel[data-dojo-type="dijit.layout.ContentPane"]`).outerHTML = ``;')
	except selenium.common.exceptions.JavascriptException: pass
	time.sleep(0.5)

	driver.switch_to.default_content()
	time.sleep(0.5)

	try: driver.execute_script('document.querySelector("div.xlbootstrap3 #mainTopNavContainer.navbar-inverse").outerHTML = "";')
	except selenium.common.exceptions.JavascriptException: pass
	time.sleep(0.5)

	try: driver.execute_script('document.querySelector("body.math").style.paddingTop = "0px";')
	except selenium.common.exceptions.JavascriptException: pass
	time.sleep(0.5)

	try: driver.execute_script('document.querySelector(".xlbootstrap3 iframe").height=500;')
	except selenium.common.exceptions.JavascriptException: pass
	time.sleep(0.5)

##	pearsontrimbtn.pack_forget()


def pearsonprintallq():
	global driver	
	tabtitle, i = '', 0
	try:
		while 'xlitemprod.pearsoncmg.com' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
		driver.close()

	except IndexError: pass


	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	while 'mathxl.com/Student/PlayerHomework.aspx?' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
	driver.switch_to.default_content()
	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[title="Question Viewer"]`);'))
	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[data-dojo-attach-point="activityFrame"][id="activityFrame"]`);'))
	driver.execute_script('document.querySelector(`'+['td#'+cont['id'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap td.dijitMenuItemLabel') if '>Print<' in str(cont)][0]+'`).click()')
##	driver.execute_script('document.querySelector(`'+['td[for="%s"]' % cont['for'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap label') if '>Print homework assignment<' in str(cont)][-1]+'`).click()')
	time.sleep(2)
	driver.execute_script('document.querySelector(`'+['label[for="%s"]' % cont['for'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap label') if '>Print homework assignment<' in str(cont)][-1]+'`).click()')
	driver.execute_script('document.querySelector(`'+['button#'+cont['id'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap .xlDialog .xlDialogButtonContainer .btn') if '>Print<' in str(cont)][0]+'`).click()')
	driver.execute_script('document.querySelector(`'+['button#'+cont['id'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap .xlDialog .xlDialogButtonContainer .btn') if '>Cancel<' in str(cont)][0]+'`).click()')

def pearsonprintsingleq():
	global driver	
	tabtitle, i = '', 0
	try:
		while 'xlitemprod.pearsoncmg.com' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
		driver.close()

	except IndexError: pass


	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	while 'mathxl.com/Student/PlayerHomework.aspx?' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
	driver.switch_to.default_content()
	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[title="Question Viewer"]`);'))
	driver.switch_to.frame(driver.execute_script('return document.querySelector(`iframe[data-dojo-attach-point="activityFrame"][id="activityFrame"]`);'))
	driver.execute_script('document.querySelector(`'+['td#'+cont['id'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap td.dijitMenuItemLabel') if '>Print<' in str(cont)][0]+'`).click()')
##	driver.execute_script('document.querySelector(`'+['td[for="%s"]' % cont['for'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap label') if '>Print homework assignment<' in str(cont)][-1]+'`).click()')
	time.sleep(2)
	driver.execute_script('document.querySelector(`'+['label[for="%s"]' % cont['for'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap label') if '>Print this question only<' in str(cont)][-1]+'`).click()')
	driver.execute_script('document.querySelector(`'+['button#'+cont['id'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap .xlDialog .xlDialogButtonContainer .btn') if '>Print<' in str(cont)][0]+'`).click()')
	driver.execute_script('document.querySelector(`'+['button#'+cont['id'] for cont in bsc(driver.execute_script('return document.querySelector(`body`).outerHTML')).select('.dbootstrap .xlDialog .xlDialogButtonContainer .btn') if '>Cancel<' in str(cont)][0]+'`).click()')

def pearsonlesson():
	global driver	
	tabtitle, i = '', 0
	try:
		while 'openvellum.ecollege.com/course.html' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url

	except IndexError: pass

	driver.execute_script('document.querySelector(`a[aria-label="Assignments"]`).click()')
	time.sleep(0.5)
	driver.switch_to.default_content()
	time.sleep(0.5)
	driver.switch_to.frame(driver.execute_script('return document.querySelector("iframe#centerIframe")'))
	time.sleep(0.5)

	assignments = bsc(driver.execute_script('return document.querySelector("html").outerHTML')).select('tr')
	assignwscore = [assignment for assignment in assignments if 'see score' in str(assignment)]
	assignpastdue = [assignment for assignment in assignments if 'past due\n' in str(assignment)]
	assignnew = [assignment for assignment in assignments if 'assignmentNameColumn' in str(assignment)]

	if len(assignpastdue) > 0:
		driver.execute_script(assignpastdue[0].a['href'][11:])
		time.sleep(0.5)

	else:
		driver.execute_script(assignwscore[-1].a['href'][11:])
		time.sleep(0.5)

	if 'Improve Score' in driver.execute_script('return document.querySelector("html").outerHTML'):
		driver.execute_script('doHomework(false)')
		time.sleep(0.5)

	driver.switch_to.default_content()
	time.sleep(0.5)
	driver.switch_to.frame(driver.execute_script('return document.querySelector("iframe#centerIframe")'))
	time.sleep(0.5)
	questiondesc = bsc(driver.execute_script('return document.querySelector("html").outerHTML')).select('li.standardtotal')
	time.sleep(0.5)

	try: alreadylearnedchecker = questiondesc[0].getText().split(': ')[1] != questiondesc[1].getText().split(': ')[1]
	except IndexError: alreadylearnedchecker = ''

	if alreadylearnedchecker: driver.execute_script([question for question in bsc(driver.execute_script('return document.querySelector("html").outerHTML')).select('.xlbootstrap3 .question-details li') if '(0/' in str(question)][0].a['href'][11:])
	else:
		try: driver.execute_script('return document.querySelector(`a[aria-label="Assignments"]`).click()')
		except:
			if "selenium.common.exceptions.JavascriptException: Message: javascript error: Cannot read property 'click' of null" in format_exc():
##				driver.execute_script('window.history.back()')
				driver.switch_to.default_content()
				time.sleep(0.5)
				driver.execute_script('document.querySelector(`button.ov-toggle`).click()')
				time.sleep(0.5)
				driver.execute_script('document.querySelector(`a[aria-label="Assignments"]`).click()')

		time.sleep(0.5)
		driver.switch_to.frame(driver.execute_script('return document.querySelector("iframe#centerIframe")'))

		time.sleep(0.5)
		driver.execute_script(assignnew[0].a['href'][11:])
		time.sleep(0.5)

		driver.execute_script([question for question in bsc(driver.execute_script('return document.querySelector("html").outerHTML')).select('.xlbootstrap3 .question-details li') if '(0/' in str(question)][0].a['href'][11:])




def omnicalctrimming():
	global driver	
	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	while 'omnicalculator' not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
	time.sleep(3)
	driver.execute_script('''

document.querySelector(`div.CalculatorDescription`).outerHTML=``
document.querySelector(`div.Header`).outerHTML=``
document.querySelector(`div.CategoriesMenuV2`).outerHTML=``
document.querySelector(`div.promo-top`).outerHTML=``
document.querySelector(`div.IntroductionModal`).outerHTML=``
document.querySelector(`div.CalculatorPagePartCenter`).outerHTML=``
document.querySelector(`div.CalculatorPagePartRight`).outerHTML=``
document.querySelector(`div.Calculator__control-panel`).outerHTML=``
document.querySelector(`div.below`).outerHTML=``
document.querySelector(`div#calculator-page-bottom`).outerHTML=``
//document.querySelector(`div.CalculatorDescription __web-inspector-hide-shortcut__`).outerHTML=``
document.querySelector(`div.LeadImage`).outerHTML=``

''')
	try:
		while 1:
			driver.execute_script('''document.querySelector("iframe").outerHTML=``''')
	except selenium.common.exceptions.JavascriptException: pass

def sjeccd(destination):
	global driver	
	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	except:
		chromedriver = r"D:\SL\Others\Siao Lung's Courses\! Creating Websites\! Selenium Webdriver\chromedriver.exe"
		my_own_chrome_options = Options()
		my_own_chrome_options.add_argument("start-maximized")
		# my_own_chrome_options.add_argument("--headless")
		# my_own_chrome_options.binary_location(chromedriver)
		
		driver = webdriver.Chrome(executable_path=chromedriver, service_args=["hide_console"], chrome_options=my_own_chrome_options)

	canvaslink = 'sjeccd.instructure.com'

	try:
		while canvaslink not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url

	except (IndexError, selenium.common.exceptions.NoSuchWindowException):
		tabtitle, i = '', 0
		driver.execute_script('window.open("%s")' % destination)
		while canvaslink not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url


	usn, pwd = mma.sum(mmin.dstatial(lambda x: cc.all2a[x], [23, 31, 33, 19, 5, 3, 7, 2])), mma.sum(mmin.dstatial(lambda x: cc.all2a[x], [3, 2, 9, 9, 3, 2, 44, 14]))
	
	for wait in range(2500):
		try: driver.execute_script('document.querySelector(`input.ic-Input[type="text"]`).value = `%s`' % usn); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5); print(format_exc())
		
	for wait in range(2500):
		try: driver.execute_script('document.querySelector(`input.ic-Input[type="password"]`).value = `%s`' % pwd); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5); print(format_exc())
	
	# for wait in range(2500):
		# try: driver.execute_script('document.querySelector(`input.ic-Input[type="password"]`).type = `text`' % usn); break
		# except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5); print(format_exc())
	
	for wait in range(2500):
		try: driver.find_element_by_css_selector('input[type="checkbox"]').click(); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
	
	for wait in range(2500):
		try: driver.find_element_by_css_selector('button[type="submit"]').click(); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
	
	for wait in range(2500):
		try: driver.execute_script("document.querySelector('head').innerHTML += '<style>* {font-family: Arial !important; font-size: 20px !important}</style>';"); break
		except: time.sleep(0.5)

def datacamp(destination):
	global driver, usn, pwd
	
	try: tabtitle, i = driver.current_url, 0
	except selenium.common.exceptions.NoSuchWindowException: tabtitle, i = '', 0
	except:
		chromedriver = r"D:\SL\Others\Siao Lung's Courses\! Creating Websites\! Selenium Webdriver\chromedriver.exe"
		my_own_chrome_options = Options()
		my_own_chrome_options.add_argument("start-maximized")
		# my_own_chrome_options.add_argument("--headless")
		# my_own_chrome_options.binary_location(chromedriver)
		
		driver = webdriver.Chrome(executable_path=chromedriver, service_args=["hide_console"], chrome_options=my_own_chrome_options)

	canvaslink = 'sjeccd.instructure.com'

	
	# def switchtourl(url, driver):
	# ...
	##	except selenium.common.exceptions.NoSuchWindowException:
	##		tabtitle, i = '', 0
	##		while url not in tabtitle: driver.switch_to.window(driver.window_handles[i]); i += 1; tabtitle = driver.current_url
	
	# try:
		# switchtourl('datacamp', driver)
		# time.sleep(0.5)

	# except (IndexError, selenium.common.exceptions.WebDriverException):
		# driver.execute_script('window.location.href = `%s`' % destination)
		# time.sleep(0.5)

	##driver.execute_script('document.querySelector(`[data-qa="btnGoogleSignUp"]`).click()')
	##time.sleep(2)
	
	driver.switch_to.window(driver.window_handles[-1])
	
	for wait in range(2500):
		try: driver.execute_script('window.open(`https://www.datacamp.com/users/auth/google_oauth2`)'); break
		#; time.sleep(1.5));
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
	
	time.sleep(0.5)
	switchtourl('oauthchooseaccount', driver)
	time.sleep(0.5)
	
	# username = driver.find_element_by_css_selector('input[type="email"]')
	
	usn, pwd = mma.sum(mmin.dstatial(lambda x: cc.all2a[x], [23, 31, 22, 19, 11, 33, 19, 14, 20, 11, 20, 11, 25, 15, 19, 84, 17, 23, 11, 19, 22, 76, 13, 25, 23])), mma.sum(mmin.dstatial(lambda x: cc.all2a[x], [8, 4, 3, 1, 1, 2, 44, 40]))
	
	for wait in range(2500):
		try: driver.execute_script('document.querySelector(`input[type="email"]`).value = `%s`' % usn); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5); print(format_exc())
		
	# username.send_keys(usn)
	
	for wait in range(2500):
		try: driver.find_element_by_css_selector('button.VfPpkd-LgbsSe-OWXEXe-k8QpJ').click(); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
		
	time.sleep(1)
	# password = driver.find_element_by_css_selector('input[type="password"]')
	time.sleep(1.5)
	
	#https://campus.datacamp.com/courses/introduction-to-tensorflow-in-python/introduction-to-tensorflow?ex=2
	for wait in range(2500):
		try: driver.execute_script('document.querySelector(`input[type="password"]`).value = `%s`' % pwd); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5); print(format_exc())
	
	for wait in range(2500):
		try: driver.execute_script('document.querySelector(`div#passwordNext button`).click()'); break
		except (selenium.common.exceptions.JavascriptException, selenium.common.exceptions.StaleElementReferenceException): time.sleep(0.5)
		
	for wait in range(2500):
		try: driver.execute_script('window.location.href = `%s`' % destination); break
		except: time.sleep(0.5)

def datacamplogin(destination):
	global driver
	password = driver.find_element_by_css_selector('input[type="password"]')
	time.sleep(1.5)
	password.send_keys(pwd)
	driver.execute_script('document.querySelector(`div#passwordNext button`).click()')
	time.sleep(0.5)
	switchtourl('datacamp', driver)
	time.sleep(1.5)
	driver.execute_script('window.location.href = `%s`' % destination)

def datacampconsole():
	switchtourl('datacamp', driver)
	output = driver.execute_script('return document.querySelectorAll(`div[style="align-items: baseline; display: flex;"]`)')
	ppc.copy(bsc(mma.sum([out.get_attribute('outerHTML') for out in output])).get_text())
	
def datacampcompleted():
	switchtourl('datacamp', driver)
	output = driver.execute_script('return document.querySelectorAll(`div[style="align-items: baseline; display: flex;"]`)')
	ppc.copy(bsc(mma.sum([out.get_attribute('outerHTML') for out in output])).get_text()+'\n\n'+bsc(driver.execute_script('return document.querySelector(`div.dc-completed__body`).outerHTML')).get_text()[10:-22].replace('XP', 'XP\n'))
	driver.execute_script('document.querySelector(`button[data-cy="next-exercise-button"]`).click()')

def easybibgo(link):
	switchtourl('newtab', driver)
	driver.execute_script('window.location.href = ("https://www.easybib.com/mla8/website-citation/search?q=%s")' % link)
	time.sleep(0.5)

	while 1:
		try:
			driver.execute_script('document.querySelector("iframe").outerHTML=``')
		except selenium.common.exceptions.JavascriptException: break


	driver.execute_script('document.querySelector("div.hnpfkW").outerHTML = ""')
	driver.execute_script('document.querySelector("div.jEJLCP").style.display = "none"')
	driver.execute_script('document.querySelector("header.doMDEo").outerHTML = ""')

	time.sleep(0.5)
	for i in range(50):
		try: driver.execute_script('document.querySelector("div.fUvypd").outerHTML = "";')
		except selenium.common.exceptions.JavascriptException: pass

		try: driver.execute_script('document.querySelector("div.iJMJjW").outerHTML = "";')
		except selenium.common.exceptions.JavascriptException: pass

		##try: driver.execute_script('document.querySelector("div.hnpfkW").outerHTML = "";')
		##except selenium.common.exceptions.JavascriptException: pass

		##try: driver.execute_script('document.querySelector("div.jEJLCP").outerHTML = "";')
		##except selenium.common.exceptions.JavascriptException: pass

		try: driver.execute_script('document.querySelector("div.adds-wrapper").outerHTML = "";')
		except selenium.common.exceptions.JavascriptException: pass

	time.sleep(1)

	driver.find_element_by_css_selector('button[data-test="cite-button"]').click()
	time.sleep(2)

	driver.find_element_by_css_selector('a[data-test="submit-eval"]').click()

	time.sleep(2)

	driver.find_element_by_css_selector('button.complete-citation').click()

	time.sleep(2)

	driver.find_element_by_css_selector('button[data-test="citations-more-menu"]').click()
	time.sleep(2)

	driver.find_element_by_css_selector('button[data-test="dropdown-copy-citation"]').click()
	time.sleep(2)
	driver.find_element_by_css_selector('button[data-test="modal-close-button"]').click()
	time.sleep(0.5)
	driver.quit()
	print(ppc.paste())
	return ppc.paste()

import tkinter as tk, ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

browsingcommand = tk.Tk()
browsingcommand.title('Cyberworld Ship Command Center')

symbolablabel = tk.Label(browsingcommand, text='Symbolab:!', font=['Arial','40'])
symbolabgobtn = tk.Button(browsingcommand, text='Symbolab - GO!', command=symbolabgo, font=['Arial','20'])

pearsonlabel = tk.Label(browsingcommand, text='\nPearson:!', font=['Arial','40'])
pearsongobtn = tk.Button(browsingcommand, text='Pearson - GO!', command=pearsongo, font=['Arial','20'])
pearsontrimassignlistbtn = tk.Button(browsingcommand, text='Pearson - TRIM\nAssignments List!', command=pearsontrimassignlist, font=['Arial','20'])
pearsontrimlessonbtn = tk.Button(browsingcommand, text='Pearson - TRIM Lesson!', command=pearsontrim, font=['Arial','20'])
pearsonprintallqbtn = tk.Button(browsingcommand, text='Pearson - Print All Questions!', command=pearsonprintallq, font=['Arial','20'])
pearsonprintsingleqbtn = tk.Button(browsingcommand, text='Pearson - Print Single Questions!', command=pearsonprintsingleq, font=['Arial','20'])
pearsonlessonbtm = tk.Button(browsingcommand, text='Pearson - Lesson!', command=pearsonlesson, font=['Arial','20'])
pearsonexbtn = tk.Button(browsingcommand, command=pearsonex, font=['Arial','20'], text='Pearson - Example')
pearsoninteractivebtn = tk.Button(browsingcommand, command=pearsoninteractive, font=['Arial','20'], text='Pearson - Interactive')

omnicalclabel = tk.Label(browsingcommand, text='\nOmniCalc:!', font=['Arial','40'])
omnicalctrimbtn = tk.Button(browsingcommand, text='OmniCalc - TRIM!', command=omnicalctrimming, font=['Arial','20'])

canvaslabel = tk.Label(browsingcommand, text='\nCanvas:!', font=['Arial','40'])
canvaslinkdest = tk.Entry(browsingcommand, font=['Arial','20'])
canvasgobtn = tk.Button(browsingcommand, text='Canvas - GO!', command=lambda: sjeccd(canvaslinkdest.get()), font=['Arial','20'])

datacamplabel = tk.Label(browsingcommand, text='\nDatacamp:!', font=['Arial','40'])
datacamplinkdest = tk.Entry(browsingcommand, font=['Arial','20'])
datacampgobtn = tk.Button(browsingcommand, text='Datacamp - GO!', command=lambda: datacamp(datacamplinkdest.get()), font=['Arial','20'])
datacampconsolebtn = tk.Button(browsingcommand, text='Datacamp - Console!', command=datacampconsole, font=['Arial','20'])
datacampcompletedbtn = tk.Button(browsingcommand, text='Datacamp\n-\nCompleted Notes!', command=datacampcompleted, font=['Arial','20'])

easybiblabel = tk.Label(browsingcommand, text='\nEasybib:!', font=['Arial','40'])
easybibgocitedlink = tk.Entry(browsingcommand, font=['Arial','20'])
easybibgobtn = tk.Button(browsingcommand, text='Easybib - GO!', command=lambda: easybibgo(easybibgocitedlink.get()), font=['Arial','20'])

col1 = [symbolablabel, symbolabgobtn, pearsonlabel, pearsongobtn, pearsontrimassignlistbtn, pearsontrimlessonbtn]
col2 = [pearsonprintsingleqbtn, pearsonprintallqbtn, pearsonexbtn, pearsoninteractivebtn, omnicalclabel, omnicalctrimbtn, canvaslabel, canvaslinkdest, canvasgobtn]
col3 = [datacamplabel, datacamplinkdest, datacampgobtn, datacampconsolebtn, datacampcompletedbtn, easybiblabel, easybibgocitedlink, easybibgobtn]

# col1[0].pack(side='left')
for c1i in range(len(col1)):
	c1 = col1[c1i]
	# c1.pack()
	c1.grid(row=c1i, column=1)

# col2[0].pack(side='left')
for c2i in range(len(col2)):
	c2 = col2[c2i]
	# c2.pack()
	c2.grid(row=c2i, column=2)

# col3[0].pack(side='left')
for c3i in range(len(col3)):
	c3 = col3[c3i]
	# c3.pack()
	c3.grid(row=c3i, column=3)

# symbolablabel.pack()
# symbolabgobtn.pack()

# pearsonlabel.pack()
# pearsongobtn.pack()
# ##pearsonlessonbtm.pack()
# pearsontrimassignlistbtn.pack()
# pearsontrimlessonbtn.pack()
# pearsonprintsingleqbtn.pack()
# pearsonprintallqbtn.pack()

# pearsonexbtn.pack()

# pearsoninteractivebtn.pack()

##omnicalclabel.pack()
##omnicalctrimbtn.pack()

browsingcommand.mainloop()
