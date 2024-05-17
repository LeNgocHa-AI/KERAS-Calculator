import tkinter as tk
from tkinter import *
import math as m
from sympy import *
import re as r
import random
import sys
import string
import webbrowser

version_of_calc = "Ver. 1.4 official"
url_help = "https://docs.google.com/forms/d/e/1FAIpQLSfRlg5Wo8wQpya0evQ00vT6waKZlB-eNCyYJY4q9T8ApKBemw/viewform?usp=sf_link"
key = ""
language = "Vietnamese"
choose_language = ["English", "Vietnamese", "Chinese", "Japanese"]

expression = ["|"]
output = ""
ans = 0
enter_eq = 0
limit_low = -10**300
limit_high = 10**300
limit_low_result = 10**(-7)
limit_high_result = 10**10
mode = "d"
imag = "OFF"
deci = "OFF"
list_cal = ["h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "sin(", "cos(", "tan(", "asin(", "acos(", "atan(", "log(", "frac(", "GCD(", "LCM(", "(", "√(", "π", "e", "∆", "Ran#", "RanInt#(", "abs(", chr(1200)]
list_num = ["0", "1", "2", "3", "4", "5", "6", "7" ,"8", "9", ".", ")", "∆", "π", "e", "h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "Ran#", chr(1200)]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "%", "h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "∆", "π", "e", chr(1200)]
power_number = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
out1_cache = ""
out2_cache = ""
expression_cache = []
cache_count = -1
calc_mode = "Normal"
min_scroll, max_scroll, select_scroll = [0], [3], 0
address_select = []
select_item = []
Catalog_select = [
["Scientific Constant",
[["Math", ["π", "e", "i", "φ"]], ["Universal", ["h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ"]],
["Electromagnetic", ["μɴ", "μʙ", "Cₑ", "Φ₀", "G₀", "Kᴊ", "Rᴋ"]],
["Atomic & Nuclear", ["mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ"]],
["Physico - Chem", ["u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ"]],
["Adopted Values", ["g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀"]],
["Other", ["t"]]]],

["Unit Conversions",
[["Length", ["in▶cm", "cm▶in", "ft▶m", "m▶ft", "yd▶m", "m▶yd", "mile▶km", "km▶mile", "n mile▶m", "m▶n mile", "pc▶km", "km▶pc"]],
["Area", ["acre▶m²", "m²▶acre"]],
["Volume", ["gal(US)▶L", "L▶gal(US)", "gal(UK)▶L", "L▶gal(UK)"]],
["Mass", ["oz▶g", "g▶oz", "lb▶kg", "kg▶lb"]],
["Velocity", ["km/h▶m/s", "m/s▶km/h"]],
["Pressure", ["atm▶Pa", "Pa▶atm", "mmHg▶Pa", "Pa▶mmHg", "kgf/cm²▶Pa", "Pa▶kgf/cm²", "lbf/in²▶kPa", "kPa▶lbf/in²"]],["Energy", ["kgf•m▶J", "J▶kgf•m", "J▶cal₁₅", "cal₁₅▶J"]],
["Power", ["hp▶kW", "kW▶hp"]],
["Temperature", ["°F▶°C", "°C▶°F"]]]],

["Probability",
["%", "!", "Ran#", "RanInt#("]],

["Numerical Calculation",
["GCD(", "LCM(", "abs("]],

["Hyperbolic/Trigonometric",
["sinh(", "cosh(", "tanh(", "asinh(", "acosh(", "atanh(", "sin(", "cos(", "tan(", "asin(", "acos(", "atan("]]]

name_conversions = [
["in▶cm", "(", "*2.54)"],
["cm▶in", "(", "/2.54)"],
["ft▶m", "(", "*0.3048)"],
["m▶ft", "(", "/0.3048)"],
["yd▶m", "(", "*0.9144)"],
["m▶yd", "(", "/0.9144)"],
["mile▶km", "(", "*1.60934)"],
["km▶mile", "(", "/1.60934)"],
["n mile▶m", "(", "*1852)"],
["m▶n mile", "(", "/1852)"],
["pc▶km", "(", "*30856778570831.27)"],
["km▶pc", "(", "/30856778570831.27)"],
["acre▶m²", "(", "*4046.873)"],
["m²▶acre", "(", "/4046.873)"],
["gal(US)▶L", "(", "*3.785411784)"],
["L▶gal(US)", "(", "/3.785411784)"],
["gal(UK)▶L", "(", "*4.54609)"],
["L▶gal(UK)", "(", "/4.54609)"],
["oz▶g", "(", "*28.3495231)"],
["g▶oz", "(", "/28.3495231)"],
["lb▶kg", "(", "*0.45359237)"],
["kg▶lb", "(", "/0.45359237)"],
["km/h▶m/s", "(", "/3.6)"],
["m/s▶km/h", "(", "*3.6)"],
["atm▶Pa", "(", "*101325)"],
["Pa▶atm", "(", "/101325)"],
["mmHg▶Pa", "(", "*133.322387415)"],
["Pa▶mmHg", "(", "/133.322387415)"],
["kgf/cm²▶Pa", "(", "*9.8066520482)"],
["Pa▶kgf/cm²", "(", "/9,8066520482)"],
["lbf/in²▶kPa", "(", "*6.89475729)"],
["kPa▶lbf/in²", "(", "/6.89475729)"],
["kgf•m▶J", "(", "*9.80665)"],
["J▶kgf•m", "(", "/9.80665)"],
["J▶cal₁₅", "(", "*0.2389029576)"],
["cal₁₅▶J", "(", "/0.2389029576)"],
["hp▶kW", "(", "*0.745699872)"],
["kW▶hp", "(", "/0.745699872)"],
["°F▶°C", "((", "-32)*5/9)"],
["°C▶°F", "((", "*9/5)+32)"]
]

#Task processing variable

i = sqrt(-1)
φ = 1.6180339887
h = 6.62607015*10**(-34)
ħ = 1.0545718*10**(-34)
c0 = 299792458
ε0 = 8.854187817*10**(-12)
μ0 = 1.2566370614*10**(-6)
Z0 = 376.730313461
G = 6.67408*10**(-11)
lₚ = 1.616229*10**(-35)
tₚ = 5.39116*10**(-44)
μɴ = 5.050783699*10**(-27)
μʙ = 9.274009994*10**(-24)
Cₑ = 1.6021766208*10**(-19)
Φ0 = 2.067833831*10**(-15)
G0 = 7.7480917310**10**(-5)
Kᴊ = 483597.8525*10**9
Rᴋ = 25812.8074555
mₚ = 1.672621898*10**(-27)
mₙ = 1.674927471*10**(-27)
mₑ = 9.10938356*10**(-31)
mμ = 1.883531594*10**(-28)
a0 = 0.52917721067*10**(-10)
α = 7.2973525664*10**(-3)
rₑ = 2.8179403227*10**(-15)
λc = 2.4263102367*10**(-12)
γₚ = 2.675221900*10**8
λcₚ = 1.32140985396*10**(-15)
λcₙ = 1.31959090481*10**(-15)
Rinf = 10973731.568508
μₚ = 1.4106067873*10**(-26)
μₑ = -928.4764620*10**(-26)
μₙ = -0.96623650*10**(-26)
μμ = -4.49044826*10**(-26)
mτ = 3.16747*10**(-27)
u = 1.660539040*10**(-27)
F = 96485.33289
Nᴀ = 6.022140857*10**23
k = 1.38064852*10**(-23)
Vₘ = 22.710947*10**(-3)
R = 8.3144598
c1 = 3.741771790*10**(-16)
c2 = 1.43877736*10**(-2)
σ = 5.670367*10**(-8)
g = 9.80665
atm = 101325
Rₖ_90 = 25812.807
Kᴊ_90 = 483597.9*10**9
t = 273.15

def output_exp(output):
	output = str(output)
	output = output.replace("**", "^")
	output = output.replace("*", "×")
	output = output.replace("pi", "π")
	output = output.replace("e+", "×10^")
	output = output.replace("E", "e")
	output = output.replace("I", "i")
	output = output.replace("sqrt", "√")
	output = r.sub(r"exp\((.*?)\)", r"e^\1", output)
	return output

def solve_exp(real_exp):
	real_exp = str(real_exp)
	real_exp = real_exp.replace("∆", "(" + str(ans) +")")
	real_exp = real_exp.replace("×", "*")
	real_exp = real_exp.replace("÷", "/")
	real_exp = real_exp.replace("√", "sqrt")
	real_exp = real_exp.replace("^", "**")
	real_exp = real_exp.replace("%", "/100")
	real_exp = real_exp.replace("#", "")
	real_exp = real_exp.replace("π", "pi")
	real_exp = real_exp.replace("e", "E")
	real_exp = real_exp.replace("₀", "0")
	real_exp = real_exp.replace("₁", "1")
	real_exp = real_exp.replace("₂", "2")
	real_exp = real_exp.replace("₉", "9")
	real_exp = real_exp.replace("∞", "inf")
	real_exp = real_exp.replace(str(chr(1200)), "I")
	return real_exp

def scr_exp(exp_input):
	exp_output = ""
	for i in exp_input:
		if i == chr(1200):
			exp_output += "i"
		else:
			exp_output += i
	return exp_output
	
def bar_up():
	
	global cache_count, expression, enter_eq, select_scroll
	
	if calc_mode == "Catalog":
		
		select_scroll -= 1
		out1.config(text = scroll(select(Catalog_select, address_select)))
	
		return None
	
	if calc_mode == "Check":
		
		try:
			webbrowser.open(url_help)
		
		except:
			pass
		
		return None
	
	button_prime_number_analysis.config(state = "disable")
	
	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	elif expression_cache == []:
		return None
	
	elif ("|" in expression) and (expression != ["|"]):
		return None
	
	else:
		
		try:
			if expression_cache[-1][1] == None:
				copy_expression_cache = expression_cache[0 : -1]
			else:
				copy_expression_cache = expression_cache
		except:
			pass
			
		if cache_count == 0:
				cache_count = len(copy_expression_cache)
	
		if "|" not in expression:
			if cache_count > 1:
				cache_count -= 1
		
		try:
				
			expression = copy_expression_cache[cache_count - 1][0]
			out1.config(text = scr_exp(expression))
			out2.config(text = f"= {copy_expression_cache[cache_count - 1][1]}")
			enter_eq = 0
			up_down_cache()
		
		except:
			pass

def bar_down():
	
	global cache_count, expression, enter_eq, select_scroll, calc_mode, language
	
	if calc_mode == "Catalog":
		
		select_scroll += 1
		out1.config(text = scroll(select(Catalog_select, address_select)))
	
		return None
	
	if calc_mode == "Check":
		
		if choose_language.index(language) == len(choose_language) - 1:
			language = choose_language[0]
		
		else:
			language = choose_language[choose_language.index(language) + 1]
			
		calc_mode = ""
		check()
		change_language()
		
		return None
	
	button_prime_number_analysis.config(state = "disable")
	
	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	elif expression_cache == []:
		return None
	
	elif ("|" in expression) and (expression != ["|"]):
		return None
	
	elif ("|" not in expression) or (expression == ["|"]):
		try:
			if expression_cache[-1][1] == None:
				copy_expression_cache = expression_cache[0 : -1]
			else:
				copy_expression_cache = expression_cache
		except:
			pass
		if cache_count == 0:
			cache_count = len(copy_expression_cache)
		if cache_count < len(copy_expression_cache):
			cache_count += 1
		else:
			pass
		
		try:
			
			expression = copy_expression_cache[cache_count - 1][0]
			out1.config(text = scr_exp(expression))
			out2.config(text = f"= {copy_expression_cache[cache_count - 1][1]}")
			enter_eq = 0
			up_down_cache()
		
		except:
			pass
		
def bar_left():
	
	global expression, enter_eq, cache_count, expression_cache, address_select, select_scroll
	
	if calc_mode == "Catalog":
		if address_select != []:
			select_scroll = address_select[-1]
			del address_select[-1], min_scroll[-1], max_scroll[-1]
			out1.config(text = scroll(select(Catalog_select, address_select)))
		
		return None
	
	if calc_mode == "Check":
		return None
	
	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	elif enter_eq == 0:
		if expression == ["|"]:
			if expression_cache != []:
				expression = expression_cache[-1][0] + ["|"]
				out1.config(text = scr_exp(expression))
				out2.config(text = "")
				return None
			else:
				return None
		else:
			if "|" in expression:
				if expression[0] == "|":
					del expression[0]
					expression += ["|"]
				else:
					k = expression.index("|")
					expression[k - 1], expression[k] = expression[k], expression[k - 1]
			else:
				expression += ["|"]
					
	else:
		if "|" not in expression:
			expression += ["|"]
			enter_eq = 0
	
	output = ""
	out2.config(text = "")
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	cache_count = 0
	up_down_cache()

def bar_right():
	
	global expression, enter_eq, cache_count, address_select, select_scroll, select_item, min_scroll, max_scroll
	
	if calc_mode == "Catalog":
		if isinstance(select_item[select_scroll], list) == True:
			address_select.append(select_scroll)
			min_scroll.append(0)
			max_scroll.append(3)
			select_scroll = 0
			out1.config(text = scroll(select(Catalog_select, address_select)))
		
		return None
	
	if calc_mode == "Check":
		return None
	
	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	elif enter_eq == 0:
		if expression == ["|"]:
			try:
				expression = ["|"] + expression_cache[-1][0]
				out1.config(text = scr_exp(expression))
				if expression_cache[-1][1] != None:
					out2.config(text = "")
				else:
					out2.config(text = "")
				return None
			except:
				pass
		else:
			if "|" in expression:
				if expression[-1] == "|":
					del expression[-1]
					expression = ["|"] + expression
				else:
					k = expression.index("|")
					expression[k + 1], expression[k] = expression[k], expression[k + 1]
			else:
				expression = ["|"] + expression
			
	else:
		if "|" not in expression:
			expression = ["|"] + expression
			enter_eq = 0
	
	output = ""
	out2.config(text = output)
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	cache_count = 0
	up_down_cache()

def bar_add(var):
	global expression, cache_count
	
	if var == "i":
		var = chr(1200)
		
	try:
		k = expression.index("|")
		expression = list(expression[: k]) + [var] + list(expression[k :])
		if ("(" in var) and (var != "("):
			del expression[k + 1]
			expression = list(expression[: k + 1]) + ["|", ")"] + list(expression[k + 1 :])
	except:
		expression = [var, "|"]
	cache_count = 0
	up_down_cache()

def bar_del():
	global expression
	
	if calc_mode == "Check":
		return None
	
	if expression == ["|"]:
		pass
	else:
		if "|" in expression:
			k = expression.index("|")
			if k == 0:
				del expression[1]
			else:
				del expression[k - 1]
		else:
			pass
	out1.config(text = scr_exp(expression))
	cache_count = 0
	up_down_cache()

def add(var):
	global expression, enter_eq
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Check":
		return None
	
	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	elif "|" in expression:
		if enter_eq != 0:
			expression = ["|"]
			enter_eq = 0
		
		if var == "i":
			bar_add(chr(1200))
		
		else:
			bar_add(var)
			
		out1.config(text = scr_exp(expression))
		
	else:

		expression = ["|"]
		output = ""
		out1.config(text = "|")
		out2.config(text = output)
		button_prime_number_analysis.config(state = "disable")

		if (var == "×") or (var == "÷") or (var == "+") or (var == "-") or (var == "^"):
			if enter_eq != 0:
				bar_add("∆")
		bar_add(var)
		out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	
	enter_eq = 0


def change_language():
	
	global language, Catalog_select
	
	if language == "English":
		
		Catalog_select[0][0] = "Scientific Constant"
		Catalog_select[0][1][0][0] = "Math"
		Catalog_select[0][1][1][0] = "Universal"
		Catalog_select[0][1][2][0] = "Electromagnetic"
		Catalog_select[0][1][3][0] = "Atomic & Nuclear"
		Catalog_select[0][1][4][0] = "Physico - Chem"
		Catalog_select[0][1][5][0] = "Adopted Values"
		Catalog_select[0][1][6][0] = "Other"
		Catalog_select[1][0] = "Unit Conversions"
		Catalog_select[1][1][0][0] = "Length"
		Catalog_select[1][1][1][0] = "Area"
		Catalog_select[1][1][2][0] = "Volume"
		Catalog_select[1][1][3][0] = "Mass"
		Catalog_select[1][1][4][0] = "Velocity"
		Catalog_select[1][1][5][0] = "Pressure"
		Catalog_select[1][1][6][0] = "Energy"
		Catalog_select[1][1][7][0] = "Power"
		Catalog_select[1][1][8][0] = "Temperature"
		Catalog_select[2][0] = "Probability"
		Catalog_select[3][0] = "Numerical Calculation"
		Catalog_select[4][0] = "Hyperbolic/Trigonometric"


	elif language == "Vietnamese":
		
		Catalog_select[0][0] = "Hằng số khoa học"
		Catalog_select[0][1][0][0] = "Hằng số toán học"
		Catalog_select[0][1][1][0] = "Hằng số chung"
		Catalog_select[0][1][2][0] = "Hằng số điện từ"
		Catalog_select[0][1][3][0] = "Hằng số nguyên tử & Hạt nhân"
		Catalog_select[0][1][4][0] = "Hằng số Lý - Hóa"
		Catalog_select[0][1][5][0] = "Giá trị thông qua"
		Catalog_select[0][1][6][0] = "Khác"
		Catalog_select[1][0] = "Chuyển đổi đơn vị"
		Catalog_select[1][1][0][0] = "Độ dài"
		Catalog_select[1][1][1] [0] = "Diện tích"
		Catalog_select[1][1][2][0] = "Thể tích"
		Catalog_select[1][1][3] [0] = "Khối lượng"
		Catalog_select[1][1][4] [0] = "Vận tốc"
		Catalog_select[1][1][5][0] = "Áp suất"
		Catalog_select[1][1][6][0] = "Năng lượng"
		Catalog_select[1][1][7][0] = "Công suất"
		Catalog_select[1][1][8] [0] = "Nhiệt độ"
		Catalog_select[2][0] = "Xác suất"
		Catalog_select[3][0] = "Phép tính số"
		Catalog_select[4][0] = "Hyperbol/Lượng giác"
	
	
	elif language == "Chinese":
		
		Catalog_select[0][0] = "科学常数"
		Catalog_select[0][1][0][0] = "数学常数"
		Catalog_select[0][1][1][0] = "通用常量"
		Catalog_select[0][1][2][0] = "电磁常数"
		Catalog_select[0][1][3][0] = "原子和核常数"
		Catalog_select[0][1][4][0] = "物理 - 化学常数"
		Catalog_select[0][1][5][0] = "传递的值"
		Catalog_select[0][1][6][0] = "其他"
		Catalog_select[1][0] = "单位换算"
		Catalog_select[1][1][0][0] = "长度"
		Catalog_select[1][1][1] [0] = "区域"
		Catalog_select[1][1][2][0] = "体积"
		Catalog_select[1][1][3] [0] = "音量"
		Catalog_select[1][1][4] [0] = "速度"
		Catalog_select[1][1][5][0] = "压力"
		Catalog_select[1][1][6][0] = "能源"
		Catalog_select[1][1][7][0] = "容量"
		Catalog_select[1][1][8] [0] = "温度"
		Catalog_select[2][0] = "概率"
		Catalog_select[3][0] = "数值计算"
		Catalog_select[4][0] = "双曲/三角"
	
	
	elif language == "Japanese":
		
		Catalog_select[0][0] = "科学定数"
		Catalog_select[0][1][0][0] = "数学定数"
		Catalog_select[0][1][1][0] = "一般定数"
		Catalog_select[0][1][2][0] = "電磁定数"
		Catalog_select[0][1][3][0] = "原子および核定数"
		Catalog_select[0][1][4][0] = "物理定数 - 化学定数"
		Catalog_select[0][1][5][0] = "渡された値"
		Catalog_select[0][1][6][0] = "その他"
		Catalog_select[1][0] = "単位換算"
		Catalog_select[1][1][0][0] = "長さ"
		Catalog_select[1][1][1] [0] = "エリア"
		Catalog_select[1][1][2][0] = "ボリューム"
		Catalog_select[1][1][3] [0] = "ボリューム"
		Catalog_select[1][1][4] [0] = "速度"
		Catalog_select[1][1][5][0] = "圧力"
		Catalog_select[1][1][6][0] = "エネルギー"
		Catalog_select[1][1][7][0] = "容量"
		Catalog_select[1][1][8] [0] = "温度"
		Catalog_select[2][0] = "確率"
		Catalog_select[3][0] = "数値計算"
		Catalog_select[4][0] = "双曲線/三角関数"
		


def up_down_cache():
	
	if expression_cache == []:
		up_cache.config(fg = "black")
		down_cache.config(fg = "black")
	
	elif len(expression_cache) == 1:
		up_cache.config(fg = "white")
		down_cache.config(fg = "black")
	
	elif len(expression_cache) > 1:
		if expression_cache[-1][1] == None:
			max = len(expression_cache) - 1
		else:
			max = len(expression_cache)
		if cache_count == 1:
			down_cache.config(fg = "white")
			up_cache.config(fg = "black")
		elif (cache_count == max) or (cache_count == 0):
			up_cache.config(fg = "white")
			down_cache.config(fg = "black")
		else:
			up_cache.config(fg = "white")
			down_cache.config(fg = "white")
	
def delete():
	global expression
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Check":
		return None
	
	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	elif calc_mode == "Reset":
		return None
		
	bar_del()
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	
def init_key():
	
	global key
	
	characters = string.ascii_letters + string.digits
	string_key = "".join(random.choice(characters) for _ in range(16))
	
	for i in range(16):
		key += string_key[i]
		
		if (i % 4 == 3) and (i != 15):
			key += " - "
	
def ac():
	global expression, enter_eq, cache_count, expression_cache, calc_mode, out1_cache, out2_cache, min_scroll, max_scroll, select_scroll, address_select, select_item
	
	if calc_mode == "Catalog":
		
		out1.config(text = out1_cache)
		out2.config(text = out2_cache)
		
		out1_cache = ""
		out2_cache = ""
		
		calc_mode = "Normal"
		min_scroll, max_scroll, select_scroll = [0], [3], 0
		address_select = []
		select_item = []
		
		calc_mode = "Normal"
		
		up_down_cache()
		
		return None
	
	if calc_mode == "Check":
		return None
	
	text = out1.cget("text")
	
	if calc_mode == "Reset":
		out1.config(text = out1_cache)
		out2.config(text = out2_cache)
		PNA_button()
		up_down_cache()
		calc_mode == "Normal"
		
	else:
		
		expression = ["|"]
		output = ""
		out1.config(text = "|")
		out2.config(text = "")
		button_prime_number_analysis.config(state = "disable")
		enter_eq = 0
		cache_count = 0
		up_down_cache()
		if expression_cache != []:
			if "|" in expression_cache[-1][0]:
				del expression_cache[-1][0][expression_cache[-1][0].index("|")]
		
		if calc_mode == "Error":
			calc_mode = "Normal"

def on():
	
	global expression, expression_cache, cache_count, enter_eq, calc_mode, min_scroll, max_scroll, select_scroll, address_select, select_item
	
	expression = ["|"]
	expression_cache = []
	out1.config(text = "|")
	out2.config(text = "")
	cache_count = -1
	button_prime_number_analysis.config(state = "disable")
	enter_eq = 0
	up_down_cache()
	calc_mode = "Normal"
	min_scroll, max_scroll, select_scroll = [0], [3], 0
	address_select = []
	select_item = []
	
def error_message():
	
	global calc_mode
	
	calc_mode = "Error"
	
	if language == "English":
		out1.config(text = "Math ERROR")
		out2.config(text = "Return: [OK] or [=]")
	
	elif language == "Vietnamese":
		out1.config(text = "LỖI toán học")
		out2.config(text = "Trở lại: [OK] hoặc [=]")
	
	elif language == "Chinese":
		out1.config(text = "数学错误")
		out2.config(text = "返回: [OK]或者[=]")
	
	elif language == "Japanese":
		out1.config(text = "数学エラー")
		out2.config(text = "戻る： [OK]または[=]")
		
	cache_count = 0
	up_down_cache()

def check_result(result):
	real, imag = result.as_real_imag()
	if limit_low <= real <= limit_high:
		if limit_low <= imag <= limit_high:
			return True
	else:
		return False

def MB10(input_result, limit_low, limit_high):
	
	result = eval(str(N(input_result)))
	
	if result == 0:
		return "0"
	
	result += 0*I
	power = 0
	sign = ""
	
	if result.as_real_imag()[1] == 0:
		
		result = float(result.as_real_imag()[0])
	
		if result < 0:
			sign = "-"
			result *= -1
		
		if abs(result) >= limit_high:
			while result >= 10:
				result /= 10
				power += 1
			
			return f"{sign}{round(result, 9)}×10^{power}"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
		
			return f"{sign}{round(result, 9)}×10^{power}"
		
		else:
			return str(input_result)
	
	elif result.as_real_imag()[0] == 0:
		
		result = float(result.as_real_imag()[1])
	
		if result < 0:
			sign = "-"
			result *= -1
		
		if abs(result) >= limit_high:
			while result >= 10:
				result /= 10
				power += 1
			
			return f"{sign}{round(result, 9)}×10^{power}*I"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
		
			return f"{sign}{round(result, 9)}×10^{power}*I"
		
		else:
			return f"{result}*I"
	
	else:
		
		result_real = float(result.as_real_imag()[0])
		result_imag = float(result.as_real_imag()[1])
		power_real = 0
		power_imag = 0
		output_result = ""
		
		if result_real < 0:
			sign = "-"
			result *= -1
		
		if abs(result_real) >= limit_high:
			while result_real >= 10:
				result_real /= 10
				power_real += 1
			
			output_result = f"{sign}{round(result_real, 9)}×10^{power_real}"
		
		elif abs(result_real) < limit_low:
			while result_real < 1:
				result_real *= 10
				power_real -= 1
		
			output_result = f"{sign}{round(result_real, 9)}×10^{power_real}"
		
		else:
			output_result = str(result_real)
		
		if result_imag < 0:
			sign = "-"
			result *= -1
		
		else:
			sign = "+"
		
		if abs(result_imag) >= limit_high:
			while result_imag >= 10:
				result_imag /= 10
				power_imag += 1
			
			output_result += f"{sign}{round(result_imag, 9)}×10^{power_imag}*I"
		
		elif abs(result_imag) < limit_low:
			while result_imag < 1:
				result_imag *= 10
				power_imag -= 1
		
			output_result += f"{sign}{round(result_imag, 9)}×10^{power_imag}*I"
		
		else:
			output_result += f"{sign}{result_imag}*I"
		
		return output_result

def GCD(a, b):
	if a % 1 != 0:
		return 0/0
	if b % 1 != 0:
		return 0/0
	while b != 0:
		a, b = b, a % b
	return a

def LCM(a, b):
	if a % 1 != 0:
		return 0/0
	if b % 1 != 0:
		return 0/0
	return (a * b) / GCD(a, b)

def frac(n):
	return factorial(n)

def RanInt(a, b):
	return random.randint(a, b)

def PNA_button():
	
	if calc_mode == "Catalog":
		button_prime_number_analysis.config(state = "disable")
		return None
		
	if calc_mode == "Check":
		button_prime_number_analysis.config(state = "disable")
		return None
		
	if calc_mode == "Error":
		button_prime_number_analysis.config(state = "disable")
		return None
	
	output = out2.cget("text")
	if (output == "") or (calc_mode == "Reset"):
		button_prime_number_analysis.config(state = "disable")
	else:
		output = output.replace("=", "")
		output = output.replace(" ", "")
		output = solve_exp(output)
		result = N(output)
		if result.is_complex == False:
			button_prime_number_analysis.config(state = "disable")
		elif result % 1 != 0:
			button_prime_number_analysis.config(state = "disable")
		elif result <= 1:
			button_prime_number_analysis.config(state = "disable")
		else:
			button_prime_number_analysis.config(state = "normal")

def PNA():
	output = out2["text"]

	for i in output:
		if i in power_number:
			return None
	output = output.replace("=", "")
	output = output.replace(" ", "")
	output = solve_exp(output)
	output = N(output)
	output = int(output)
	output = factorint(output)
	output = str(output)
	output = output.replace(" ", "")
	output = output.replace("{", "")
	output = output.replace("}", "")
	output = output.split(",")
	text = []
	for i in output:
		i = i.split(":")
		n = ""
		if i[1] != "1":
			for j in i[1]:
				j = str(j)
				k = number.index(j)
				n += power_number[k]
			text.append(str(i[0]) + n)
		else:
			text.append(str(i[0]))
	output = text
	output= " × ".join(output)
	out2.config(text = "= " + output)

def check():
	
	global calc_mode, out1_cache, out2_cache
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Check":
		
		out1.config(text = out1_cache)
		out2.config(text = out2_cache)
		
		up_down_cache()
		
		calc_mode = "Normal"
	
		return None
	
	if calc_mode == "Error":
		return None
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")
	
	if calc_mode != "":
		out1_cache = out1.cget("text")
		out2_cache = out2.cget("text")
	
	calc_mode = "Check"
	
	if language == "English":
		text = f"Version: {version_of_calc}\n"
	
	elif language == "Vietnamese":
		text = f"Phiên bản: {version_of_calc}\n"
	
	elif language == "Chinese":
		text = f"版本: {version_of_calc}\n"
	
	elif language == "Japanese":
		text = f"バージョン: {version_of_calc}\n"
	
	button_prime_number_analysis.config(state = "disable")
	
	name_of_data = ["B", "KB", "MB"]
	
	all_of_code = expression, output, ans, enter_eq, mode, imag, deci, out1_cache, out2_cache, expression_cache, cache_count, calc_mode, min_scroll, max_scroll, select_scroll, address_select, select_item, key
	
	all_of_code = str(all_of_code)
	data_of_code = sys.getsizeof(all_of_code)
	
	data_div = 0
	data_of_code_div = data_of_code
	
	while data_of_code_div > 1024:
		data_of_code_div /= 1024
		data_div += 1
	
	if language == "English":
		text += f"Data used: {data_of_code} Bytes"
	
	elif language == "Vietnamese":
		text += f"Dữ liệu đã sử dụng: {data_of_code} Bytes"
	
	elif language == "Chinese":
		text += f"使用的数据: {data_of_code} Bytes"
	
	elif language == "Japanese":
		text += f"使用されたデータ: {data_of_code} Bytes"
	
	if data_div != 0:
		text += f" ({round(data_of_code_div, 1)} {name_of_data[data_div]})"
	
	if language == "English":
		text += f"\nYour key: {key}"
		text += f"\nYour language: English"
		text_out = "Click [Check] again to exit\n"
		text_out += "Need help?  Press [˄] - Change language press [˅]"
	
	elif language == "Vietnamese":
		text += f"\nChìa khóa của bạn: {key}"
		text += f"\nNgôn ngữ của bạn: Tiếng Việt"
		text_out = "Bấm vào [Check] lần nữa để thoát\n"
		text_out += "Cần giúp đỡ?  Nhấn [˄] - Thay đổi ngôn ngữ nhấn [˅]"
	
	elif language == "Chinese":
		text += f"\n你的钥匙: {key}"
		text += f"\n您的语言： 中文"
		text_out = "再次点击[Check]退出\n"
		text_out += "需要帮助？按 [˄] - 更改语言按 [˅]"
	
	elif language == "Japanese":
		text += f"\nあなたの鍵: {key}"
		text += f"\nあなたの言語: 日本語"
		text_out = "終了するにはもう一度[Check]をクリックします\n"
		text_out += "お困りですか？[˄] - 言語変更は[˅]"
	
	out1.config(text = text)
	out2.config(text = text_out)
	return None

def sinh(a):
	return m.sinh(a)
		
def cosh(a):
	return m.cosh(a)
		
def tanh(a):
	return m.tanh(a)
		
def asinh(a):
	return m.asinh(a)
		
def acosh(a):
	return m.acosh(a)
		
def atanh(a):
	return m.atanh(a)	

def sin(a):
	global mode
	if mode == "r":
		return m.sin(a)
	if mode == "d":
		return m.sin(m.radians(a))
		
def cos(a):
	global mode
	if mode == "r":
		return m.cos(a)
	if mode == "d":
		return m.cos(m.radians(a))
		
def tan(a):
	global mode
	if mode == "r":
		return m.tan(a)
	if mode == "d":
		return m.tan(m.radians(a))
		
def asin(a):
	global mode
	if mode == "r":
		return m.asin(a)
	if mode == "d":
		return m.degrees(m.asin(a))
		
def acos(a):
	global mode
	if mode == "r":
		return m.acos(a)
	if mode == "d":
		return m.degrees(m.acos(a))
		
def atan(a):
	global mode
	if mode == "r":
		return m.atan(a)
	if mode == "d":
		return m.degrees(m.atan(a))
		
def mode_degree(degree):
	global mode
	if degree == "d":
		button_d_mode.config(state = "disabled")
		button_r_mode.config(state = "normal")
		mode = "d"
	if degree == "r":
		button_r_mode.config(state = "disabled")
		button_d_mode.config(state = "normal")
		mode = "r"
	
def on_imag_num():
	global imag
	button_ON_imagnum_mode.config(state = "disabled")
	button_OFF_imagnum_mode.config(state = "normal")
	imag = "ON"
	
def off_imag_num():
	global imag
	button_OFF_imagnum_mode.config(state = "disabled")
	button_ON_imagnum_mode.config(state = "normal")
	imag = "OFF"

def on_deci_num():
	global deci
	button_ON_decimal_mode.config(state = "disabled")
	button_OFF_decimal_mode.config(state = "normal")
	deci = "ON"
	
def off_deci_num():
	global deci
	button_OFF_decimal_mode.config(state = "disabled")
	button_ON_decimal_mode.config(state = "normal")
	deci = "OFF"

def end_left():
	global expression
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Check":
		return None

	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	try:
		k = expression.index("|")
		del expression[k]
		expression = ["|"] + expression
	except:
		pass
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")

def end_right():
	global expression
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Check":
		return None
	
	text = out1.cget("text")
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	try:
		k = expression.index("|")
		del expression[k]
		expression += ["|"]
	except:
		pass
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	
def reset_message():
	global out1_cache, out2_cache, calc_mode
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Error":
		return None
	
	if calc_mode != "Reset":
		out1_cache = out1.cget("text")
		out2_cache = out2.cget("text")
		
	calc_mode = "Reset"

	button_prime_number_analysis.config(state = "disable")

	if language == "English":
		out1.config(text = "Are you sure you want to reset?")
		out2.config(text = "Yes: [OK] or [=]\nNo: [AC]")
		
	elif language == "Vietnamese":
		out1.config(text = "Bạn có chắc chắn muốn đặt lại?")
		out2.config(text = "Có: [OK] hoặc [=]\nKhông: [AC]")
	
	elif language == "Chinese":
		out1.config(text = "您确定要重置吗？")
		out2.config(text = "可: [OK] 或者 [=]\n不: [AC]")
	
	elif language == "Japanese":
		out1.config(text = "本当にリセットしますか?")
		out2.config(text = "コ: [OK] または [=]\nいいえ: [AC]")
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")

def reset():
	global expression, output, ans, enter_eq, mode, imag, deci, out1_cache, out2_cache, expression_cache, cache_count, calc_mode, min_scroll, max_scroll, select_scroll, address_select, select_item
	
	expression = ["|"]
	output = ""
	ans = 0
	enter_eq = 0
	mode = "d"
	imag = "OFF"
	deci = "OFF"
	out1.config(text = scr_exp(expression))
	out2.config(text = "")
	button_Ans.config(text = "∆ = 0")
	mode_degree("d")
	off_imag_num()
	off_deci_num()
	button_prime_number_analysis.config(state = "disable")
	out1_cache = ""
	out2_cache = ""
	expression_cache = []
	cache_count = -1
	up_down_cache()
	calc_mode = "Normal"
	min_scroll, max_scroll, select_scroll = [0], [3], 0
	address_select = []
	select_item = []

def off_calc():
	return None

def off_calc_1():
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")
	
	for widget in app.winfo_children():
		if isinstance(widget, tk.Button):
			widget.config(command = lambda: off_calc())
	
	out1.config(text = "KERAS", anchor = "center", font = ("", 20))
	out2.config(text = version_of_calc, anchor = "center", font = ("", 7))
	
	app.after(2000, off_calc_2)

def off_calc_2():
	
	out1.config(text = "Power Calculator")
	out2.config(text = "Made by Lê Ngọc Hà")
	
	app.after(2300, off_calc_3)

def off_calc_3():
	
	app.destroy()

def select(A, pos):
	
	global calc_mode, min_scroll, max_scroll, select_scroll, select_item
	
	for i in pos:
		if isinstance(A[i], list) == True:
			A = A[i][1]
		else:
			try:
				A = A[i]
			except:
				pass
	
	select_item = A
	text = []
	
	if isinstance(A, list) == True:
		
		if pos == []:
			for i in range(len(A)):
				text.append(f"{i + 1}. {A[i][0]}")
				
		else:
			for i in range(len(A)):
				if isinstance(A[i], list) == True:
					text.append(f"{i + 1}. {A[i][0]}")
				else:
					text.append(f"{i + 1}. {A[i]}")
	
	else:
	
		return None
	
	return text

def scroll(list):
	
	global min_scroll, max_scroll, select_scroll
	
	length_select = len(list)
	
	if select_scroll == length_select:
		if length_select <= 4:
			min_scroll[-1], max_scroll[-1], select_scroll = 0, length_select - 1, 0
		else:
			min_scroll[-1], max_scroll[-1], select_scroll = 0, 3, 0
	
	elif select_scroll == -1:
		if length_select <= 4:
			min_scroll[-1] = 0
		else:
			min_scroll[-1] = length_select - 4
		max_scroll[-1], select_scroll = length_select - 1, length_select - 1
		
	elif select_scroll < min_scroll[-1]:
		min_scroll[-1] -= 1
		max_scroll[-1] -= 1
	
	elif select_scroll > max_scroll[-1]:
		min_scroll[-1] += 1
		max_scroll[-1] += 1
		
	text = ""
	if length_select > 4:
		length_select = 4
	for i in range(0, length_select):
		if text != "":
			text += "\n"
		if i + (min_scroll[-1] - select_scroll) == 0:
			text += f"▶{list[min_scroll[-1] + i]}"
		else:
			text += f"    {list[min_scroll[-1] + i]}"

	return text

def catalog():
	
	global calc_mode, out1_cache, out2_cache
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Error":
		return None
		
	calc_mode = "Catalog"
	
	out1_cache = out1.cget("text")
	out2_cache = out2.cget("text")
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")
	
	out1.config(text = scroll(select(Catalog_select, address_select)))
	
	if language == "English":
		out2.config(text = "Scroll: [^] or [˅]\nSelect: [OK] or [=]")
	
	elif language == "Vietnamese":
		out2.config(text = "Cuộn: [^] hoặc [˅]\nChọn: [OK] hoặc [=]")
	
	elif language == "Chinese":
		out2.config(text = "滚动：[^] 或 [˅]\n选择：[OK] 或 [=]")
	
	elif language == "Japanese":
		out2.config(text = "スクロール: [^] または [˅]\n選択: [OK] または [=]")


def change_exp(real_exp):
	
	if "%" in real_exp:
			 
		time_parentheses = 0
			 
		for i in range(len(real_exp)):
			if real_exp[i + 2 * time_parentheses] == "%":
				try:
					if real_exp[i + 1 + 2 * time_parentheses] != ")":
							
						parentheses = 0
						change_parentheses = False
						exit = False
							
						for j in range(i - 1 + 2 * time_parentheses, -1, -1):
								
							if exit == True:
								continue
								
							if real_exp[j] == ")":
								parentheses += 1
								change_parentheses = True
									
							if real_exp[j] == "(":
								parentheses -= 1
								change_parentheses = True
								
							if (parentheses == 0) and (change_parentheses == True):
								real_exp = real_exp[: j] + "(" + real_exp[j : i + 1 + 2 * time_parentheses] + ")" + real_exp[i + 1 + 2 * time_parentheses :]
								time_parentheses += 1
								exit = True
						
				except:
						
					parentheses = 0
					change_parentheses = False
					exit = False
							
					for j in range(i - 1 + 2 * time_parentheses, -1, -1):
								
						if exit == True:
							continue
								
						if real_exp[j] == ")":
							parentheses += 1
							change_parentheses = True
									
						if real_exp[j] == "(":
							parentheses -= 1
							change_parentheses = True
								
						if (parentheses == 0) and (change_parentheses == True):
							real_exp = real_exp[: j] + "(" + real_exp[j :] + ")"
							time_parentheses += 1
							exit = True
		
		
	if "!" in real_exp:
			 
		time_frac = 0
			 
		for i in range(len(real_exp)):
			if real_exp[i + 3 * time_frac] == "!":
							
				parentheses = 0
				change_parentheses = False
				exit = False
							
				for j in range(i - 1 + 3 * time_frac, -1, -1):
								
					if exit == True:
						continue
								
					if real_exp[j] == ")":
						parentheses += 1
						change_parentheses = True
									
					if real_exp[j] == "(":
						parentheses -= 1
						change_parentheses = True
								
					if (parentheses == 0) and (change_parentheses == True):
						real_exp = real_exp[: j] + "frac" + real_exp[j : i + 3 * time_frac] + real_exp[i + 1 + 3 * time_frac :]
						time_frac += 1
						exit = True

	
	for k in range(len(name_conversions)):
	
		if name_conversions[k][0] in real_exp:
			
			real_exp = real_exp.replace(name_conversions[k][0], chr(1000 + k))
				 
			time_jump = 0
			time_skip = len(name_conversions[k][1]) + len(name_conversions[k][2])
				 
			for i in range(len(real_exp)):
				if real_exp[i + time_skip * time_jump] == chr(1000 + k):
					try:
						if real_exp[i + 1 + time_skip * time_jump] != ")":
								
							parentheses = 0
							change_parentheses = False
							exit = False
								
							for j in range(i - 1 + time_skip * time_jump, -1, -1):
									
								if exit == True:
									continue
									
								if real_exp[j] == ")":
									parentheses += 1
									change_parentheses = True
										
								if real_exp[j] == "(":
									parentheses -= 1
									change_parentheses = True
									
								if (parentheses == 0) and (change_parentheses == True):
									real_exp = real_exp[: j] + name_conversions[k][1] + real_exp[j : i + 1 + time_skip * time_jump] + name_conversions[k][2] + real_exp[i + 1 + time_skip * time_jump :]
									time_jump += 1
									exit = True
							
					except:
							
						parentheses = 0
						change_parentheses = False
						exit = False
								
						for j in range(i - 1 + time_skip * time_jump, -1, -1):
									
							if exit == True:
								continue
									
							if real_exp[j] == ")":
								parentheses += 1
								change_parentheses = True
										
							if real_exp[j] == "(":
								parentheses -= 1
								change_parentheses = True
									
							if (parentheses == 0) and (change_parentheses == True):
								real_exp = real_exp[: j] + name_conversions[k][1] + real_exp[j :] + name_conversions[k][2]
								time_jump += 1
								exit = True
		
			real_exp = real_exp.replace(chr(1000 + k), "")
	
	return real_exp
	
	
def solve():
	global expression, output, ans, enter_eq, list_cal, expression_cache, cache_count, select_scroll, address_select, calc_mode, select_item, min_scroll, max_scroll
	
	if calc_mode == "Catalog":
		
		address_select.append(select_scroll)
		if select(Catalog_select, address_select) == None:

			bar_add(select_item)
			calc_mode = "Normal"
			address_select = []
			out1.config(text = scr_exp(expression))
			out2.config(text = "")
			up_down_cache()
			min_scroll, max_scroll, select_scroll = [0], [3], 0
			
		else:
			min_scroll.append(0)
			max_scroll.append(3)
			select_scroll = 0
			out1.config(text = scroll(select(Catalog_select, address_select)))
	
		return None
	
	if calc_mode == "Error":
		calc_mode = "Normal"
		expression += "|"
		out1.config(text = scr_exp(expression))
		out2.config(text = "")
	
	elif calc_mode == "Reset":
		reset()
	
	elif expression == ["|"]:
		pass
	
	else:
		
		try:
			k = expression.index("|")
			del expression[k]
		except:
			pass
		
		previous_character = None
		real_exp = []
		error = 0
		
		for i in range(len(expression)):
			if (previous_character in list_num) and (expression[i] in list_cal):
				real_exp += ["*"] + [expression[i]]
		
			elif (previous_character not in list_num) and (expression[i] == "."):
				real_exp += ["0."]
		
			else:
				real_exp += [expression[i]]
			
			previous_character = expression[i]
		
		number_handle = ""
		new_exp = ""
		real_exp += [""]
		
		for i in real_exp:
			
			if i in number:
				number_handle += i
				
			elif i == "Ran#":
				new_exp += f"({random.randint(0, 999)}/1000)"
				
			else:
				try:
					try:
						if "%" in number_handle:
							new_exp += "(" + str(int(number_handle[0 : -1])) + "%)" + i
						else:
							new_exp += "(" + str(int(number_handle)) + ")" + i
					
					except:
						if (number_handle != "%") or (number_handle != ""):
							if ("%" in number_handle) and (number_handle != "%"):
								new_exp += "(" + number_handle[0 : -1] + "%)" + i
							else:
								new_exp += number_handle + i
								
						else:
							new_exp += i
				
				except:
					
					try:
						try:
							if "%" in number_handle:
								new_exp += "(" + str(float(number_handle[0 : -1])) + "%)" + i
							else:
								new_exp += "(" + str(float(number_handle)) + ")" + i
								
						except:
							if (number_handle != "%") or (number_handle != ""):
								if ("%" in number_handle) and (number_handle != "%"):
									new_exp += "(" + number_handle[0 : -1] + "%)" + i
								else:
									new_exp += number_handle + i
							
							else:
								new_exp += i
					
					except:
						if number_handle == "":
							new_exp += i
			
				number_handle = ""
		
		real_exp = new_exp
		
		real_exp = change_exp(real_exp)
		
		real_exp = solve_exp(real_exp)
		
		if imag == "OFF":
			try:
				if deci == "OFF":
					output = eval(real_exp)
				else:
					output = N(eval(real_exp))
				if "I" in str(output):
					error += 1
			except :
				error_message()
		else:
			try:
				if deci == "OFF":
					output = eval(real_exp)
				else:
					output = N(eval(real_exp))
			except:
				error_message()
		
		try:
			check = check_result(N(eval(real_exp)))
			if check == False:
				error += 1
		except:
			error += 1
	
		if error == 0:
			output = MB10(output, limit_low_result, limit_high_result)
			ans_real = output
			output = output_exp(output)
			out2.config(text = "= " + str(output))
			ans = ans_real
			out1.config(text = scr_exp(expression))
			button_Ans.config(text = "∆ = " + output_exp(output))
			enter_eq += 1
			try:
				if expression_cache[-1][1] != None:
					pass
				else:
					del expression_cache[-1]
			except:
				pass
			expression_cache.append([expression, output])
			if len(expression_cache) > 30:
				del expression_cache[0]

		else:
			try:
				if expression_cache[-1][1] != None:
					pass
				else:
					del expression_cache[-1]
			except:
				pass
			expression_cache.append([expression, None])
			error_message()
		
		PNA_button()
	cache_count = 0
	up_down_cache()

app = tk.Tk()
app.geometry("720x1650")

calculator_screen = Frame(app)
calculator_screen.place(x = 0, y = 0, height = 240, width = 720)

up_cache = tk.Label(app, text = "↑", bg = "black", fg = "black")
up_cache.place(x = 685, y = 250, height = 35, width = 35)

down_cache = tk.Label(app, text = "↓", bg = "black", fg = "black")
down_cache.place(x = 650, y = 250, height = 35, width = 35)

out1 = tk.Label(calculator_screen, text = expression, bg = "black", fg = "white", justify = "left", anchor = "nw", wraplength = 720)
out1.place(x = 0, y = 0, height = 150, width = 720)

#----------expression input screen----------

out2 = tk.Label(calculator_screen, text = output, bg = "black", fg = "white", anchor = "e")
out2.place(x = 0, y = 150, height = 90, width = 720)

#-----------output screen----------

button_Ans = tk.Button(app, text = "∆ = 0", bg = "black", fg = "white", anchor = "w", wraplength = 330, font = ("Arial", 5), command = lambda: add("∆"))
button_Ans.place(x= 455, y = 400, height = 60, width = 275)

button_ON = tk.Button(app, text = "ON", bg = "white", command = lambda: on())
button_ON.place(x = 5, y = 245, height = 70, width = 70)

button_check = tk.Button(app, text = "Check", bg = "white", font = ("", 5), command = lambda: check())
button_check.place(x = 80, y = 245, height = 70, width = 70)

button_OFF = tk.Button(app, text = "OFF", bg = "white", command = lambda: off_calc_1())
button_OFF.place(x = 5, y = 320, height = 70, width = 70)

button_left = tk.Button(app, text = "<", bg = "white", command = lambda: bar_left())
button_left.place(x = 215, y = 320, height = 65, width = 65)

button_right = tk.Button(app, text = ">", bg = "white", command = lambda: bar_right())
button_right.place(x = 365, y = 320, height = 65, width = 65)

button_OK = tk.Button(app, text = "OK", bg = "white", command = lambda: solve())
button_OK.place(x = 290, y = 320, height = 65, width = 65)

button_up = tk.Button(app, text = "˄", bg = "white", command = lambda: bar_up())
button_up.place(x = 290, y = 245, height = 65, width = 65)

button_down = tk.Button(app, text = "˅", bg = "white", command = lambda: bar_down())
button_down.place(x = 290, y = 395, height = 65, width = 65)

button_catalog = tk.Button(app, text = "ctl", bg = "white", command = lambda: catalog())
button_catalog.place(x = 365, y = 395, height = 65, width = 65)

button_end_left = tk.Button(app, text = "←", fg = "blue", command = lambda: end_left())
button_end_left.place(x = 440, y = 320, height = 65, width = 65)

button_end_right = tk.Button(app, text = "→", fg = "blue", command = lambda: end_right())
button_end_right.place(x = 515, y = 320, height = 65, width = 65)

#----------navigation bar button---------

button_1 = tk.Button(app, text = "1", bg = "white", command = lambda: add("1"))
button_1.place(x = 15, y = 465, height = 100, width = 100)

button_2 = tk.Button(app, text = "2", bg = "white", command = lambda: add("2"))
button_2.place(x = 125, y = 465, height = 100, width = 100)

button_3 = tk.Button(app, text = "3", bg = "white", command = lambda: add("3"))
button_3.place(x = 235, y = 465, height = 100, width = 100)

button_del = tk.Button(app, text = "Del", bg = "white", command = lambda: delete())
button_del.place(x = 345, y = 465, height = 100, width = 100)

button_ac = tk.Button(app, text = "AC", bg = "white", command = lambda: ac())
button_ac.place(x = 455, y = 465, height = 100, width = 100)

#---------------line 1---------------

button_4 = tk.Button(app, text = "4", bg = "white", command = lambda: add("4"))
button_4.place(x = 15, y = 575, height = 100, width = 100)

button_5 = tk.Button(app, text = "5", bg = "white", command = lambda: add("5"))
button_5.place(x = 125, y = 575, height = 100, width = 100)

button_6 = tk.Button(app, text = "6", bg = "white", command = lambda: add("6"))
button_6.place(x = 235, y = 575, height = 100, width = 100)

button_time = tk.Button(app, text = "×", bg = "white", command = lambda: add("×"))
button_time.place(x = 345, y = 575, height = 100, width = 100)

button_div = tk.Button(app, text = "÷", bg = "white", command = lambda: add("÷"))
button_div.place(x = 455, y = 575, height = 100, width = 100)

#---------------line 2---------------

button_7 = tk.Button(app, text = "7", bg = "white", command = lambda: add("7"))
button_7.place(x = 15, y = 685, height = 100, width = 100)

button_8 = tk.Button(app, text = "8", bg = "white", command = lambda: add("8"))
button_8.place(x = 125, y = 685, height = 100, width = 100)

button_9 = tk.Button(app, text = "9", bg = "white", command = lambda: add("9"))
button_9.place(x = 235, y = 685, height = 100, width = 100)

button_plus = tk.Button(app, text = "+", bg = "white", command = lambda: add("+"))
button_plus.place(x = 345, y = 685, height = 100, width = 100)

button_minus = tk.Button(app, text = "-", bg = "white", command = lambda: add("-"))
button_minus.place(x = 455, y = 685, height = 100, width = 100)

#---------------line 3---------------

button_0 = tk.Button(app, text = "0", bg = "white", command = lambda: add("0"))
button_0.place(x = 15, y = 795, height = 100, width = 100)

button_dot = tk.Button(app, text = ".", bg = "white", command = lambda: add("."))
button_dot.place(x = 125, y = 795, height = 100, width = 100)

button_pi = tk.Button(app, text = "π", bg = "white", command = lambda: add("π"))
button_pi.place(x = 235, y = 795, height = 100, width = 100)

button_euler = tk.Button(app, text = "e", bg = "white", command = lambda: add("e"))
button_euler.place(x = 345, y = 795, height = 100, width = 100)

button_exe = tk.Button(app, text = "=", bg = "white", command = lambda: solve())
button_exe.place(x = 455, y = 795, height = 100, width = 100)

#---------------line 4---------------

button_sin = tk.Button(app, text = "sin(", bg = "white", command = lambda: add("sin("))
button_sin.place(x = 15, y = 905, height = 100, width = 100)

button_cos = tk.Button(app, text = "cos(", bg = "white", command = lambda: add("cos("))
button_cos.place(x =125, y = 905, height = 100, width = 100)

button_tan = tk.Button(app, text = "tan(", bg = "white", command = lambda: add("tan("))
button_tan.place(x = 235, y = 905, height = 100, width = 100)

button_open_parenthesis = tk.Button(app, text = "(", bg = "white", command = lambda: add("("))
button_open_parenthesis.place(x = 345, y = 905, height = 100, width = 100)

button_sqrt = tk.Button(app, text = "√", bg = "white", command = lambda: add("√("))
button_sqrt.place(x = 455, y = 905, height = 100, width = 100)

button_asin = tk.Button(app, text = "asin(", bg = "white", command = lambda: add("asin("))
button_asin.place(x = 15, y = 1015, height = 100, width = 100)

button_acos = tk.Button(app, text = "acos(", bg = "white", command = lambda: add("acos("))
button_acos.place(x =125, y = 1015, height = 100, width = 100)

button_atan = tk.Button(app, text = "atan(", bg = "white", command = lambda: add("atan("))
button_atan.place(x = 235, y = 1015, height = 100, width = 100)

button_close_parenthesis = tk.Button(app, text = ")", bg = "white", command = lambda: add(")"))
button_close_parenthesis.place(x = 345, y = 1015, height = 100, width = 100)

button_sqrt = tk.Button(app, text = "^", bg = "white", command = lambda: add("^"))
button_sqrt.place(x = 455, y = 1015, height = 100, width = 100)


button_log = tk.Button(app, text = "log(", bg = "white", command = lambda: add("log("))
button_log.place(x = 15, y = 1125, height = 100, width = 100)

button_GCD = tk.Button(app, text = "GCD(", bg = "white", command = lambda: add("GCD("))
button_GCD.place(x = 125, y = 1125, height = 100, width = 100)

button_LCM = tk.Button(app, text = "LCM(", bg = "white", command = lambda: add("LCM("))
button_LCM.place(x = 235, y = 1125, height = 100, width = 100)

button_comma = tk.Button(app, text = ",", bg = "white", command = lambda: add(","))
button_comma.place(x = 345, y = 1125, height = 100, width = 100)

button_frac = tk.Button(app, text = "!", bg = "white", command = lambda: add("!"))
button_frac.place(x = 455, y = 1125, height = 100, width = 100)


degree_mode_txt = tk.Label(app, text = "Degree mode", fg = "blue", font = ("Arial", 5))
degree_mode_txt.place(x = 575, y = 460)

button_d_mode = tk.Button(app, text = "d", fg = "blue", command = lambda: mode_degree("d"), state = "disabled")
button_d_mode.place(x = 575, y = 490, height = 50, width = 50)

button_r_mode = tk.Button(app, text = "r", fg = "blue", command = lambda: mode_degree("r"), state = "normal")
button_r_mode.place(x = 635, y = 490, height = 50, width = 50)

text_imagnum_mode = tk.Label(app, text = "Imaginary number mode", fg = "blue", font = ("Arial", 4))
text_imagnum_mode.place(x = 555, y = 550)

button_ON_imagnum_mode = tk.Button(app, text = "ON", fg = "blue", command = lambda: on_imag_num(), state = "normal")
button_ON_imagnum_mode.place(x = 575, y = 590, height = 50, width = 50)

button_OFF_imagnum_mode = tk.Button(app, text = "OFF", fg = "blue", command = lambda: off_imag_num(), state = "disabled")
button_OFF_imagnum_mode.place(x = 635, y = 590, height = 50, width = 50)

text_decimal_mode = tk.Label(app, text = "Decimal number mode", fg = "blue", font = ("Arial", 4))
text_decimal_mode.place(x = 555, y = 645)

button_ON_decimal_mode = tk.Button(app, text = "ON", fg = "blue", command = lambda: on_deci_num(), state = "normal")
button_ON_decimal_mode.place(x = 575, y = 675, height = 50, width = 50)

button_OFF_decimal_mode = tk.Button(app, text = "OFF", fg = "blue", command = lambda: off_deci_num(), state = "disable")
button_OFF_decimal_mode.place(x = 635, y = 675, height = 50, width = 50)

button_reset_mode = tk.Button(app, text = "Reset", fg = "blue", command = lambda: reset_message())
button_reset_mode.place(x = 575, y = 735, height = 50, width = 110)

button_prime_number_analysis = tk.Button(app, text = "PNA", fg = "blue", command = lambda: PNA(), state = "disable")
button_prime_number_analysis.place(x = 575, y = 795, height = 50, width = 110)

init_key()
change_language()
app.mainloop()