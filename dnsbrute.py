import dns.resolver

host =input("host alvo: ")
tp ="A"
res = dns.resolver.Resolver()
arquivo = open("/home/kali/sublist.txt","r")
subdominios = arquivo.read().splitlines()

for subdominio in subdominios:
	try:
		sub_alvo = subdominio + "." + host
		resultado = res.resolve(sub_alvo,tp)
		for ip in resultado:
			print (sub_alvo, "->", ip)
	except:
		pass
