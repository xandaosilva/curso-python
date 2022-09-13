from cnpj import generate, checkvalidate

cn_a = "04.252.011/0001-10"
cn_b = "00.000.000/0000-00"
cn_c = generate()
cn_d = generate()
cn_e = generate()
cn_f = generate()
cn_g = generate()
cn_h = "22.222.222/2222-22"
cn_i = "aa.aaa.aaa/aaaa-aa"
cn_j = generate()

checkvalidate(cn_a)
checkvalidate(cn_b)
checkvalidate(cn_c)
checkvalidate(cn_d)
checkvalidate(cn_e)
checkvalidate(cn_f)
checkvalidate(cn_g)
checkvalidate(cn_h)
checkvalidate(cn_i)
checkvalidate(cn_j)
