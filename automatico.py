import tweepy
import time
import random 
import os

#definição das chaves
api_key = os.environ['TWITTER_API_KEY']
api_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
client = tweepy.Client(
    bearer_token,
    api_key,
    api_secret,
    access_token,
    access_secret,
    wait_on_rate_limit=True,
)

#transforma os arquivos em listas
with open('nomes.txt', 'r', encoding='utf-8') as arq:
    nomes = arq.readlines()
with open('substantivos.txt', 'r', encoding='utf-8') as arq:
    substantivos = arq.readlines()
with open('verbos.txt', 'r', encoding='utf-8') as arq:
    verbos = arq.readlines()
with open('adjetivos.txt', 'r', encoding='utf-8') as arq:
    adjetivos = arq.readlines()
with open('locais.txt', 'r', encoding='utf-8') as arq:
    locais = arq.readlines()
with open('cidades.txt', 'r', encoding='utf-8') as arq:
    cidades = arq.readlines()
with open('objetos.txt', 'r', encoding='utf-8') as arq:
    objetos = arq.readlines()
with open('generos.txt', 'r', encoding='utf-8') as arq:
    generos = arq.readlines()
with open('diretores.txt', 'r', encoding='utf-8') as arq:
    diretores = arq.readlines()
with open('atores.txt', 'r', encoding='utf-8') as arq:
    atores = arq.readlines()



#escolhe a os nomes aleatorios dos arquivos
nome = random.choice(nomes) 
nome = nome.rstrip('\n')
time.sleep(1)
substantivo = random.choice(substantivos) 
substantivo = substantivo.rstrip('\n')
time.sleep(2)
verbo = random.choice(verbos) 
verbo = verbo.rstrip('\n')
time.sleep(1)
adjetivo = random.choice(adjetivos) 
adjetivo = adjetivo.rstrip('\n')
time.sleep(1)
local = random.choice(locais) 
local = local.rstrip('\n')
time.sleep(1)
cidade = random.choice(cidades) 
cidade = cidade.rstrip('\n')
time.sleep(1)
objeto = random.choice(objetos) 
objeto = objeto.rstrip('\n')
time.sleep(1)
genero = random.choice(generos) 
genero = genero.rstrip('\n')
time.sleep(1)
diretor = random.choice(diretores) 
diretor = diretor.rstrip('\n')
time.sleep(1)
ator1 = random.choice(atores) 
ator1 = ator1.rstrip('\n')
time.sleep(1)
ator2 = random.choice(atores) 
ator2 = ator2.rstrip('\n')
time.sleep(1)
ator3 = random.choice(atores) 
ator3 = ator3.rstrip('\n')
        

def postafrase(aswr):
    if aswr == 1:
        rpt = random.choice(nomes) 
        rpt = rpt.rstrip('\n')
        client.create_tweet(text="Nome: " + nome + " quer " + verbo + " " + rpt + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(nome + " quer " + verbo + " " + nome + "\n")
    elif aswr == 2:
        client.create_tweet(text="Nome: " + "O " + verbo + " de " + nome + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print("o " + verbo + " de " + nome + "\n")
    elif aswr == 3:
        client.create_tweet(text="Nome: " + cidade + " uma cidade " + adjetivo + "\n" + "Genero: " + "Documentario" + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(cidade + " uma cidade " + adjetivo + " (O DOCUMENTARIO)" + "\n")
    elif aswr == 4:
        client.create_tweet(text="Nome: " + nome + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(nome + "\n")
    elif aswr == 5:
        client.create_tweet(text="Nome: " + objeto + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(objeto + "\n")
    elif aswr == 6:
        client.create_tweet(text="Nome: " + "O " + substantivo + " do " + nome + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print("o " + substantivo + " do " + nome + "\n")
    elif aswr == 7:
        client.create_tweet(text="Nome: " + substantivo + " " + adjetivo + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(substantivo + " " + adjetivo + "\n")
    elif aswr == 8:
        rpt = random.choice(substantivos) 
        rpt = rpt.rstrip('\n')
        client.create_tweet(text="Nome: " + substantivo + " de " + rpt + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(substantivo + " de " + rpt + "\n")
    elif aswr == 9:
        client.create_tweet(text="Nome: " + local + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(local + "\n")
    elif aswr == 10:
        client.create_tweet(text="Nome: " + nome + " " + adjetivo + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(nome + " " + adjetivo + "\n")
    elif aswr == 11:
        client.create_tweet(text="Nome: " + nome + " " + adjetivo + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(nome + " " + adjetivo + "\n")
    elif aswr == 12:
        client.create_tweet(text="Nome: " + "Cuidado com o " + local + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print("cuidado com o " + local + "\n")
    elif aswr == 13:
        client.create_tweet(text="Nome: " + substantivo + " de " + nome + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(substantivo + " de " + nome + "\n")
    elif aswr == 14:
        client.create_tweet(text="Nome: " + cidade + " em caos" + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(cidade + " em caos" + "\n")
    elif aswr == 15:
        rpt = random.choice(nomes) 
        rpt = rpt.rstrip('\n')
        client.create_tweet(text="Nome: " + nome + ", " + rpt + " e o " + objeto + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(nome + ", " + rpt + " e o " + objeto + "\n")
    elif aswr == 16:
        rpt = random.choice(objetos) 
        rpt = rpt.rstrip('\n')
        client.create_tweet(text="Nome: " + objeto + ", " + rpt + " e outras coisas" + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(objeto + ", " + rpt + " e outras coisas" + "\n" )
    elif aswr == 17:
        client.create_tweet(text="Nome: " + local + " " + adjetivo + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(local + " " + adjetivo + "\n")
    elif aswr == 18:
        client.create_tweet(text="Nome: " + substantivo + " " + adjetivo + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(substantivo + " " + adjetivo + "\n")
    elif aswr == 19:
        client.create_tweet(text="Nome: " + verbo + " " + adjetivo + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(verbo + " " + adjetivo + "\n")
    elif aswr == 20:
        client.create_tweet(text="Nome: " + verbo + " " + adjetivo + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(verbo + " " + adjetivo + "\n")
    elif aswr == 21:
        client.create_tweet(text="Nome: " + local + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(local + "\n")
    elif aswr == 22:
        rpt = random.choice(cidades) 
        rpt = rpt.rstrip('\n')
        client.create_tweet(text="Nome: " + cidade + " vs " + rpt + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(cidade + " vs " + rpt + "\n")
    elif aswr == 23:
        rpt = random.choice(nomes) 
        rpt = rpt.rstrip('\n')
        client.create_tweet(text="Nome: " + nome + " vs " + rpt + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print(nome + " vs " + rpt + "\n")
    elif aswr == 24:
        client.create_tweet(text="Nome: " + "O " + objeto + " do " + local + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print("o " + objeto + " do " + local + "\n")
    elif aswr == 25:
        client.create_tweet(text="Nome: " + "O assasinato de " + nome + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print("o assasinato de " + nome + "\n")
    elif aswr == 26:
        client.create_tweet(text="Nome: " + "O assasino da " + local + "\n" + "Genero: " + genero + "\n" + "Diretor: " + diretor + "\n" + "Elenco principal: " + ator1 + ", " + ator2 + ", " + ator3)
        print("o assasino da " + local + "\n")

#função main
def main():
    aswr = random.randint(1,26)
    postafrase(aswr)
main()
