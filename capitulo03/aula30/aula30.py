from cnpj import generate, checkvalidate

cn_a, cn_b, cn_h, cn_i = "04.252.011/0001-10", "00.000.000/0000-00", "22.222.222/2222-22", "aa.aaa.aaa/aaaa-aa"
cn_c, cn_d, cn_e, cn_f, cn_g, cn_j = generate(), generate(), generate(), generate(), generate(), generate()
list_cnpj = [cn_a, cn_b, cn_c, cn_d, cn_e, cn_f, cn_g, cn_h, cn_i, cn_j]

for cn in list_cnpj:
    checkvalidate(cn)

