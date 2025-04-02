import tkinter as tk
from tkinter import *
import math as m
from sympy import *
from fractions import *
import re as r
import random
import time
import sys
import json
import os
import string
import webbrowser
import threading
import concurrent.futures
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

version_of_calc = "Version 1.5.0.0"
url_help = "https://docs.google.com/forms/d/e/1FAIpQLSfRlg5Wo8wQpya0evQ00vT6waKZlB-eNCyYJY4q9T8ApKBemw/viewform?usp=sf_link"
DATA_FILE = "variable_data.json"
private_key_path = "private_key.pem"
public_key_path = "public_key.pem"
signature_path = "signature.sig"
key = ""
language = "English"
choose_language = ["English", "Vietnamese", "Chinese", "Japanese"]
cache_lang = ""
solve_thread = None
executor = concurrent.futures.ThreadPoolExecutor(max_workers = 5)
var_calc = ""

expression = ["|"]
output = ""
ans = 0
enter_eq = 0
limit_low = -10**300
limit_high = 10**300
limit_low_result = 10**(-3)
limit_high_result = 10**10
mode = "d"
imag = "OFF"
deci = "OFF"
ES_mode = "OFF"
fix_num = 9
shift_select = False
fix_out = -1
sci_out = -1
fix_txt = ""
sci_txt = ""
norm_txt = " : 1"
width_screen, height_screen = 400, 750
max_expression_cache = 30
use_button = False
max_length_exp = 49
max_lines = 4
line_in_scr = 0

