word = "Testing"
list_a = ["O", "rato", "roeu", "a", "roupa", "do", "rei", "de", "Roma"]
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
text_aux = "Item1@Item2@Item3"

expression_a = list(word)
expression_b = word[0]
expression_c = " ".join(list_a)
expression_d = text.startswith("ipsum")
expression_e = text.endswith("elit.")
expression_f = text.upper()
expression_g = text.lower()
expression_h = "Lorem" in text
expression_i = "rato" not in text
expression_j = "ipsum" not in text
expression_k = text.count("Lorem")
expression_l = text.count("abacaxi")
expression_m = text.find("consectetur")
expression_n = text.find("Roma")
expression_o = text.split(",")
expression_p = text_aux.split("@")
expression_q = text.replace("Lorem", "LOREM")
expression_r = text.isdigit()

list_expressions = [
    expression_a, expression_b, expression_c, expression_d, expression_e, expression_f, expression_g, expression_h,
    expression_i, expression_j, expression_k, expression_l, expression_m, expression_n, expression_o, expression_p,
    expression_q, expression_q    
]

for expression in list_expressions:
    print(expression)

