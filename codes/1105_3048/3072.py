# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
n = input( " Digite o nome do brasao: " )

lobo    = "Stark"
leao    = "Lannister"
veado   = "Baratheon"
dragao  = "Targaryen"
rosa    = "Tyrell"
sol     = "Martell"
lula    = "Greyjoy"
esfolado= "Bolton"
turta   = "Tully"


print(" Entrada: " ,n)

if ((n!="lobo") and (n!="leao") and (n!="veado") and (n!="dragao") and (n!="rosa") and (n!="sol") and (n!="lula") and (n!="esfolado") and (n!="turta")):
	mensagem = " Brasao invalido "
	print(mensagem)
elif(n=="lobo"):
	mensagem = " Casa: Stark "
	print(mensagem)
elif(n=="leao"):
	mensagem = " Casa: Lannister "
	print(mensagem)
elif(n=="veado"):
	mensagem = " Casa: Baratheon"
	print(mensagem)
elif(n=="dragao"):
	mensagem = " Casa: Targaryen "
	print(mensagem)
elif(n=="rosa"):
	mensagem = " Casa: Tyrell"
	print(mensagem)
elif(n=="sol"):
	mensagem = " Casa: Martell "
	print(mensagem)
elif(n=="lula"):
	mensagem = " Casa: Greyjoy "
	print(mensagem)
elif(n=="esfolado"):
	mensagem = " Casa: Bolton "
	print(mensagem)
elif(n=="turta"):
	mensagem = " Casa: Tully "
	print(mensagem)