name_ES = ["m", "μ", "n", "p", "f", "k", "M", "G", "T", "P", "E"]
list_cal = ["h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "sin(", "cos(", "tan(", "asin(", "acos(", "atan(", "log(", "frac(", "GCD(", "LCM(", "(", "√(", "π", "e", "∆", "Ran#", "RanInt#(", "abs(", chr(1200), "x", "y", "z", "Σ("]
list_num = ["0", "1", "2", "3", "4", "5", "6", "7" ,"8", "9", ".", ")", "∆", "π", "e", "h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "Ran#", chr(1200), "x", "y", "z"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "%", "h", "ħ", "c₀", "ε₀", "μ₀", "Z₀", "G", "lₚ", "tₚ", "μɴ", "μʙ", "e", "Φ₀", "G₀", "Kᴊ", "Rᴋ", "mₚ", "mₙ", "mₑ", "mμ", "a₀", "α", "rₑ", "λc", "γₚ", "λcₚ", "λcₙ", "R∞", "μₚ", "μₑ", "μₙ", "μμ", "mτ", "u", "F", "Nᴀ", "k", "Vₘ", "R", "c₁", "c₂", "σ", "g", "atm", "Rₖ_₉₀", "Kᴊ_₉₀", "t", "φ", "∆", "π", "e", chr(1200), "x", "y", "z"]
power_number = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
name_variable = ["x", "y", "z"]
expression_variable = ["0", "0", "0"]
have_var = []

out1_cache = ""
out2_cache = ""
expression_cache = []
cache_count = -1
calc_mode = "Normal"
calc_mode_cache = ""
min_scroll, max_scroll, select_scroll = [0], [3], 0
address_select = []
select_item = []
time_pointer = 0

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

Setting_select = [
["Calculator Settings",
[["Angle Unit", ["Degree!RATIO-ON!", "Radian!RATIO-OFF!", "Gradian!RATIO-OFF!"]],
["Number Format",
[[f"Fix!RATIO-OFF!{fix_txt}", ["Fix 0 : 0.",
                               "Fix 1 : 0.1",
                               "Fix 2 : 0.12",
                               "Fix 3 : 0.123",
                               "Fix 4 : 0.1234",
                               "Fix 5 : 0.12345",
                               "Fix 6 : 0.123456",
                               "Fix 7 : 0.1234567",
                               "Fix 8 : 0.12345678",
                               "Fix 9 : 0.123456789"]],
[f"Sci!RATIO-OFF!{sci_txt}", ["Sci 1 : 1 × 10^-1",
                                      "Sci 2 : 1.2 × 10^-1",
                                      "Sci 3 : 1.23 × 10^-1",
                                      "Sci 4 : 1.234 × 10^-1",
                                      "Sci 5 : 1.2345 × 10^-1",
                                      "Sci 6 : 1.23456 × 10^-1",
                                      "Sci 7 : 1.234567 × 10^-1",
                                      "Sci 8 : 1.2345678 × 10^-1",
                                      "Sci 9 : 1.23456789 × 10^-1",
                                      "Sci 10 : 1.234567890 × 10^-1"]],
[f"Norm!RATIO-ON!{norm_txt}", ["Norm 1 : 1.23 × 10^-3",
                               "Norm 2 : 0.00123"]]]],
["Engineer Symbol", ["ES : On!RATIO-OFF!",
                     "ES : Off!RATIO-ON!"]]]],

["System Settings",
[["Contrast", ["Light!RATIO-ON!",
               "Dark!RATIO-OFF!"]],
["Language", ["English!RATIO-ON!",
              "Tiếng Việt!RATIO-OFF!",
              "中国人!RATIO-OFF!",
              "日本語!RATIO-OFF!"]]]],

["Reset", ["Settings & Data",
           "Variable Memory",
           "Initialize All"]],

["Quality",
[["Screen", ["400 × 750!RATIO-ON!",
 			 "480 × 1100!RATIO-OFF!",
			 "500 × 720!RATIO-OFF!"]]]]
]

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


x = 0
y = 0
z = 0

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
	output = output.replace("e-0", "×10^-")
	output = output.replace("e-", "×10^-")
	output = output.replace("E", "e")
	output = output.replace("I", "i")
	output = output.replace("sqrt", "√")
	output = r.sub(r"exp\((.*?)\)", r"e^\1", output)
	return output

def solve_exp(real_exp):
	real_exp = str(real_exp)
	real_exp = real_exp.replace("∆", "(" + str(ans) + ")")
	real_exp = real_exp.replace("ₓ₁₀", "*10**")
	real_exp = real_exp.replace("×", "*")
	real_exp = real_exp.replace("÷", "/")
	real_exp = real_exp.replace("√", "Sqrt")
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
	real_exp = real_exp.replace("Σ", "sigma")
	real_exp = real_exp.replace("powEr", "power")
	return real_exp

def better_output(out):

	num = ""
	char = ""
	list_out = []

	out = out.replace("×10^", "ₓ₁₀")

	for i in out:

		if (i in number) or (i == "-"):
			num += i
			if char != "":
				list_out.append(char)
				char = ""
		
		else:
			char += i
			if num != "":
				list_out.append(num)
				num = ""
	
	if num != "":
		list_out.append(num)
	if char != "":
		list_out.append(char)
	
	for i in range(0, len(list_out)):

		if list_out[i] == "ₓ₁₀":

			list_out[i + 1] = list_out[i + 1].replace("-", "⎻")
			
			for j in range(0, 10):
				list_out[i + 1] = list_out[i + 1].replace(str(j), power_number[j])
	
	out = "".join(list_out)

	out = out.replace("-1×", "-")
	out = out.replace("+1×", "+")

	if out[: 2] == "1×":
		out = out[2 :]
	
	out = out.replace("-", " - ")
	out = out.replace("+", " + ")
	
	return out


def line_exp(input_list, max_length):
	
	global line_in_scr

	if calc_mode == "Calculating":

		result = ""
		for i in input_list:
			result += i
		
		return result
	
	if calc_mode == "Normal":

		result = []
		current_line = ""
		
		for word in input_list:
			if len(current_line) + len(word) <= max_length:
				current_line += word
				
			else:
				result.append(current_line)
				current_line = word
				
		if current_line:
			result.append(current_line)
		
		indice = [i for i, num in enumerate(result) if "|" in str(num)]

		try:
			indice = indice[0]
		
		except:
			indice = 0

		if indice < line_in_scr:
			line_in_scr = indice
		
		if indice > line_in_scr + 3:
			line_in_scr = indice - 3
		
		return '\n'.join(result[line_in_scr : line_in_scr + 4]) if len(result) >= 4 else '\n'.join(result)
	
	if calc_mode == "CALC1":

		left_exp = input_list[0 : input_list.index("|") + 1]

		if input_list[-1] != "|":
			right_exp = input_list[input_list.index("|") + 1 :]
			result = [right_exp[0]]
			length_result = len(result[0])
			del right_exp[0]
		
		else:
			right_exp = []
			result = []
			length_result = 0
		
		out_result = ""
		overflow_char = ""

		result.reverse()
		left_exp.reverse()

		for i in left_exp:

			result.append(i)
			length_result += len(i)

			if length_result > max_length_exp - 5:
				overflow_char = result[-1]
				del result[-1]
				break

		if result == input_list:
			result.reverse()
			out_result = "".join(result)
			return f"{out_result}"
		
		if overflow_char == "":
			result.reverse()
			result += right_exp
			out_result = "".join(result)

			if out_result == out_result[: max_length_exp - 4]:
				return f"{out_result}"
			
			else:
				return f"{out_result[: max_length_exp - 5]}▶"
			
		if result != left_exp:
			result.reverse()
			out_result = "".join(result)
			out_result = overflow_char + out_result
			out_result = out_result[:: -1]

			if right_exp == []:
				out_result = out_result[: max_length_exp - 5]
				return f"◀{out_result[:: -1]}"
			
			else:
				out_result = out_result[: max_length_exp - 6]
				return f"◀{out_result[:: -1]}▶"

def scr_exp(exp_input):

	exp_output = ""
	exp_output = line_exp(exp_input, max_length_exp)
	exp_output = exp_output.replace(chr(1200), "i")
	exp_output = exp_output.replace("x", "𝒙")
	exp_output = exp_output.replace("y", "𝒚")
	exp_output = exp_output.replace("z", "𝒛")

	return exp_output
	
def bar_up():
	
	global cache_count, expression, enter_eq, select_scroll, var_calc, expression_variable, x, y, z
	
	if calc_mode == "Catalog":
		
		select_scroll -= 1
		out1.config(text = scroll(select(Catalog_select, address_select)))
	
		return None
	
	if calc_mode == "Setting":
		
		select_scroll -= 1
		out1.config(text = scroll(select(Setting_select, address_select)))
	
		return None

	if calc_mode == "Error data":

		if out1.cget("text") == "Detect changes to data storage files!\n▶ Make new storage\n  Quit exit the program":
			out1.config(text = "Detect changes to data storage files!\n  Make new storage\n▶ Quit exit the program")
		
		else:
			out1.config(text = "Detect changes to data storage files!\n▶ Make new storage\n  Quit exit the program")
		
		return None
	
	if calc_mode == "Check":
		
		try:
			webbrowser.open(url_help)
		
		except:
			pass
		
		return None
		
	if calc_mode == "Calculating":
		return None
	
	if calc_mode == "CALC":

		expression_variable = [x, y, z]

		if have_var.index(var_calc) != 0:
			var_calc = have_var[have_var.index(var_calc) - 1]
			out2_var()

		up_down_cache()
		
		return None
	
	button_prime_number_analysis.config(state = "disable")
	
	if calc_mode == "Error":
		return None
	
	if calc_mode == "Reset":
		return None
	
	if ("|" in expression) and (expression != ["|"]):
		
		k = 0
		z = expression.index("|")

		if z == 0:
			return None
		
		while True:

			k += len(expression[z - 1])
			z -= 1
			bar_left()

			if z == 0:
				return None
			
			if k >= max_length_exp:
				return None
	
	else:

		if expression_cache == []:
			return None
		
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
	
	global cache_count, expression, enter_eq, select_scroll, calc_mode, language, var_calc, expression_variable, x, y, z
	
	if calc_mode == "Catalog":
		
		select_scroll += 1
		out1.config(text = scroll(select(Catalog_select, address_select)))
	
		return None
	
	if calc_mode == "Setting":
		
		select_scroll += 1
		out1.config(text = scroll(select(Setting_select, address_select)))
	
		return None
	
	if calc_mode == "Error data":

		bar_up()
		return None
	
	if calc_mode == "Check":
		
		return None
	
	if calc_mode == "Calculating":
		return None
	
	button_prime_number_analysis.config(state = "disable")
	
	if calc_mode == "Error":
		return None
	
	if calc_mode == "CALC":
		
		expression_variable = [x, y, z]

		if have_var.index(var_calc) == len(have_var) - 1:
			return None

		else:
			var_calc = have_var[have_var.index(var_calc) + 1]
			out2_var()
		
		up_down_cache()
		
		return None
	
	if calc_mode == "Reset":
		return None
	
	if ("|" in expression) and (expression != ["|"]):

		k = 0
		z = expression.index("|")

		if z == len(expression) - 1:
			return None
		
		while True:

			k += len(expression[z + 1])
			z += 1
			bar_right()

			if z == len(expression) - 1:
				return None
			
			if k >= max_length_exp:
				return None
	
	if ("|" not in expression) or (expression == ["|"]):

		if expression_cache == []:
			return None

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
	
	global expression, enter_eq, cache_count, expression_cache, address_select, select_scroll, address_select
	
	if calc_mode == "Catalog":
		if address_select != []:
			select_scroll = address_select[-1]
			del address_select[-1], min_scroll[-1], max_scroll[-1]
			out1.config(text = scroll(select(Catalog_select, address_select)))
		
		return None
	
	if calc_mode == "Setting":
		if address_select != []:
			select_scroll = address_select[-1]
			del address_select[-1], min_scroll[-1], max_scroll[-1]
			out1.config(text = scroll(select(Setting_select, address_select)))
		
		return None

	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Error":
		return None
	
	if calc_mode == "Calculating":
		return None
	
	if calc_mode == "CALC":
		return None
	
	elif calc_mode == "Reset":
		setting()
		out1.config(text = scroll(select(Setting_select, address_select)))
		return None
	
	elif enter_eq == 0:

		if expression == ["|"]:
			if expression_cache != []:
				
				try:
					expression = expression_cache[-1][0] + ["|"]
				
				except:
					expression = expression_cache[-1] + ["|"]

				out1.config(text = scr_exp(expression))
				out2.config(text = "")

				return None
			else:
				return None
		else:
			if "|" in expression:
				if expression[0] == "|":
					
					if calc_mode == "CALC1":
						return None

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
	
	if calc_mode == "Normal":
		out2.config(text = "")
		out1.config(text = scr_exp(expression))

	if calc_mode == "CALC1":
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")

	button_prime_number_analysis.config(state = "disable")
	cache_count = 0
	up_down_cache()

def bar_right():
	
	global expression, enter_eq, cache_count, address_select, select_scroll, select_item, min_scroll, max_scroll, calc_mode
	
	if calc_mode == "Catalog":
		if isinstance(select_item[select_scroll], list) == True:
			address_select.append(select_scroll)
			min_scroll.append(0)
			max_scroll.append(3)
			select_scroll = 0
			out1.config(text = scroll(select(Catalog_select, address_select)))
		
		return None
	
	if calc_mode == "Setting":
		if isinstance(select_item[select_scroll], list) == True:
			address_select.append(select_scroll)
			min_scroll.append(0)
			max_scroll.append(3)
			select_scroll = 0
			out1.config(text = scroll(select(Setting_select, address_select)))
		
		return None

	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Error":
		return None
		
	if calc_mode == "Calculating":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	elif enter_eq == 0:
		if expression == ["|"]:
			try:

				if calc_mode == "CALC":

					out2.config(text = f"{var_calc} = {scr_exp(expression)}")
					calc_mode = "CALC1"

					return None

				try:
					expression = ["|"] + expression_cache[-1][0]

				except:
					expression = ["|"] + expression_cache[-1]
					
				out1.config(text = scr_exp(expression))
				out2.config(text = "")

				return None

			except:
				pass
		else:
			if "|" in expression:
				if expression[-1] == "|":

					if calc_mode == "CALC1":
						return None
					
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
	if calc_mode == "Normal":
		out2.config(text = "")
		out1.config(text = scr_exp(expression))

	if calc_mode == "CALC":
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")
		calc_mode = "CALC1"
	
	if calc_mode== "CALC1":
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")

	button_prime_number_analysis.config(state = "disable")
	cache_count = 0
	up_down_cache()

def bar_add(var):

	global expression, cache_count, enter_eq
	
	if var == "i":
		var = chr(1200)
		
	try:
		k = expression.index("|")
		expression = list(expression[: k]) + [var] + list(expression[k :])
		if ("(" in var) and (var != "(") and (")" not in var):
			del expression[k + 1]
			expression = list(expression[: k + 1]) + ["|", ")"] + list(expression[k + 1 :])
	except:
		expression = [var] + ["|"]
	
	enter_eq = 0
	cache_count = 0
	up_down_cache()

def bar_del():
	global expression, cache_count
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Setting":
		return None

	if calc_mode == "Error data":
		return None
	
	if expression == ["|"]:
		return None
	
	if calc_mode == "Calculating":
		return None
	
	else:
		if "|" in expression:
			k = expression.index("|")
			if k == 0:
				del expression[1]
			else:
				del expression[k - 1]
		else:
			pass
	cache_count = 0
	up_down_cache()

def add(var):

	global expression, enter_eq, calc_mode
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Setting":
		return None

	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		return None
		
	if calc_mode == "Calculating":
		return None
	
	if calc_mode == "Error":
		return None
	
	elif calc_mode == "Reset":
		return None
	
	elif "|" in expression:

		if enter_eq != 0:
			expression = ["|"]
			enter_eq = 0
		
		bar_add(var)
			
		if calc_mode == "Normal":
			out1.config(text = scr_exp(expression))
			out2.config(text = "")
			return None
		
		if (calc_mode == "CALC1") or (calc_mode == "CALC"):
			calc_mode = "CALC1"
			out2.config(text = f"{var_calc} = {scr_exp(expression)}")
			return None
		
	else:

		expression = ["|"]
		output = ""
		button_prime_number_analysis.config(state = "disable")

		if (var == "×") or (var == "÷") or (var == "+") or (var == "-") or (var == "^"):
			if enter_eq != 0:
				bar_add("∆")
		bar_add(var)

		if calc_mode == "Normal":
			out1.config(text = scr_exp(expression))
			out2.config(text = output)
		if calc_mode == "CALC1":
			out2.config(text = f"{var_calc} = {scr_exp(expression)}")
	button_prime_number_analysis.config(state = "disable")
	
	enter_eq = 0


def on_key_press(event):

	if event.keysym == "0":
		add("0")
	
	if event.keysym == "1":
		add("1")

	if event.keysym == "2":
		add("2")
	
	if event.keysym == "3":
		add("3")
	
	if event.keysym == "4":
		add("4")
	
	if event.keysym == "5":
		add("5")

	if event.keysym == "6":
		add("6")
	
	if event.keysym == "7":
		add("7")
	
	if event.keysym == "8":
		add("8")
	
	if event.keysym == "9":
		add("9")

	if event.keysym == ".":
		add(".")
	
	if event.keysym == ",":
		add(",")
	
	if event.keysym == "Return":
		solve_screen()
	
	if event.keysym == "x":
		add("x")

	if event.keysym == "s":
		add("sin(")
	
	if event.keysym == "c":
		add("cos(")
	
	if event.keysym == "t":
		add("tan(")
	
	if event.keysym == "(":
		add("(")

	if event.keysym == ")":
		add(")")
	
	if event.keysym == "BackSpace":
		delete()


def fix_change_lang(text):

	return text[text.index("!") :]


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

		Setting_select[0][0] = "Calculator Settings"
		Setting_select[0][1][0][0] = "Angle Unit"
		Setting_select[0][1][0][1][0] = "Degree" + fix_change_lang(Setting_select[0][1][0][1][0])
		Setting_select[0][1][0][1][1] = "Radian" + fix_change_lang(Setting_select[0][1][0][1][1])
		Setting_select[0][1][0][1][2] = "Gradian" + fix_change_lang(Setting_select[0][1][0][1][2])
		Setting_select[0][1][1][0] = "Number Format"
		Setting_select[0][1][1][1][0][0] = "Fix" + fix_change_lang(Setting_select[0][1][1][1][0][0])
		Setting_select[0][1][1][1][1][0] = "Sci" + fix_change_lang(Setting_select[0][1][1][1][1][0])
		Setting_select[0][1][1][1][2][0] = "Norm" + fix_change_lang(Setting_select[0][1][1][1][2][0])
		Setting_select[0][1][2][0] = "Engineer Symbol"
		Setting_select[1][0] = "System Settings"
		Setting_select[1][1][0][0] = "Contrast"
		Setting_select[1][1][0][1][0] = "Light" + fix_change_lang(Setting_select[1][1][0][1][0])
		Setting_select[1][1][0][1][1] = "Dark" + fix_change_lang(Setting_select[1][1][0][1][1])
		Setting_select[1][1][1][0] = "Language"
		Setting_select[2][0] = "Reset"
		Setting_select[2][1][0] = "Settings & Data"
		Setting_select[2][1][1] = "Variable Memory"
		Setting_select[2][1][2] = "Initialize All"
		Setting_select[3][0] = "Quality"
		Setting_select[3][1][0][0] = "Screen"


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
		Catalog_select[1][1][1][0] = "Diện tích"
		Catalog_select[1][1][2][0] = "Thể tích"
		Catalog_select[1][1][3][0] = "Khối lượng"
		Catalog_select[1][1][4][0] = "Vận tốc"
		Catalog_select[1][1][5][0] = "Áp suất"
		Catalog_select[1][1][6][0] = "Năng lượng"
		Catalog_select[1][1][7][0] = "Công suất"
		Catalog_select[1][1][8][0] = "Nhiệt độ"
		Catalog_select[2][0] = "Xác suất"
		Catalog_select[3][0] = "Phép tính số"
		Catalog_select[4][0] = "Hyperbol/Lượng giác"

		Setting_select[0][0] = "Cài đặt phép tính"
		Setting_select[0][1][0][0] = "Đơn vị góc"
		Setting_select[0][1][0][1][0] = "Độ" + fix_change_lang(Setting_select[0][1][0][1][0])
		Setting_select[0][1][0][1][1] = "Radian" + fix_change_lang(Setting_select[0][1][0][1][1])
		Setting_select[0][1][0][1][2] = "Gradian" + fix_change_lang(Setting_select[0][1][0][1][2])
		Setting_select[0][1][1][0] = "Định dạng số"
		Setting_select[0][1][1][1][0][0] = "Chọn số thập phân" + fix_change_lang(Setting_select[0][1][1][1][0][0])
		Setting_select[0][1][1][1][1][0] = "Dạng a×10^n" + fix_change_lang(Setting_select[0][1][1][1][1][0])
		Setting_select[0][1][1][1][2][0] = "Viết bình thường" + fix_change_lang(Setting_select[0][1][1][1][2][0])
		Setting_select[0][1][2][0] = "Ký hiệu kĩ thuật"
		Setting_select[1][0] = "Cài đặt hệ thống"
		Setting_select[1][1][0][0] = "Độ tương phản"
		Setting_select[1][1][0][1][0] = "Sáng" + fix_change_lang(Setting_select[1][1][0][1][0])
		Setting_select[1][1][0][1][1] = "Tối" + fix_change_lang(Setting_select[1][1][0][1][1])
		Setting_select[1][1][1][0] = "Ngôn ngữ"
		Setting_select[2][0] = "Đặt lại"
		Setting_select[2][1][0] = "Cài đặt & Dữ liệu"
		Setting_select[2][1][1] = "Biến nhớ"
		Setting_select[2][1][2] = "Khởi tạo tất cả"
		Setting_select[3][0] = "Chất lượng"
		Setting_select[3][1][0][0] = "Màn hình"
	
	
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
		Catalog_select[1][1][1][0] = "区域"
		Catalog_select[1][1][2][0] = "体积"
		Catalog_select[1][1][3][0] = "音量"
		Catalog_select[1][1][4][0] = "速度"
		Catalog_select[1][1][5][0] = "压力"
		Catalog_select[1][1][6][0] = "能源"
		Catalog_select[1][1][7][0] = "容量"
		Catalog_select[1][1][8][0] = "温度"
		Catalog_select[2][0] = "概率"
		Catalog_select[3][0] = "数值计算"
		Catalog_select[4][0] = "双曲/三角"

		Setting_select[0][0] = "计算设置"
		Setting_select[0][1][0][0] = "角度单位"
		Setting_select[0][1][0][1][0] = "度" + fix_change_lang(Setting_select[0][1][0][1][0])
		Setting_select[0][1][0][1][1] = "弧度" + fix_change_lang(Setting_select[0][1][0][1][1])
		Setting_select[0][1][0][1][2] = "百分度" + fix_change_lang(Setting_select[0][1][0][1][2])
		Setting_select[0][1][1][0] = "数值格式"
		Setting_select[0][1][1][1][0][0] = "选择小数点" + fix_change_lang(Setting_select[0][1][1][1][0][0])
		Setting_select[0][1][1][1][1][0] = "a×10^n格式" + fix_change_lang(Setting_select[0][1][1][1][1][0])
		Setting_select[0][1][1][1][2][0] = "正常格式" + fix_change_lang(Setting_select[0][1][1][1][2][0])
		Setting_select[0][1][2][0] = "技术符号"
		Setting_select[1][0] = "系统设置"
		Setting_select[1][1][0][0] = "对比度"
		Setting_select[1][1][0][1][0] = "明亮" + fix_change_lang(Setting_select[1][1][0][1][0])
		Setting_select[1][1][0][1][1] = "黑暗" + fix_change_lang(Setting_select[1][1][0][1][1])
		Setting_select[1][1][1][0] = "语言"
		Setting_select[2][0] = "重置"
		Setting_select[2][1][0] = "设置与数据"
		Setting_select[2][1][1] = "内存变量"
		Setting_select[2][1][2] = "全部初始化"
		Setting_select[3][0] = "质量"
		Setting_select[3][1][0][0] = "屏幕"
	
	
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
		Catalog_select[1][1][1][0] = "エリア"
		Catalog_select[1][1][2][0] = "ボリューム"
		Catalog_select[1][1][3][0] = "ボリューム"
		Catalog_select[1][1][4][0] = "速度"
		Catalog_select[1][1][5][0] = "圧力"
		Catalog_select[1][1][6][0] = "エネルギー"
		Catalog_select[1][1][7][0] = "容量"
		Catalog_select[1][1][8][0] = "温度"
		Catalog_select[2][0] = "確率"
		Catalog_select[3][0] = "数値計算"
		Catalog_select[4][0] = "双曲線/三角関数"

		Setting_select[0][0] = "計算設定"
		Setting_select[0][1][0][0] = "角度単位"
		Setting_select[0][1][0][1][0] = "度" + fix_change_lang(Setting_select[0][1][0][1][0])
		Setting_select[0][1][0][1][1] = "ラジアン" + fix_change_lang(Setting_select[0][1][0][1][1])
		Setting_select[0][1][0][1][2] = "グラディアン" + fix_change_lang(Setting_select[0][1][0][1][2])
		Setting_select[0][1][1][0] = "数値形式"
		Setting_select[0][1][1][1][0][0] = "小数点を選択" + fix_change_lang(Setting_select[0][1][1][1][0][0])
		Setting_select[0][1][1][1][1][0] = "a×10^n形式" + fix_change_lang(Setting_select[0][1][1][1][1][0])
		Setting_select[0][1][1][1][2][0] = "通常形式" + fix_change_lang(Setting_select[0][1][1][1][2][0])
		Setting_select[0][1][2][0] = "技術表記"
		Setting_select[1][0] = "システム設定"
		Setting_select[1][1][0][0] = "コントラスト"
		Setting_select[1][1][0][1][0] = "明るい" + fix_change_lang(Setting_select[1][1][0][1][0])
		Setting_select[1][1][0][1][1] = "暗い" + fix_change_lang(Setting_select[1][1][0][1][1])
		Setting_select[1][1][1][0] = "言語"
		Setting_select[2][0] = "リセット"
		Setting_select[2][1][0] = "設定とデータ"
		Setting_select[2][1][1] = "メモリ変数"
		Setting_select[2][1][2] = "すべて初期化"
		Setting_select[3][0] = "品質"
		Setting_select[3][1][0][0] = "画面"


def up_down_cache():

	if calc_mode == "Normal":
	
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
		
		return None
	
	if (calc_mode == "CALC") or (calc_mode == "CALC1"):

		if have_var.index(var_calc) == 0:
			down_cache.config(fg = "white")
			up_cache.config(fg = "black")
		
		elif have_var.index(var_calc) == len(have_var) - 1:
			up_cache.config(fg = "white")
			down_cache.config(fg = "black")
		
		else:
			up_cache.config(fg = "white")
			down_cache.config(fg = "white")
		
		return None
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")


def shift():
	
	global shift_select
	
	if shift_select == False:	
		shift_select = True
		shift_screen.config(fg = "white")
	
	else:
		shift_select = False
		shift_screen.config(fg = "black")
	
def delete():
	global expression
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Setting":
		return None
	
	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Calculating":
		return None
	
	if calc_mode == "Error":
		return None
	elif calc_mode == "Reset":
		return None
		
	bar_del()

	if calc_mode == "CALC1":
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")

	else:
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

def generate_keys():
    if not os.path.exists(private_key_path) or not os.path.exists(public_key_path):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

        with open(private_key_path, "wb") as private_file:
            private_file.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        public_key = private_key.public_key()
        with open(public_key_path, "wb") as public_file:
            public_file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

def sign_file():

    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password = None)

    hasher = hashes.Hash(hashes.SHA256())
    with open(DATA_FILE, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    file_hash = hasher.finalize()

    signature = private_key.sign(
        file_hash,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

    with open(signature_path, "wb") as sig_file:
        sig_file.write(signature)

def verify_file_signature():

	if not os.path.exists(DATA_FILE):

		if os.path.exists(public_key_path):
			return False
		
		return True
	
	try:
		with open(public_key_path, "rb") as key_file:
			public_key = serialization.load_pem_public_key(key_file.read())
	
	except:
		return None
		
	hasher = hashes.Hash(hashes.SHA256())
	with open(DATA_FILE, 'rb') as file:
		while chunk := file.read(8192):
			hasher.update(chunk)
			
	file_hash = hasher.finalize()
	
	try:
		with open(signature_path, "rb") as sig_file:
			signature = sig_file.read()
	
	except:
		return False
		
	try:
		public_key.verify(
            signature,
            file_hash,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
		return True
	except Exception as e:
		return False
	
def ac():
	global expression, enter_eq, cache_count, expression_cache, calc_mode, out1_cache, out2_cache, min_scroll, max_scroll, select_scroll, address_select, select_item, shift_select, output
	
	if shift_select == True:
		
		off_calc_1()
		return None
	
	elif calc_mode == "Catalog":
		
		out1.config(text = out1_cache)
		out2.config(text = out2_cache)
		
		out1_cache = ""
		out2_cache = ""
		
		min_scroll, max_scroll, select_scroll = [0], [3], 0
		address_select = []
		select_item = []
		
		calc_mode = "Normal"
		
		up_down_cache()
		
		return None
	
	elif calc_mode == "Setting":
		
		out1.config(text = out1_cache)
		out2.config(text = out2_cache)
		
		out1_cache = ""
		out2_cache = ""
		
		min_scroll, max_scroll, select_scroll = [0], [3], 0
		address_select = []
		select_item = []
		
		calc_mode = "Normal"
		
		up_down_cache()
		
		return None
	
	if (calc_mode == "CALC") or (calc_mode == "CALC1"):

		calc_mode = "Normal"
		expression = ["|"]
		out1.config(text = scr_exp(expression))
		out2.config(text = "", anchor = "e")

		try:
			del expression_cache[-1][expression_cache[-1].index("|")]
		except:
			pass

		expression_cache[-1] = [expression_cache[-1], None]

		return None
	
	if calc_mode == "Error data":
		return None
	
	elif calc_mode == "Check":
		return None
	
	elif calc_mode == "Reset":
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
		
		calc_mode = "Normal"

def on():
	
	global expression, expression_cache, cache_count, enter_eq, calc_mode, min_scroll, max_scroll, select_scroll, address_select, select_item, solve_thread
	
	if solve_thread != None:
		solve_thread.join()
		solve_thread = None
	
	if calc_mode == "Error data":
		return None
	
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
	out1.config(anchor = "nw")
	
def error_message():
	
	global calc_mode, cache_count
	
	calc_mode = "Error"
	
	out1.config(anchor = "nw")
	out2.config(anchor = "e")
	
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

def fix_result(result):		
	
	if result % 1 == 0:
		return int(result)
	
	else:
		result = str(result)
		result = float(result)
		
		if result % 1 == 0:
			return int(result)
		else:
			return float(result)

def simp(in_exp):
	
	in_exp += sqrt(0)
	
	if len(in_exp.as_ordered_terms()) >= 3:
		return fix_result(round(N(in_exp), fix_num))
		
	if deci == "ON":
		return fix_result(round(N(in_exp), fix_num))
	
	if "sqrt" in str(in_exp):
		
		sqrt_terms = []
		constant_terms = []
		
		for term in in_exp.as_ordered_terms():
			
			if "sqrt" in str(term):
				coeff, sqrt_part = term.as_coeff_Mul()
				sqrt_terms.append((coeff, sqrt_part))
			
			elif term.is_Number:
				constant_terms.append(term)
		
		if len(constant_terms) == 0:
				
			output_1 = str(together(ratsimp(in_exp)))
			output_2 = str(together(in_exp.simplify()))
				
			if output_1 == output_2:
				return output_1
						
			else:
					if len(output_1) < len(output_2):
						return output_1
					
					else:
						return output_2
		
		
		else:
			
			num_const = None
			num_sqrt = None
			make_frac = None
			
			if constant_terms[0] % 1 != 0:
				
				num_const = Fraction(float(constant_terms[0])).limit_denominator(10**(fix_num - 1))
				num_const = num_const.denominator
			
			if sqrt_terms[0][0] % 1 != 0:
				
				num_sqrt = Fraction(float(sqrt_terms[0][0])).limit_denominator(10**(fix_num - 1))
				num_sqrt = num_sqrt.denominator
			
			if num_const == None:
				if num_sqrt != None:
					make_frac = num_sqrt
				
				else:
					return in_exp
				
			else:
				if num_sqrt == None:
					make_frac = num_const
				
				else:
					make_frac = lcm(num_const, num_sqrt)
			
			if make_frac < 100:
				
				out = int(constant_terms[0] * make_frac) + int(sqrt_terms[0][0] * make_frac) * sqrt_terms[0][1]
				out = together(out/make_frac)
				return out
			
			else:
				
				return fix_result(round(N(in_exp), fix_num))
			
			
	else:
		
		out = Fraction(float(N(in_exp))).limit_denominator(10**fix_num)
		
		if (len(str(out)) <= 7) and ("-" not in str(out)):
			return out
		
		if (len(str(out)) <= 8) and ("-" in str(out)):
			return out
		
		else:
			
			if (len(in_exp.as_ordered_terms()) == 1) and ("pi" in str(in_exp)) and ("/" not in str(in_exp)) and (N(in_exp) <= 1000000) and (in_exp.as_coeff_Mul()[0] % 1 == 0):
				return in_exp
			
			else:
				return fix_result(round(N(out), fix_num))


def MB10(input_result, limit_low, limit_high):

	result = eval(str(N(input_result)))
	
	if result == 0:
		return "0"
	
	result += 0*I
	power = 0
	sign = ""
	
	if result.as_real_imag()[1] == 0:
		
		result = result.as_real_imag()[0]

		if ES_mode == "ON":
			return ES_handle(result)
		
		if (norm_txt == " : 2") and (limit_low <= abs(result) < limit_high):
			
			return result_handle(input_result)
		
		if (fix_out != -1) and (result >= limit_high):
			
			pass
		
		elif (fix_out != -1) or (sci_out != -1):
			
			return f"{result_handle(input_result)}"
	
		if result < 0:
			sign = "-"
			result *= -1
		
		if abs(result) >= limit_high:
			while round(result, 9) >= 10:
				result /= 10
				power += 1
			
			result = fix_result(round(result, fix_num))
			result = round(result, fix_num)
			
			return f"{sign}{result}×10^{power}"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
			
			result = fix_result(round(result, fix_num))
			result = round(result, fix_num)
		
			return f"{sign}{result}×10^{power}"
		
		else:
			
			result = simp(input_result)
			return f"{result}"
	
	elif result.as_real_imag()[0] == 0:
		
		result = result.as_real_imag()[1]

		if ES_mode == "ON":
			return f"{ES_handle(result)}*I"
	
		if result < 0:
			sign = "-"
			result *= -1
		
		if (norm_txt == " : 2") and (limit_low <= result < limit_high):
			
			return f"{result_handle(input_result.as_real_imag()[1])}*I"
		
		if (fix_out != -1) and (result >= limit_high):
			
			pass
		
		elif (fix_out != -1) or (sci_out != -1):
			
			return f"{result_handle(input_result.as_real_imag()[1])}*I"
		
		if abs(result) >= limit_high:
			while round(result, 9) >= 10:
				result /= 10
				power += 1
			
			result = fix_result(round(result, fix_num))
			result = round(result, fix_num)
			
			return f"{sign}{result}×10^{power}*I"
		
		elif abs(result) < limit_low:
			while result < 1:
				result *= 10
				power -= 1
			
			result = fix_result(round(result, fix_num))
			result = round(result, fix_num)
			
			return f"{sign}{result}×10^{power}*I"
		
		else:
			
			result = simp(input_result.as_real_imag()[1])
			return f"{result}*I"
	
	else:
		
		result_real, result_imag = result.as_real_imag()
		power_real = 0
		power_imag = 0
		output_result = ""
		
		if (fix_out != -1) and (result_real >= limit_high):
			
			pass
		
		elif (fix_out != -1) or (sci_out != -1):
			
			output_result_handle = f"{result_handle(input_result.as_real_imag()[0])}"
		
		if result_real < 0:
			sign = "-"
			result_real *= -1
		
		if (norm_txt == " : 2") and (limit_low <= result_real < limit_high):
			
			output_result_handle = f"{result_handle(input_result.as_real_imag()[0])}"
		
		if abs(result_real) >= limit_high:
			while round(result_real, 9) >= 10:
				result_real /= 10
				power_real += 1
			
			result_real = fix_result(round(result_real, fix_num))
			result_real = round(result_real, fix_num)
			
			output_result = f"{sign}{result_real}×10^{power_real}"
		
		elif abs(result_real) < limit_low:
			while result_real < 1:
				result_real *= 10
				power_real -= 1
				
			result_real = fix_result(round(result_real, fix_num))
			result_real = round(result_real, fix_num)
		
			output_result = f"{sign}{result_real}×10^{power_real}"
		
		else:
			
			output_result = str(simp(input_result.as_real_imag()[0]))
		
		if result_imag < 0:
			sign = "-"
			result_imag *= -1
		
		else:
			sign = "+"
		
		if (norm_txt == " : 2") and (limit_low <= result_real < limit_high):
			
			output_result_handle += f"{sign}{result_handle(abs(input_result.as_real_imag()[1]))}*I"
			return output_result_handle
		
		if (fix_out != -1) and (result_imag >= limit_high):
			
			pass
		
		elif (fix_out != -1) or (sci_out != -1):
			
			output_result_handle += f"{sign}{result_handle(abs(input_result.as_real_imag()[1]))}*I"
			return output_result_handle
		
		if abs(result_imag) >= limit_high:
			while round(result_imag, 9) >= 10:
				result_imag /= 10
				power_imag += 1
			
			result_imag = fix_result(round(result_imag, fix_num))
			result_imag = round(result_imag, fix_num)
			
			output_result += f"{sign}{result_imag}×10^{power_imag}*I"
		
		elif abs(result_imag) < limit_low:
			while result_imag < 1:
				result_imag *= 10
				power_imag -= 1
			
			result_imag = fix_result(round(result_imag, fix_num))
			result_imag = round(result_imag, fix_num)
		
			output_result += f"{sign}{result_imag}×10^{power_imag}*I"
		
		else:
			
			output_result += f"{sign}{simp(input_result.as_real_imag()[1])}*I"
		
		return output_result

def check_output_number(inp):
	
	copy_inp = str(inp)
	
	try:
		inp = float(inp)
		if inp % 1 == 0:
			inp = str(int(inp))
		else:
			inp = str(float(inp))
		if inp == copy_inp:
			return True
		else:
			return False
	except:
		return False

def result_handle(inp):
	
	inp = simp(inp)
	
	if check_output_number(inp) == False:
		
		return inp
	
	if norm_txt == " : 2":
		
		if ("." not in str(inp)) and inp % 1 == 0:
			
			return inp
		
		else:
			
			inp = f"{float(inp):.11f}"
			while True:
				if inp[-1] == "0":
					inp = inp[: -1]
				else:
					break
			
			return inp

	if fix_out != -1:
		
		inp = round(N(inp), fix_out)
		inp = str(inp)
		
		return f"{float(inp):.{fix_out}f}"[: 11]
		
	elif sci_out != -1:
			
		sign = ""
			
		if inp < 0:
			sign = "-"
			inp *= -1
			
		power = 0
			
		if abs(inp) >= 1:
			while round(inp, 9) >= 10:
				inp /= 10
				power += 1
				
			return f"{sign}{float(inp):.{sci_out}f}×10^{power}"
			
		elif abs(inp) < 1:
			while inp < 1:
				inp *= 10
				power -= 1
				
			return f"{sign}{float(inp):.{sci_out}f}×10^{power}"
			
		return inp
		
	else:
		return inp

def ES_handle(result_inp):

	result_inp = N(result_inp)
	power = 0

	if abs(result_inp) >= 1000:
		while abs(result_inp) >= 1000:
			result_inp /= 1000
			power += 3
		
	elif abs(result_inp) < 1:
		while (result_inp) < 1:
			result_inp *= 1000
			power -= 3
	
	if power > 0:

		if power <= 18:
			result_inp = f"{result_inp:.{11}f}"
			output = f"{fix_result(float(result_inp))} "
			output += name_ES[int(power/3 + 4)]
		else:
			output = f"{fix_result(result_inp)}×10^{power}"
		
		return output
	
	elif power < 0:
		
		if power >= -15:
			result_inp = f"{result_inp:.{11}f}"
			output = f"{fix_result(float(result_inp))} "
			output += name_ES[int(-power/3 - 1)]
			
		else:
			output = f"{fix_result(result_inp)}×10^{power}"
		return output
	
	else:
		return fix_result(result_inp)


def GCD(a, b):

	a, b = fix_input(a), fix_input(b)

	if a.as_real_imag()[1] != 0:
		return None
	
	if b.as_real_imag()[1] != 0:
		return None

	if a >= limit_high_result:
		return None

	if b >= limit_high_result:
		return None

	if a % 1 != 0:
		return None
	
	if b % 1 != 0:
		return None
	
	while b != 0:
		a, b = b, a % b

	return a

def LCM(a, b):

	a, b = fix_input(a), fix_input(b)

	if a.as_real_imag()[1] != 0:
		return None
	
	if b.as_real_imag()[1] != 0:
		return None

	if a >= limit_high_result:
		return None

	if b >= limit_high_result:
		return None

	if a % 1 != 0:
		return None
	
	if b % 1 != 0:
		return None
	
	return (a * b) / GCD(a, b)

def frac(n):
	return factorial(fix_input(n))

def RanInt(a, b):

	a, b = fix_input(a), fix_input(b)

	if a.as_real_imag()[1] != 0:
		return None
	
	if b.as_real_imag()[1] != 0:
		return None

	if abs(a) >= limit_high_result:
		return None

	if abs(b) >= limit_high_result:
		return None
	
	return random.randint(a, b)

def PNA_button():
	
	if calc_mode == "Catalog":
		button_prime_number_analysis.config(state = "disable")
		return None
	
	if calc_mode == "Setting":
		button_prime_number_analysis.config(state = "disable")
		return None
	
	if calc_mode == "Error data":
		return None
		
	if calc_mode == "Check":
		button_prime_number_analysis.config(state = "disable")
		return None
		
	if calc_mode == "Error":
		button_prime_number_analysis.config(state = "disable")
		return None
	
	if calc_mode == "CALC":
		button_prime_number_analysis.config(state = "disable")
		return None
	
	if calc_mode == "CALC1":
		button_prime_number_analysis.config(state = "disable")
		return None
	
	if calc_mode == "Calculating":
		button_prime_number_analysis.config(state = "disable")
		return None
	
	if ES_mode == "ON":
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
		elif result > limit_high_result:
			button_prime_number_analysis.config(state = "disable")
		else:
			button_prime_number_analysis.config(state = "normal")

def PNA():

	if ES_mode == "ON":
		return None
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
		
	if calc_mode == "Setting":
		return None
	
	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		
		out1.config(text = out1_cache)
		out2.config(text = out2_cache)
		
		calc_mode = "Normal"
		up_down_cache()
	
		return None
	
	if calc_mode == "Error":
		return None
	
	if calc_mode == "Calculating":
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

def fix_input(inp):

	inp = str(inp).replace("symbols('x')", "x")

	if "x" in inp:
		return N(inp)
		
	return N(eval(inp))

def sigma(exp_in, a, b):

	a, b = str(a).replace("symbols('x')", "x"), str(b).replace("symbols('x')", "x")
	a, b = eval(a), eval(b)
	
	if a % 1 != 0:
		return None
		
	if b % 1 != 0:
		return None
		
	if -(10 ** 10) < a <= b < 10**10:
		
		exp_in = str(exp_in)
		exp_in = exp_in.replace("x", chr(1201))
		exp_in = sympify(exp_in)
		
		result = summation(exp_in, (chr(1201), a, b))
		
		return result
		
	else:
		return None

def sinh(a):
	return m.sinh(fix_input(a))
		
def cosh(a):
	return m.cosh(fix_input(a))
		
def tanh(a):
	return m.tanh(fix_input(a))
		
def asinh(a):
	return m.asinh(fix_input(a))
		
def acosh(a):
	return m.acosh(fix_input(a))
		
def atanh(a):
	return m.atanh(fix_input(a))

def sin(a):

	global mode

	a = fix_input(a)

	if mode == "r":
		return m.sin(a)
	
	if mode == "d":
		return m.sin(m.radians(a))
	
	if mode == "g":
		return m.sin(m.radians(a*0.9))
		
def cos(a):

	global mode

	a = fix_input(a)

	if mode == "r":
		return m.cos(a)
	
	if mode == "d":
		return m.cos(m.radians(a))
	
	if mode == "g":
		return m.cos(m.radians(a*0.9))
		
def tan(a):

	global mode

	a = fix_input(a)

	if mode == "r":
		return m.tan(a)
	
	if mode == "d":
		return m.tan(m.radians(a))
	
	if mode == "g":
		return m.tan(m.radians(a*0.9))
		
def asin(a):

	global mode

	a = fix_input(a)

	if mode == "r":
		return m.asin(a)
	
	if mode == "d":
		return m.degrees(m.asin(a))
	
	if mode == "g":
		return m.degrees(m.asin(a))/0.9
		
def acos(a):

	global mode

	a = fix_input(a)

	if mode == "r":
		return m.acos(a)
	
	if mode == "d":
		return m.degrees(m.acos(a))
	
	if mode == "g":
		return m.degrees(m.acos(a))/0.9
	
		
def atan(a):

	global mode

	a = fix_input(a)

	if mode == "r":
		return m.atan(a)
	
	if mode == "d":
		return m.degrees(m.atan(a))
	
	if mode == "d":
		return m.degrees(m.atan(a))/0.9
	

def Sqrt(n, sq = 2):

	n, sq = str(fix_input(n)), str(fix_input(sq))

	if "x" not in n:
		n = str(N(eval(n)))
	else:
		n = str(N(n))
	
	if "x" not in sq:
		sq = str(N(eval(sq)))
	else:
		sq = str(N(sq))

	if N(n).as_real_imag()[1] != 0:
		return None

	if N(sq).as_real_imag()[1] != 0:
		return None
	
	if check_result(N(n)) == False:
		return None
	
	if check_result(N(sq)) == False:
		return None

	if eval(sq) == 2:
		return sqrt(N(n))
	
	out = Pow(N(n), N(1/N(sq)))
	if out == sqrt(N(n)):
		return sqrt(N(n))
	
	else:
		return out

def power(a, b):

	a, b = str(fix_input(a)), str(fix_input(b))

	if "x" not in a:
		a = str(N(eval(a)))
	else:
		a = str(N(a))
	
	if "x" not in b:
		b = str(N(eval(b)))
	else:
		b = str(N(b))

	if N(eval(a)).as_real_imag()[1] != 0:
		return None

	if N(eval(b)).as_real_imag()[1] != 0:
		return None

	if eval(b) * log(eval(a), 10) >= log(limit_high, 10):
		return None
	
	return N(Pow(N(a), N(b)))
	
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
	
	if calc_mode == "Setting":
		return None
	
	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		return None

	if calc_mode == "Calculating":
		return None
	
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

	if calc_mode == "CALC1":
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")
		return None
	
	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")

def end_right():
	global expression
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Setting":
		return None
	
	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Calculating":
		return None
	
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

	if calc_mode == "CALC1":
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")
		return None

	out1.config(text = scr_exp(expression))
	button_prime_number_analysis.config(state = "disable")
	
def reset_message():
	global out1_cache, out2_cache, calc_mode
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Setting":
		return None
	
	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Error":
		return None
	
	if calc_mode == "Calculating":
		return None
	
	if calc_mode != "Reset":
		out1_cache = out1.cget("text")
		out2_cache = out2.cget("text")
		
	calc_mode = "Reset"

	button_prime_number_analysis.config(state = "disable")

	if language == "English":
		out1.config(text = f"Are you sure you want to reset?\n{select(Setting_select, address_select)[select_scroll]}")
		out2.config(text = "Yes: [OK] or [=]\nNo: [AC]")
		
	elif language == "Vietnamese":
		out1.config(text = f"Bạn có chắc chắn muốn đặt lại?\n{select(Setting_select, address_select)[select_scroll]}")
		out2.config(text = "Có: [OK] hoặc [=]\nKhông: [AC]")
	
	elif language == "Chinese":
		out1.config(text = f"您确定要重置吗?\n{select(Setting_select, address_select)[select_scroll]}")
		out2.config(text = "可: [OK] 或者 [=]\n不: [AC]")
	
	elif language == "Japanese":
		out1.config(text = f"本当にリセットしますか?\n{select(Setting_select, address_select)[select_scroll]}")
		out2.config(text = "コ: [OK] または [=]\nいいえ: [AC]")
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")

def reset():
	global expression, output, ans, enter_eq, mode, imag, deci, out1_cache, out2_cache, expression_cache, cache_count, calc_mode, min_scroll, max_scroll, select_scroll, address_select, select_item, x
	
	calc_mode = "Normal"

	if select_scroll != 0:
		ans = 0
		x = 0

	expression = ["|"]
	output = ""
	enter_eq = 0
	if select_scroll != 1:
		mode = "d"
		imag = "OFF"
		deci = "OFF"
		off_imag_num()
		off_deci_num()
	out1.config(text = scr_exp(expression))
	out2.config(text = "")
	if select_scroll != 0:
		button_Ans.config(text = "∆ = 0")
	button_prime_number_analysis.config(state = "disable")
	out1_cache = ""
	out2_cache = ""
	expression_cache = []
	cache_count = -1
	up_down_cache()
	min_scroll, max_scroll, select_scroll = [0], [3], 0
	address_select = []
	select_item = []

def off_calc():
	return None

def off_calc_1():

	global calc_mode

	calc_mode = "OFF CALC"
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")
	shift_screen.config(fg = "black")
	
	for widget in app.winfo_children():
		if isinstance(widget, tk.Button):
			widget.config(command = lambda: off_calc())
	
	out1.config(text = "KERAS", anchor = "center", font = ("", 20))
	out2.config(text = version_of_calc, anchor = "center", font = ("", 7))
	
	app.after(2000, off_calc_2)

def off_calc_2():
	
	out1.config(text = "Power Calculator")
	out2.config(text = "Made by Nguyễn Hà")
	
	app.after(2300, off_calc_3)

def off_calc_3():
	
	app.destroy()

def calc_exp():

	global expression, calc_mode, expression_cache, var_calc, have_var

	have_var = []

	for i in name_variable:
		if i in expression:
			have_var.append(i)
	
	if have_var == []:
		solve_screen()
	
	else:
		
		calc_mode = "CALC"
		expression_cache.append(expression)
		have_var.append("▷ Execute")
		out1.config(text = out1.cget("text").replace("|", ""))
		expression = ["|"]

		var_calc = have_var[0]
		out2_var()
		up_down_cache()

def out2_var():

	global var_calc

	if "▷" in var_calc:

		out2.config(text = f"{var_calc}", anchor = "w")
		return None

	if var_calc == "x":

		out2.config(text = f"{var_calc} = {better_output(output_exp(x))}", anchor = "w")
	
	if var_calc == "y":

		out2.config(text = f"{var_calc} = {better_output(output_exp(y))}", anchor = "w")
	
	if var_calc == "z":

		out2.config(text = f"{var_calc} = {better_output(output_exp(z))}", anchor = "w")


def change_color(object_type, color_bg, color_fg, background):

    for widget in app.winfo_children():

        if object_type == "label" and isinstance(widget, tk.Label):
            if widget.cget("fg") == "black":
                pass
            elif widget.cget("fg") != "blue":
                widget.config(bg = color_bg, fg = color_fg)
            else:
                widget.config(bg = background)

        elif object_type == "button" and isinstance(widget, tk.Button):
            if widget.cget("fg") != "blue":
                widget.config(bg = color_bg, fg = color_fg)
            else:
                pass

def save_data(data):

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent = 4)

def load_data():

    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except:
                return {}
    return {}

def update_variable():

	global ans, mode, imag, x, y, z, Catalog_select, Setting_select, language, fix_out, sci_out, fix_txt, sci_txt, norm_txt, fix_num, deci, ES_mode, key, width_screen, height_screen
	
	try:
		with open(DATA_FILE, "r") as file:
			pass
	except:
		return None

	saved_data = load_data()
	ans = saved_data.get("ans")
	button_Ans.config(text = saved_data.get("ans_button"))
	mode = saved_data.get("mode")
	imag = saved_data.get("imag")
	if imag == "ON":
		button_OFF_imagnum_mode.config(state = "normal")
		button_ON_imagnum_mode.config(state = "disable")
	Catalog_select = saved_data.get("Catalog_select")
	Setting_select = saved_data.get("Setting_select")
	language = saved_data.get("language")
	fix_out = saved_data.get("fix_out")
	sci_out = saved_data.get("sci_out")
	fix_txt = saved_data.get("fix_txt")
	sci_txt = saved_data.get("sci_txt")
	norm_txt = saved_data.get("norm_txt")
	fix_num = saved_data.get("fix_num")
	deci = saved_data.get("deci")
	if deci == "ON":
		button_OFF_decimal_mode.config(state = "normal")
		button_ON_decimal_mode.config(state = "disable")
	ES_mode = saved_data.get("ES_mode")
	color = saved_data.get("color")
	if color == "#323232":
		app.config(bg = "black")
		change_color("label", "black", "white", "black")
		change_color("button", "white", "black", "black")
		out1.config(bg = "#323232")
		out2.config(bg = "#323232")
	
	key = saved_data.get("key")
	width_screen = saved_data.get("width_screen")
	height_screen = saved_data.get("height_screen")
	refresh_screen()

	x = eval(saved_data.get("x"))
	y = eval(saved_data.get("y"))
	z = eval(saved_data.get("z"))

def close_app():

	global ans, mode, imag, x, y, z, Catalog_select, Setting_select, language, fix_out, sci_out, fix_txt, sci_txt, norm_txt, fix_num, deci, ES_mode
	data = {
		"ans": ans,
		"ans_button": button_Ans.cget("text"),
		"mode": mode,
		"imag": imag,
		"Catalog_select": Catalog_select,
		"Setting_select": Setting_select,
		"language": language,
		"fix_out": fix_out,
		"sci_out": sci_out,
		"fix_txt": fix_txt,
		"sci_txt": sci_txt,
		"norm_txt": norm_txt,
		"fix_num": fix_num,
		"deci": deci,
		"ES_mode": ES_mode,
		"color": out1.cget("bg"),
		"key": key,
		"width_screen": width_screen,
		"height_screen": height_screen,
		"x": str(x),
		"y": str(y),
		"z": str(z)
	}
	save_data(data)
	sign_file()
	app.destroy()

def check_data():

	global calc_mode

	if verify_file_signature() == False:

		calc_mode = "Error data"

		out1.config(text = "Detect changes to data storage files!\n▶ Make new storage\n  Quit exit the program")
		out2.config(text = "Scroll: [^] or [˅]\nSelect: [OK] or [=]")
	
	else:

		generate_keys()
		update_variable()

def pointer(use_button):

	global time_pointer

	if use_button:

		time_pointer = 0

		if (calc_mode == "Normal") or (calc_mode == "CALC1"):

			press_button()

		return None

	while True:

		if (calc_mode == "Normal") or (calc_mode == "CALC1"):
			if "|" in expression:

				while True:
					
					if time_pointer >= 1200:
						off_calc_1()

					if time_pointer % 2 == 0:

						if calc_mode == "Normal":
							out1.config(text = out1.cget("text").replace("|", " "))
							time_pointer += 1
							time.sleep(0.5)
						if calc_mode == "CALC1":
							out2.config(text = out2.cget("text").replace("|", " "))
							time_pointer += 1
							time.sleep(0.5)
						
						else:
							break
						
					else:

						if calc_mode == "Normal":
							out1.config(text = scr_exp(expression))
							time_pointer += 1
							time.sleep(0.5)
						if calc_mode == "CALC1":
							out2.config(text = f"{var_calc} = {scr_exp(expression)}")
							time_pointer += 1
							time.sleep(0.5)
						
						else:
							break

def press_button():

	global time_pointer

	if calc_mode == "Normal":
		out1.config(text = scr_exp(expression))
	
	if calc_mode == "CALC1":
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")

def pointer_thread():
    thread = threading.Thread(target = pointer, args = (use_button, ))
    thread.daemon = True
    thread.start()

def light_screen():
	
	app.config(bg = "#F0F0F0")
	change_color("label", "black", "white", "#F0F0F0")
	change_color("button", "white", "black", "#F0F0F0")
	out1.config(bg = "black")
	out2.config(bg = "black")

def dark_screen():

	app.config(bg = "black")
	change_color("label", "black", "white", "black")
	change_color("button", "white", "black", "black")
	out1.config(bg = "#323232")
	out2.config(bg = "#323232")

def refresh_screen():

	app.geometry(f"{width_screen}x{height_screen}")

	calculator_screen.place(x = 0, y = 0, height = height_screen*8/55, width = width_screen)

	up_cache.place(x = width_screen*137/144, y = height_screen*5/33, height = height_screen*7/330, width = width_screen*5/72)
	down_cache.place(x = width_screen*65/72, y = height_screen*5/33, height = height_screen*7/330, width = width_screen*5/72)
	shift_screen.place(x = width_screen*41/48, y = height_screen*5/33, height = height_screen*7/330, width = width_screen*5/72)
	out1.place(x = 0, y = 0, height = height_screen/11, width = width_screen)

	#----------expression input screen----------

	out2.place(x = 0, y = height_screen/11, height = height_screen*3/55, width = width_screen)

	#-----------output screen----------

	button_Ans.place(x= width_screen*91/144, y = height_screen*8/33, height = height_screen*2/55, width = width_screen*53/144)
	button_ON.place(x = width_screen/144, y = height_screen*49/330, height = height_screen*7/165, width = width_screen*7/72)
	button_check.place(x = width_screen/9, y = height_screen*49/330, height = height_screen*7/165, width = width_screen*7/72)
	button_setting.place(x = width_screen/144, y = height_screen*32/165, height = height_screen*7/165, width = width_screen*7/72)
	button_shift.place(x = width_screen/9, y = height_screen*32/165, height = height_screen*7/165, width = width_screen*7/72)
	button_calc_exp.place(x = width_screen/144, y = height_screen*79/330, height = height_screen*7/165, width = width_screen*7/72)
	button_left.place(x = width_screen*43/144, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)
	button_right.place(x = width_screen*73/144, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)
	button_OK.place(x = width_screen*29/72, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)
	button_up.place(x = width_screen*29/72, y = height_screen*49/330, height = height_screen*13/330, width = width_screen*13/144)
	button_down.place(x = width_screen*29/72, y = height_screen*79/330, height = height_screen*13/330, width = width_screen*13/144)
	button_catalog.place(x = width_screen*73/144, y = height_screen*79/330, height = height_screen*13/330, width = width_screen*13/144)
	button_end_left.place(x = width_screen*11/18, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)
	button_end_right.place(x = width_screen*103/144, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)

	#----------navigation bar button---------

	button_1.place(x = width_screen/48, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)
	button_2.place(x = width_screen*25/144, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)
	button_3.place(x = width_screen*47/144, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)
	button_del.place(x = width_screen*23/48, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)
	button_ac.place(x = width_screen*91/144, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)

	#---------------line 1---------------

	button_4.place(x = width_screen/48, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)
	button_5.place(x = width_screen*25/144, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)
	button_6.place(x = width_screen*47/144, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)
	button_time.place(x = width_screen*23/48, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)
	button_div.place(x = width_screen*91/144, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)

	#---------------line 2---------------

	button_7.place(x = width_screen/48, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)
	button_8.place(x = width_screen*25/144, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)
	button_9.place(x = width_screen*47/144, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)
	button_plus.place(x = width_screen*23/48, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)
	button_minus.place(x = width_screen*91/144, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)

	#---------------line 3---------------

	button_0.place(x = width_screen/48, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)
	button_dot.place(x = width_screen*25/144, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)
	button_pi.place(x = width_screen*47/144, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)
	button_euler.place(x = width_screen*23/48, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)
	button_exe.place(x = width_screen*91/144, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)

	#---------------line 4---------------

	button_sin.place(x = width_screen/48, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)
	button_cos.place(x = width_screen*25/144, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)
	button_tan.place(x = width_screen*47/144, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)
	button_open_parenthesis.place(x = width_screen*23/48, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)
	button_sqrt.place(x = width_screen*91/144, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)
	button_asin.place(x = width_screen/48, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)
	button_acos.place(x = width_screen*25/144, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)
	button_atan.place(x = width_screen*47/144, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)
	button_close_parenthesis.place(x = width_screen*23/48, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)
	button_power.place(x = width_screen*91/144, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)
	button_log.place(x = width_screen/48, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)
	button_sigma.place(x = width_screen*25/144, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)
	button_x_var.place(x = width_screen*47/144, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)
	button_comma.place(x = width_screen*23/48, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)
	button_frac.place(x = width_screen*91/144, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)
	button_y_var.place(x = width_screen/48, y = height_screen*247/330, height = height_screen*2/33, width = width_screen*5/36)
	button_z_var.place(x = width_screen*25/144, y = height_screen*247/330, height = height_screen*2/33, width = width_screen*5/36)

	text_imagnum_mode.place(x = width_screen*37/48, y = height_screen/3)
	button_ON_imagnum_mode.place(x = width_screen*115/144, y = height_screen*59/165, height = height_screen/33, width = width_screen*5/72)
	button_OFF_imagnum_mode.place(x = width_screen*127/144, y = height_screen*59/165, height = height_screen/33, width = width_screen*5/72)
	text_decimal_mode.place(x = width_screen*37/48, y = height_screen*43/110)
	button_ON_decimal_mode.place(x = width_screen*115/144, y = height_screen*9/22, height = height_screen/33, width = width_screen*5/72)
	button_OFF_decimal_mode.place(x = width_screen*127/144, y = height_screen*9/22, height = height_screen/33, width = width_screen*5/72)
	button_prime_number_analysis.place(x = width_screen*115/144, y = height_screen*53/110, height = height_screen/33, width = width_screen*11/72)


def trim_after_last_exclamation(s):
	
	last_exclamation_index = s.rfind("!")
	
	if last_exclamation_index != -1:
		return s[:last_exclamation_index + 1]
	
	return s


def update_setting_select_list():
	
	global Setting_select
	
	fix_get_txt = Setting_select[0][1][1][1][0][0]
	sci_get_txt = Setting_select[0][1][1][1][1][0]
	norm_get_txt = Setting_select[0][1][1][1][2][0]
	
	fix_get_txt = trim_after_last_exclamation(fix_get_txt)
	sci_get_txt = trim_after_last_exclamation(sci_get_txt)
	norm_get_txt = trim_after_last_exclamation(norm_get_txt)
	
	Setting_select[0][1][1][1][0][0] = fix_get_txt + fix_txt
	Setting_select[0][1][1][1][1][0] = sci_get_txt + sci_txt
	Setting_select[0][1][1][1][2][0] = norm_get_txt + norm_txt
	
	
	
def setting_handle(inp):
	
	global Setting_select, address_select, mode, fix_out, sci_out, min_scroll, max_scroll, select_scroll, sci_txt, fix_txt, norm_txt, Setting_select, limit_low_result, fix_num, ES_mode, language, cache_lang, calc_mode, height_screen, width_screen, max_length_exp

	
	if "Degree" in inp:
		
		for i in range(len(Setting_select[0][1][0][1])):
			Setting_select[0][1][0][1][i] = Setting_select[0][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[0][1][0][1][0] = Setting_select[0][1][0][1][0].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		mode = "d"

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
		
	if "Radian" in inp:
		
		for i in range(len(Setting_select[0][1][0][1])):
			Setting_select[0][1][0][1][i] = Setting_select[0][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[0][1][0][1][1] = Setting_select[0][1][0][1][1].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		mode = "r"

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "Gradian" in inp:
		
		for i in range(len(Setting_select[0][1][0][1])):
			Setting_select[0][1][0][1][i] = Setting_select[0][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[0][1][0][1][2] = Setting_select[0][1][0][1][2].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		mode = "g"

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	
	if "Fix" in inp:
		
		for i in range(len(Setting_select[0][1][1][1])):
			Setting_select[0][1][1][1][i][0] = Setting_select[0][1][1][1][i][0].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[0][1][1][1][0][0] = Setting_select[0][1][1][1][0][0].replace("RATIO-OFF", "RATIO-ON")
		
		fix_out = select_scroll
		sci_out = -1
		fix_txt = f" : {fix_out}"
		sci_txt = ""
		norm_txt = ""
			
		select_scroll = address_select[-2]
			
		del address_select[-1]
		del min_scroll[-1]
		del max_scroll[-1]
		del address_select[-1]
		
		update_setting_select_list()

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "Sci" in inp:
		
		for i in range(len(Setting_select[0][1][1][1])):
			Setting_select[0][1][1][1][i][0] = Setting_select[0][1][1][1][i][0].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[0][1][1][1][1][0] = Setting_select[0][1][1][1][1][0].replace("RATIO-OFF", "RATIO-ON")
			
		sci_out = select_scroll + 1
		fix_out = -1
		sci_txt = f" : {sci_out}"
		fix_txt = ""
		norm_txt = ""
			
		select_scroll = address_select[-2]
			
		del address_select[-1]
		del min_scroll[-1]
		del max_scroll[-1]
		del address_select[-1]
		
		update_setting_select_list()

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "Norm" in inp:
		
		for i in range(len(Setting_select[0][1][1][1])):
			Setting_select[0][1][1][1][i][0] = Setting_select[0][1][1][1][i][0].replace("RATIO-ON", "RATIO-OFF")
		
		Setting_select[0][1][1][1][2][0] = Setting_select[0][1][1][1][2][0].replace("RATIO-OFF", "RATIO-ON")
		
		if select_scroll == 0:
			 
			limit_low_result = 10**(-3)
			fix_num = 9
		
		if select_scroll == 1:
			 
			limit_low_result = 10**(-9)
			fix_num = 11
			
		sci_out = -1
		fix_out = -1
		norm_txt = f" : {select_scroll + 1}"
		fix_txt = ""
		sci_txt = ""
			
		select_scroll = address_select[-2]
			
		del address_select[-1]
		del min_scroll[-1]
		del max_scroll[-1]
		del address_select[-1]
		
		update_setting_select_list()

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))

	
	if "ES : On" in inp:
		
		for i in range(len(Setting_select[0][1][2][1])):
			Setting_select[0][1][2][1][i] = Setting_select[0][1][2][1][i].replace("RATIO-ON", "RATIO-OFF")
		
		Setting_select[0][1][2][1][0] = Setting_select[0][1][2][1][0].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		ES_mode = "ON"

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "ES : Off" in inp:
		
		for i in range(len(Setting_select[0][1][2][1])):
			Setting_select[0][1][2][1][i] = Setting_select[0][1][2][1][i].replace("RATIO-ON", "RATIO-OFF")
		
		Setting_select[0][1][2][1][1] = Setting_select[0][1][2][1][1].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		ES_mode = "OFF"

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	

	if "Light" in inp:
		
		for i in range(len(Setting_select[1][1][0][1])):
			Setting_select[1][1][0][1][i] = Setting_select[1][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[1][1][0][1][0] = Setting_select[1][1][0][1][0].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		light_screen()

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "Dark" in inp:
		
		for i in range(len(Setting_select[1][1][0][1])):
			Setting_select[1][1][0][1][i] = Setting_select[1][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[1][1][0][1][1] = Setting_select[1][1][0][1][1].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		dark_screen()

		language = cache_lang
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	

	if "English" in inp:
		
		for i in range(len(Setting_select[1][1][1][1])):
			Setting_select[1][1][1][1][i] = Setting_select[1][1][1][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[1][1][1][1][0] = Setting_select[1][1][1][1][0].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		language = "English"
		change_language()
		out2.config(text = "Scroll: [^] or [˅]\nSelect: [OK] or [=]")
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "Tiếng Việt" in inp:
		
		for i in range(len(Setting_select[1][1][1][1])):
			Setting_select[1][1][1][1][i] = Setting_select[1][1][1][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[1][1][1][1][1] = Setting_select[1][1][1][1][1].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		language = "Vietnamese"
		change_language()
		out2.config(text = "Cuộn: [^] hoặc [˅]\nChọn: [OK] hoặc [=]")
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "中国人" in inp:
		
		for i in range(len(Setting_select[1][1][1][1])):
			Setting_select[1][1][1][1][i] = Setting_select[1][1][1][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[1][1][1][1][2] = Setting_select[1][1][1][1][2].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		language = "Chinese"
		change_language()
		out2.config(text = "滚动：[^] 或 [˅]\n选择：[OK] 或 [=]")
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "日本語" in inp:
		
		for i in range(len(Setting_select[1][1][1][1])):
			Setting_select[1][1][1][1][i] = Setting_select[1][1][1][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[1][1][1][1][3] = Setting_select[1][1][1][1][3].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		language = "Japanese"
		change_language()
		out2.config(text = "スクロール: [^] または [˅]\n選択: [OK] または [=]")
		
		out1.config(text = scroll(select(Setting_select, address_select)))


	if "Settings & Data" in inp:
		select_scroll = address_select[-1]
			
		del address_select[-1]

		language = cache_lang
		change_language()
		calc_mode = "Reset"
		reset_message()
	
	if "Variable Memory" in inp:
		select_scroll = address_select[-1]
			
		del address_select[-1]

		language = cache_lang
		change_language()
		calc_mode = "Reset"
		reset_message()

	if "Initialize All" in inp:
		select_scroll = address_select[-1]
			
		del address_select[-1]

		language = cache_lang
		change_language()
		calc_mode = "Reset"
		reset_message()
	

	if "400 × 750" in inp:

		for i in range(len(Setting_select[3][1][0][1])):
			Setting_select[3][1][0][1][i] = Setting_select[3][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[3][1][0][1][0] = Setting_select[3][1][0][1][0].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		width_screen, height_screen = 400, 750
		max_length_exp = 49

		refresh_screen()
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "480 × 1100" in inp:

		for i in range(len(Setting_select[3][1][0][1])):
			Setting_select[3][1][0][1][i] = Setting_select[3][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[3][1][0][1][1] = Setting_select[3][1][0][1][1].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		width_screen, height_screen = 480, 1100
		max_length_exp = 59

		refresh_screen()
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	if "500 × 720" in inp:

		for i in range(len(Setting_select[3][1][0][1])):
			Setting_select[3][1][0][1][i] = Setting_select[3][1][0][1][i].replace("RATIO-ON", "RATIO-OFF")

		Setting_select[3][1][0][1][2] = Setting_select[3][1][0][1][2].replace("RATIO-OFF", "RATIO-ON")
		select_scroll = address_select[-1]
			
		del address_select[-1]
		
		width_screen, height_screen = 500, 720
		max_length_exp = 61
		
		refresh_screen()
		change_language()
		
		out1.config(text = scroll(select(Setting_select, address_select)))
	
	return None


def select(A, pos):
	
	global calc_mode, min_scroll, max_scroll, select_item
	
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
				text.append(f"{A[i][0]}")
				
		else:
			for i in range(len(A)):
				if isinstance(A[i], list) == True:
					text.append(f"{A[i][0]}")
				else:
					text.append(f"{A[i]}")
	
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
		
		out_select = list[min_scroll[-1] + i]
		
		if text != "":
			text += "\n"
			
		if "!RATIO-ON!" in out_select:
			out_select = out_select.replace("!RATIO-ON!", "")
			if i + (min_scroll[-1] - select_scroll) == 0:
				text += f"⦿[{out_select}]"
			else:
				text += f"⦿ {out_select}"
		
		elif "!RATIO-OFF!" in out_select:
			out_select = out_select.replace("!RATIO-OFF!", "")
			if i + (min_scroll[-1] - select_scroll) == 0:
				text += f"◯[{out_select}]"
			else:
				text += f"◯ {out_select}"
		
		elif i + (min_scroll[-1] - select_scroll) == 0:
			text += f"▶ {out_select}"
		else:
			text += f"  {out_select}"

	return text

def catalog():
	
	global calc_mode, out1_cache, out2_cache, calc_mode_cache
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Catalog":
		return None

	if calc_mode == "Setting":
		return None
	
	if calc_mode == "Error data":
		return None
	
	if calc_mode == "Error":
		return None
	
	if calc_mode == "Calculating":
		return None
	
	if calc_mode == "CALC":
		return None
	
	calc_mode_cache = calc_mode
	calc_mode = "Catalog"
	
	out1_cache = out1.cget("text")
	out2_cache = out2.cget("text")
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")
	
	out1.config(text = scroll(select(Catalog_select, address_select)))
	out2.config(anchor = "e")
	
	if language == "English":
		out2.config(text = "Scroll: [^] or [˅]\nSelect: [OK] or [=]")
	
	elif language == "Vietnamese":
		out2.config(text = "Cuộn: [^] hoặc [˅]\nChọn: [OK] hoặc [=]")
	
	elif language == "Chinese":
		out2.config(text = "滚动：[^] 或 [˅]\n选择：[OK] 或 [=]")
	
	elif language == "Japanese":
		out2.config(text = "スクロール: [^] または [˅]\n選択: [OK] または [=]")


def setting():
	
	global calc_mode, out1_cache, out2_cache
	
	if calc_mode == "Check":
		return None
	
	if calc_mode == "Catalog":
		return None
	
	if calc_mode == "Error":
		return None
	
	if calc_mode == "Calculating":
		return None
	
	if calc_mode == "Setting":
		return None
	
	if calc_mode == "Error data":
		return None
	
	if calc_mode == "CALC":
		return None
	
	if calc_mode == "CALC1":
		return None
		
	calc_mode = "Setting"
	
	out1_cache = out1.cget("text")
	out2_cache = out2.cget("text")
	
	up_cache.config(fg = "black")
	down_cache.config(fg = "black")
	
	out1.config(text = scroll(select(Setting_select, address_select)))
	
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
			if real_exp[i + 5 * time_frac] == "!":
							
				parentheses = 0
				change_parentheses = False
				exit = False
							
				for j in range(i - 1 + 5 * time_frac, -1, -1):
								
					if exit == True:
						continue
								
					if real_exp[j] == ")":
						parentheses += 1
						change_parentheses = True
									
					if real_exp[j] == "(":
						parentheses -= 1
						change_parentheses = True
								
					if (parentheses == 0) and (change_parentheses == True):
						real_exp = real_exp[: j] + "(frac" + real_exp[j : i + 5 * time_frac] + ")" + real_exp[i + 1 + 5 * time_frac :]
						time_frac += 1
						exit = True
						

	while "^" in real_exp:
		
		time_pow = 0
		
		for i in range(len(real_exp) - 1, -1, -1):
			if real_exp[i] == "^":
				
				parentheses = 0
				change_parentheses = False
				exit = False
							
				for j in range(i, -1, -1):
								
					if exit == True:
						continue
								
					if real_exp[j] == ")":
						parentheses += 1
						change_parentheses = True
									
					if real_exp[j] == "(":
						parentheses -= 1
						change_parentheses = True
								
					if (parentheses == 0) and (change_parentheses == True):
						real_exp = real_exp[: j] + "(power(" + real_exp[j :]
						real_exp = real_exp[: i + 7] + "," + real_exp[i + 1 + 7:]
						time_pow += 1
						exit = True
						
				parentheses = 0
				change_parentheses = False
				exit = False
						
				for j in range(i + 7, len(real_exp)):
								
					if exit == True:
						continue
								
					if real_exp[j] == ")":
						parentheses += 1
						change_parentheses = True
									
					if real_exp[j] == "(":
						parentheses -= 1
						change_parentheses = True
								
					if (parentheses == 0) and (change_parentheses == True):
						real_exp = real_exp[: j] + "))" + real_exp[j :]
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


def solve_screen():
	
	global calc_mode, solve_thread, calc_mode_cache, expression_cache, expression, out1_cache, out2_cache
	
	if calc_mode == "Calculating":
		return None
	
	if (calc_mode == "CALC") and ("Execute" not in var_calc):

		calc_mode = "CALC1"
		expression = ["|"]
		out2.config(text = f"{var_calc} = {scr_exp(expression)}")

		return None
	
	if (calc_mode == "CALC") and ("Execute" in var_calc):

		calc_mode = "Normal"
		expression = expression_cache[-1]
		del expression_cache[-1]
	
	if ((calc_mode == "Normal") or (calc_mode == "CALC1")) and (expression != ["|"]):

		out1_cache = out1.cget("text")
		out2_cache = out2.cget("text")
		out2.config(anchor = "e")
	
		if language == "English":
			out1.config(text = "Calculating...", anchor = "center")
			
		elif language == "Vietnamese":
			out1.config(text = "Đang tính toán...", anchor = "center")
		
		elif language == "Chinese":
			out1.config(text = "计算...", anchor = "center")
		
		elif language == "Japanese":
			out1.config(text = "計算中...", anchor = "center")
	
		out2.config(text = "")
		
		calc_mode_cache = calc_mode
		calc_mode = "Calculating"
		
		solve_thread = executor.submit(solve)
	
	else:
		
		solve()
	
	
def solve():
	global expression, output, ans, enter_eq, list_cal, expression_cache, cache_count, select_scroll, address_select, calc_mode, select_item, min_scroll, max_scroll, Setting_select, language, cache_lang, var_calc, x, y, z
	
	if calc_mode == "Catalog":
		
		address_select.append(select_scroll)
		if select(Catalog_select, address_select) == None:
			
			calc_mode = calc_mode_cache
			add(select_item)
			address_select = []

			if calc_mode == "CALC1":

				out1.config(text = out1_cache)
				out2.config(text = f"{var_calc} = {scr_exp(expression)}", anchor = "w")
				return None
			
			up_down_cache()
			min_scroll, max_scroll, select_scroll = [0], [3], 0
			
		else:
			min_scroll.append(0)
			max_scroll.append(3)
			select_scroll = 0
			out1.config(text = scroll(select(Catalog_select, address_select)))
	
		return None
	
	elif calc_mode == "Setting":
		
		address_select.append(select_scroll)

		if select(Setting_select, address_select) == None:
			
			cache_lang = language
			language = "English"
			change_language()
			
			if calc_mode == "Setting":
			
				select(Setting_select, address_select)
				setting_handle(select_item)
			
		else:
			min_scroll.append(0)
			max_scroll.append(3)
			select_scroll = 0
			out1.config(text = scroll(select(Setting_select, address_select)))
	
		return None

	elif calc_mode == "Error data":
		
		text = out1.cget("text")

		if text == "Detect changes to data storage files!\n▶ Make new storage\n  Quit exit the program":
			if os.path.exists(DATA_FILE):
				os.remove(DATA_FILE)

			calc_mode = "Normal"
			out1.config(text = scr_exp(expression))
			out2.config(text = output)

		else:
			app.destroy()
		
		return None
	
	elif calc_mode == "Error":
		
		calc_mode = calc_mode_cache

		if calc_mode == "CALC1":
			
			expression = expression + ["|"]
			out1.config(text = out1_cache)
			out2.config(text = out2_cache, anchor = "w")

			return None

		expression = expression_cache[-1][0] + ["|"]
		out1.config(text = scr_exp(expression))
		out2.config(text = "")
		
		return None
	
	elif calc_mode == "Reset":
		
		reset()
		return None
	
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
				real_exp += ["0", "."]
		
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

				if (number_handle != "") and (chr(1200) not in number_handle) and (number_handle != "∆"):

					if abs(N(eval(solve_exp(number_handle.replace("%", ""))))) >= limit_high:
						number_handle = "_NUM"
						
					if abs(N(eval(solve_exp(number_handle.replace("%", ""))))) <= limit_low:
						number_handle = "0"
				
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
								
								if number_handle != "":
									new_exp += "(" + number_handle + ")" + i						
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
									
									if number_handle != "":
										new_exp += "(" + number_handle + ")" + i						
									else:
										new_exp += number_handle + i
							
							else:
								new_exp += i
					
					except:
						if number_handle == "":
							new_exp += i
			
				number_handle = ""
		
		ans = str(ans)
		ans = ans.replace(" ", "")
		
		real_exp = new_exp
		real_exp = change_exp(real_exp)
		real_exp = solve_exp(real_exp)
		real_exp = real_exp.replace("x", "symbols('x')")
		real_exp = str(real_exp)
		
		try:

			output = eval(real_exp)

			while "x" in str(output):
				output = eval(str(output))

			if deci == "ON":
				output = N(output)

			if ("I" in str(output)) and (imag == "OFF"):
				error += 1

		except:

			error += 1
		
		try:
			check = check_result(N(output))

			if check == False:
				error += 1

		except:
			error += 1
		
		if calc_mode != "Calculating":
			return None
	
		if error == 0:
			
			if calc_mode == "Calculating":
				
				output_copy_ans = output
				output = MB10(output, limit_low_result, limit_high_result)
				output = better_output(output_exp(output))
				
				if calc_mode == "Calculating":
					
					out1.config(anchor = "nw")
					
					enter_eq += 1
					
					if calc_mode_cache == "Normal":

						ans = str(output_copy_ans)
						out2.config(text = "= " + str(output))
						out1.config(text = scr_exp(expression))
						button_Ans.config(text = "∆ = " + output)

						try:
							if expression_cache[-1][1] != None:
								pass
							else:
								del expression_cache[-1]
						except:
							pass
						expression_cache.append([expression, output])
						if len(expression_cache) > max_expression_cache:
							del expression_cache[0]
					
					else:

						if var_calc == "x":
							x = output_copy_ans
						
						if var_calc == "y":
							y = output_copy_ans
						
						if var_calc == "z":
							z = output_copy_ans

						expression = ["|"]
						var_calc = have_var[have_var.index(var_calc) + 1]
						out1.config(text = scr_exp(expression_cache[-1]).replace("|", ""))
						out2.config(text = f"{var_calc} = {scr_exp(expression)}")
					
					if calc_mode_cache == "Normal":
						calc_mode = calc_mode_cache
					
					elif calc_mode_cache == "CALC1":
						calc_mode = "CALC"
						out2_var()
						up_down_cache()

		else:
			
			if calc_mode == "Calculating":
				
				try:
					if expression_cache[-1][1] == None:
						del expression_cache[-1]
				except:
					pass
				
				if calc_mode_cache == "Normal":
					enter_eq = 0
					expression_cache.append([expression, None])

				out1.config(anchor = "nw")
				error_message()
		
		PNA_button()
		
	out1.config(anchor = "nw")
	cache_count = 0
	up_down_cache()

app = tk.Tk()
app.geometry(f"{width_screen}x{height_screen}")
app.resizable(False, False)
app.title(f"Casio fx - 880BTG Emulator ~ {version_of_calc}")
icon_app = PhotoImage(file = "icon.png")
app.iconphoto(False, icon_app)

calculator_screen = Frame(app)
calculator_screen.place(x = 0, y = 0, height = height_screen*8/55, width = width_screen)

up_cache = tk.Label(app, text = "↑", bg = "black", fg = "black")
up_cache.place(x = width_screen*137/144, y = height_screen*5/33, height = height_screen*7/330, width = width_screen*5/72)

down_cache = tk.Label(app, text = "↓", bg = "black", fg = "black")
down_cache.place(x = width_screen*65/72, y = height_screen*5/33, height = height_screen*7/330, width = width_screen*5/72)

shift_screen = tk.Label(app, text = "S", bg = "black", fg = "black")
shift_screen.place(x = width_screen*41/48, y = height_screen*5/33, height = height_screen*7/330, width = width_screen*5/72)

out1 = tk.Label(calculator_screen, text = expression, font = "unifont", bg = "black", fg = "white", justify = "left", anchor = "nw", wraplength = width_screen)
out1.place(x = 0, y = 0, height = height_screen/11, width = width_screen)

#----------expression input screen----------

out2 = tk.Label(calculator_screen, text = output, font = "unifont", bg = "black", fg = "white", anchor = "e")
out2.place(x = 0, y = height_screen/11, height = height_screen*3/55, width = width_screen)

#-----------output screen----------

button_Ans = tk.Button(app, text = "∆ = 0", bg = "white", justify = "left", anchor = "nw", wraplength = 330, font = ("Arial", 6), command = lambda: add("∆"))
button_Ans.place(x= width_screen*91/144, y = height_screen*8/33, height = height_screen*2/55, width = width_screen*53/144)

button_ON = tk.Button(app, text = "ON", bg = "white", command = lambda: on())
button_ON.place(x = width_screen/144, y = height_screen*49/330, height = height_screen*7/165, width = width_screen*7/72)

button_check = tk.Button(app, text = "Check", bg = "white", font = ("", 5), command = lambda: check())
button_check.place(x = width_screen/9, y = height_screen*49/330, height = height_screen*7/165, width = width_screen*7/72)

button_setting = tk.Button(app, text = "Set", bg = "white", command = lambda: setting())
button_setting.place(x = width_screen/144, y = height_screen*32/165, height = height_screen*7/165, width = width_screen*7/72)

button_shift = tk.Button(app, text = "Shift", bg = "white", command = lambda: shift())
button_shift.place(x = width_screen/9, y = height_screen*32/165, height = height_screen*7/165, width = width_screen*7/72)

button_calc_exp = tk.Button(app, text = "CALC", bg = "white", command = lambda: calc_exp())
button_calc_exp.place(x = width_screen/144, y = height_screen*79/330, height = height_screen*7/165, width = width_screen*7/72)

button_left = tk.Button(app, text = "<", bg = "white", command = lambda: bar_left())
button_left.place(x = width_screen*43/144, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)

button_right = tk.Button(app, text = ">", bg = "white", command = lambda: bar_right())
button_right.place(x = width_screen*73/144, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)

button_OK = tk.Button(app, text = "OK", bg = "white", command = lambda: solve_screen())
button_OK.place(x = width_screen*29/72, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)

button_up = tk.Button(app, text = "˄", bg = "white", command = lambda: bar_up())
button_up.place(x = width_screen*29/72, y = height_screen*49/330, height = height_screen*13/330, width = width_screen*13/144)

button_down = tk.Button(app, text = "˅", bg = "white", command = lambda: bar_down())
button_down.place(x = width_screen*29/72, y = height_screen*79/330, height = height_screen*13/330, width = width_screen*13/144)

button_catalog = tk.Button(app, text = "ctl", bg = "white", command = lambda: catalog())
button_catalog.place(x = width_screen*73/144, y = height_screen*79/330, height = height_screen*13/330, width = width_screen*13/144)

button_end_left = tk.Button(app, text = "←", fg = "blue", command = lambda: end_left())
button_end_left.place(x = width_screen*11/18, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)

button_end_right = tk.Button(app, text = "→", fg = "blue", command = lambda: end_right())
button_end_right.place(x = width_screen*103/144, y = height_screen*32/165, height = height_screen*13/330, width = width_screen*13/144)

#----------navigation bar button---------

button_1 = tk.Button(app, text = "1", bg = "white", command = lambda: add("1"))
button_1.place(x = width_screen/48, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)

button_2 = tk.Button(app, text = "2", bg = "white", command = lambda: add("2"))
button_2.place(x = width_screen*25/144, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)

button_3 = tk.Button(app, text = "3", bg = "white", command = lambda: add("3"))
button_3.place(x = width_screen*47/144, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)

button_del = tk.Button(app, text = "Del", bg = "white", command = lambda: delete())
button_del.place(x = width_screen*23/48, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)

button_ac = tk.Button(app, text = "AC", bg = "white", command = lambda: ac())
button_ac.place(x = width_screen*91/144, y = height_screen*31/110, height = height_screen*2/33, width = width_screen*5/36)

#---------------line 1---------------

button_4 = tk.Button(app, text = "4", bg = "white", command = lambda: add("4"))
button_4.place(x = width_screen/48, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)

button_5 = tk.Button(app, text = "5", bg = "white", command = lambda: add("5"))
button_5.place(x = width_screen*25/144, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)

button_6 = tk.Button(app, text = "6", bg = "white", command = lambda: add("6"))
button_6.place(x = width_screen*47/144, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)

button_time = tk.Button(app, text = "×", bg = "white", command = lambda: add("×"))
button_time.place(x = width_screen*23/48, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)

button_div = tk.Button(app, text = "÷", bg = "white", command = lambda: add("÷"))
button_div.place(x = width_screen*91/144, y = height_screen*23/66, height = height_screen*2/33, width = width_screen*5/36)

#---------------line 2---------------

button_7 = tk.Button(app, text = "7", bg = "white", command = lambda: add("7"))
button_7.place(x = width_screen/48, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)

button_8 = tk.Button(app, text = "8", bg = "white", command = lambda: add("8"))
button_8.place(x = width_screen*25/144, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)

button_9 = tk.Button(app, text = "9", bg = "white", command = lambda: add("9"))
button_9.place(x = width_screen*47/144, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)

button_plus = tk.Button(app, text = "+", bg = "white", command = lambda: add("+"))
button_plus.place(x = width_screen*23/48, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)

button_minus = tk.Button(app, text = "-", bg = "white", command = lambda: add("-"))
button_minus.place(x = width_screen*91/144, y = height_screen*137/330, height = height_screen*2/33, width = width_screen*5/36)

#---------------line 3---------------

button_0 = tk.Button(app, text = "0", bg = "white", command = lambda: add("0"))
button_0.place(x = width_screen/48, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)

button_dot = tk.Button(app, text = ".", bg = "white", command = lambda: add("."))
button_dot.place(x = width_screen*25/144, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)

button_pi = tk.Button(app, text = "π", bg = "white", command = lambda: add("π"))
button_pi.place(x = width_screen*47/144, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)

button_euler = tk.Button(app, text = "e", bg = "white", command = lambda: add("e"))
button_euler.place(x = width_screen*23/48, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)

button_exe = tk.Button(app, text = "=", bg = "white", command = lambda: solve_screen())
button_exe.place(x = width_screen*91/144, y = height_screen*53/110, height = height_screen*2/33, width = width_screen*5/36)

#---------------line 4---------------

button_sin = tk.Button(app, text = "sin(", bg = "white", command = lambda: add("sin("))
button_sin.place(x = width_screen/48, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)

button_cos = tk.Button(app, text = "cos(", bg = "white", command = lambda: add("cos("))
button_cos.place(x = width_screen*25/144, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)

button_tan = tk.Button(app, text = "tan(", bg = "white", command = lambda: add("tan("))
button_tan.place(x = width_screen*47/144, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)

button_open_parenthesis = tk.Button(app, text = "(", bg = "white", command = lambda: add("("))
button_open_parenthesis.place(x = width_screen*23/48, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)

button_sqrt = tk.Button(app, text = "√", bg = "white", command = lambda: add("√("))
button_sqrt.place(x = width_screen*91/144, y = height_screen*181/330, height = height_screen*2/33, width = width_screen*5/36)

button_asin = tk.Button(app, text = "asin(", bg = "white", command = lambda: add("asin("))
button_asin.place(x = width_screen/48, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)

button_acos = tk.Button(app, text = "acos(", bg = "white", command = lambda: add("acos("))
button_acos.place(x = width_screen*25/144, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)

button_atan = tk.Button(app, text = "atan(", bg = "white", command = lambda: add("atan("))
button_atan.place(x = width_screen*47/144, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)

button_close_parenthesis = tk.Button(app, text = ")", bg = "white", command = lambda: add(")"))
button_close_parenthesis.place(x = width_screen*23/48, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)

button_power = tk.Button(app, text = "^", bg = "white", command = lambda: add("^"))
button_power.place(x = width_screen*91/144, y = height_screen*203/330, height = height_screen*2/33, width = width_screen*5/36)


button_log = tk.Button(app, text = "log(", bg = "white", command = lambda: add("log("))
button_log.place(x = width_screen/48, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)

button_sigma = tk.Button(app, text = "Σ(", bg = "white", command = lambda: add("Σ("))
button_sigma.place(x = width_screen*25/144, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)

button_x_var = tk.Button(app, text = "x", bg = "white", command = lambda: add("x"))
button_x_var.place(x = width_screen*47/144, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)

button_comma = tk.Button(app, text = ",", bg = "white", command = lambda: add(","))
button_comma.place(x = width_screen*23/48, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)

button_frac = tk.Button(app, text = "!", bg = "white", command = lambda: add("!"))
button_frac.place(x = width_screen*91/144, y = height_screen*15/22, height = height_screen*2/33, width = width_screen*5/36)

button_y_var = tk.Button(app, text = "y", bg = "white", command = lambda: add("y"))
button_y_var.place(x = width_screen/48, y = height_screen*247/330, height = height_screen*2/33, width = width_screen*5/36)

button_z_var = tk.Button(app, text = "z", bg = "white", command = lambda: add("z"))
button_z_var.place(x = width_screen*25/144, y = height_screen*247/330, height = height_screen*2/33, width = width_screen*5/36)

text_imagnum_mode = tk.Label(app, text = "Imaginary number mode", fg = "blue", font = ("Arial", 4))
text_imagnum_mode.place(x = width_screen*37/48, y = height_screen/3)

button_ON_imagnum_mode = tk.Button(app, text = "ON", fg = "blue", command = lambda: on_imag_num(), state = "normal")
button_ON_imagnum_mode.place(x = width_screen*115/144, y = height_screen*59/165, height = height_screen/33, width = width_screen*5/72)

button_OFF_imagnum_mode = tk.Button(app, text = "OFF", fg = "blue", command = lambda: off_imag_num(), state = "disabled")
button_OFF_imagnum_mode.place(x = width_screen*127/144, y = height_screen*59/165, height = height_screen/33, width = width_screen*5/72)

text_decimal_mode = tk.Label(app, text = "Decimal number mode", fg = "blue", font = ("Arial", 4))
text_decimal_mode.place(x = width_screen*37/48, y = height_screen*43/110)

button_ON_decimal_mode = tk.Button(app, text = "ON", fg = "blue", command = lambda: on_deci_num(), state = "normal")
button_ON_decimal_mode.place(x = width_screen*115/144, y = height_screen*9/22, height = height_screen/33, width = width_screen*5/72)

button_OFF_decimal_mode = tk.Button(app, text = "OFF", fg = "blue", command = lambda: off_deci_num(), state = "disable")
button_OFF_decimal_mode.place(x = width_screen*127/144, y = height_screen*9/22, height = height_screen/33, width = width_screen*5/72)

button_prime_number_analysis = tk.Button(app, text = "PNA", fg = "blue", command = lambda: PNA(), state = "disable")
button_prime_number_analysis.place(x = width_screen*115/144, y = height_screen*53/110, height = height_screen/33, width = width_screen*11/72)

init_key()
change_language()
app.bind("<KeyPress>", on_key_press)
check_data()
app.protocol("WM_DELETE_WINDOW", close_app)
app.bind("<Button-1>", lambda event: pointer(True))
pointer_thread()
app.mainloop()